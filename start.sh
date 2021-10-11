echo "##teamcity[blockOpened name='environment']"
env
echo "##teamcity[blockClosed name='environment']"

set -ex

if [ "%balance.docker_name%" != "" ] ; then
    branch_id_raw="%balance.docker_name%"
elif [ "%balance.arcadia_pr_id%" != "" ] ; then
    branch_id_raw="pr-%balance.arcadia_pr_id%"
elif [ "%billing.vhost.branch%" != "%billing.vhost.stableBranch%" ] && [ "%billing.vhost.branch%" != "" ] ; then
    branch_id_raw="%billing.vhost.branch%"
else
    echo "At least one of this must be specified: balance.docker_name, balance.arcadia_pr_id or not released billing.vhost.branch"
    exit 1
fi
branch_id=`echo "$branch_id_raw" | tr [:upper:] [:lower:] | tr "./_" "-"`
branch_dir="/home/${USER}/%billing.branch.work_dir%/$branch_id"
echo "ENV VARS"

echo "##teamcity[setParameter name='env.branch_id_raw' value='$branch_id_raw']"
echo "##teamcity[setParameter name='env.branch_id' value='$branch_id']"
echo "##teamcity[setParameter name='env.branch_dir' value='$branch_dir']"
echo "##teamcity[setParameter name='balance.arcadia_dir' value='$branch_dir/arcadia']"

# prepare branch
set -xe
USERNAME="$USER"

echo "REMOVING OLD REPOS..."
find "/home/$USERNAME/%billing.branch.work_dir%" -maxdepth 1 -mtime "+%billing.branch.max_ttl%" -type d -exec sudo rm -Rf "{}" \;

echo "REMOVING OLD LOGS..."
find "%billing.branch.logs_dir%" -maxdepth 1 -mtime "+%billing.branch.logs_max_ttl%" -type d -exec sudo rm -Rf "{}" \;
find "%billing.branch.logs_dir%" -name *.log* -mtime "+%billing.branch.logs_max_ttl%" -type f -exec sudo rm -Rf "{}" \;

echo "CREATING BRANCH DIR..."
mkdir -p "%env.branch_dir%"
echo %balance.arcadia_pr_id% > "%env.branch_dir%/arcadia_pr_id"

echo "PULLING CONFIGS..."
test -f /mnt/remote/greed-tm1h.paysys.yandex.net/etc/oracle/tnsnames.ora
test -f /mnt/remote/greed-tm1h.paysys.yandex.net/etc/yandex/balance-common/components.cfg.xml
if [ "%billing.runTVMTool%" = "yes" ]
then
  test -f /mnt/remote/greed-tm1h.paysys.yandex.net/etc/tvmtool/tvmtool.conf
fi

rm -rf /home/$USERNAME/%billing.branch.work_dir%/%env.branch_id%/etc
cp -r --no-dereference --no-preserve=mode,ownership /mnt/remote/greed-tm1h.paysys.yandex.net/etc /home/$USERNAME/%billing.branch.work_dir%/%env.branch_id%/etc 2>/dev/null || :

# Checkouting billing folder in this instance of svn.
svn update "%balance.arcadia_dir%/billing"

# Svn up
if [ "%balance.arcadia_revision%" != "" ]; then
  svn up "-r%balance.arcadia_revision%" "%balance.arcadia_dir%"
fi

# Prep binaries
set -ex

BINARIES_DIR="/home/$USER/%billing.branch.work_dir%/%env.branch_id%/binaries"

docker stop "%env.branch_id%" || true

mkdir -p "$BINARIES_DIR"

if [ "%balance.balance_binary_url%" != "" ] ; then
    wget "%balance.balance_binary_url%" -O "$BINARIES_DIR/balance-binary"
fi
if [ "%balance.snout_proxy_binary_url%" != "" ] ; then
    wget "%balance.snout_proxy_binary_url%" -O "$BINARIES_DIR/yb-snout-proxy-binary"
fi

if [ ! -f "$BINARIES_DIR/balance-binary" ] ; then
    echo "balance-binary is absent. Provide balance.balance_binary_url parameter. Or put binary manually into $BINARIES_DIR/balance-binary"
fi
if [ ! -f "$BINARIES_DIR/yb-snout-proxy-binary" ] ; then
    echo "yb-snout-proxy-binary is absent. Provide balance.snout_proxy_binary_url parameter. Or put binary manually into $BINARIES_DIR/yb-snout-proxy-binary"
fi

chmod a+x "$BINARIES_DIR/balance-binary"
chmod a+x "$BINARIES_DIR/yb-snout-proxy-binary"

# Update vhost
set -x
branch_dir="/home/${USER}/%billing.branch.work_dir%/%env.branch_id%"
vhost_checkout_dir="$branch_dir/vhost"

echo "This tools directory is legacy. This is vhost rep now"
vhost_dir="vhost"

if [ "%billing.vhost.code%" = "clean" ] ; then
    echo "Removing vhost dir"
    sudo rm -Rf "$vhost_checkout_dir"
fi

if [ ! -d "$vhost_checkout_dir" ] ; then
    echo "NO VHOST DIR FOUND. CLONING..."
    git clone --single-branch -b "%billing.vhost.branch%" ssh://git@bb.yandex-team.ru/billing/tools.git "$vhost_checkout_dir"
elif [ "%billing.vhost.code%" = "existing" ] ; then
    echo "Using existing vhost code without cloning or updating"
else
    echo "VHOST DIR FOUND. UPDATING..."

    cd "$vhost_checkout_dir"

    git clean -fdx
    git reset --hard
    git pull

    cd ..
fi

# Update QA
qa_dir="qa"

if [ "%billing.needQAWeb%" = "yes" ] ; then
    echo "Clone QA web app"

    set -x

    cd "/home/$(whoami)/%billing.branch.work_dir%/%env.branch_id%"

    sudo rm -Rf "$qa_dir"

    git clone "git@github.yandex-team.ru:Billing/yb-qa-web.git" "$qa_dir"

    cd "$qa_dir"

    sudo -n git clean -fdx

    git reset --hard
    git checkout develop
    git pull
    git fetch origin "%billing.qa.branch%"
    git branch -D "%billing.qa.branch%" || true
    git checkout -b "%billing.qa.branch%" FETCH_HEAD || true
else
    mkdir -p "$qa_dir"
fi

# Docker prepare
set -x

docker pull "%billing.dockerImage%"
docker rm -f "%env.branch_id%" || true
docker network disconnect -f bridge "%env.branch_id%" || true

# Docker build
set -ex

docker run \
       --rm \
       --name "%env.branch_id%" \
       -e DOCKER_BALANCE_DB="%billing.branch.balance_db%" \
       -e NEED_STORYBOOK=%billing.needStorybook% \
       -e NEED_QA_WEB=%billing.needQAWeb% \
       -v /home/${USER}/.secret:/.secret:ro \
       -v "%balance.arcadia_dir%/billing/balance:/tools" \
       -v "/home/${USER}/%billing.branch.work_dir%/%env.branch_id%/venvs:/venvs" \
       -v "%balance.arcadia_dir%/billing/snout:/snout" \
       -v "%balance.arcadia_dir%/billing/balance_utils:/balance-utils" \
       -v "/home/${USER}/%billing.branch.work_dir%/%env.branch_id%/vhost:/vhost" \
       -v "/home/${USER}/%billing.branch.work_dir%/%env.branch_id%/qa:/qa" \
       -v /var/cache/geobase:/var/cache/geobase \
       -v "/home/${USER}/.ssh:/root/.ssh" \
       %billing.dockerImage% \
       /build.sh

# docker run
set -x

BRANCH_DIR="/home/$(whoami)/%billing.branch.work_dir%/%env.branch_id%"

docker run \
       -d \
       -P \
       --name "%env.branch_id%" \
       -e DOCKER_BALANCE_DB="%billing.branch.balance_db%" \
       -e CONTAINER_TTL="%billing.branchTTL%d" \
       -e PYTHON_SUFFIX="%billing.pythonVersion%" \
       -e RUN_CRON="%billing.runCron%" \
       -e RUN_TVMTOOL="%billing.runTVMTool%" \
       -e DOCKER_INCREASE_WORKERS="%billing.dockerIncreaseWorkers%" \
       -v "%balance.arcadia_dir%/billing/balance:/tools" \
       -v "%balance.arcadia_dir%/billing/snout:/snout" \
       -v "%balance.arcadia_dir%/billing/balance_utils:/balance-utils" \
       -v "$BRANCH_DIR/vhost:/vhost" \
       -v "$BRANCH_DIR/binaries:/binaries" \
       -v "$BRANCH_DIR/qa:/qa" \
       -v "%billing.branch.logs_dir%/%env.branch_id%:/var/log/yb" \
       -v /var/cache/geobase:/var/cache/geobase \
       -v "$BRANCH_DIR/etc/yandex:/etc/yandex" \
       -v "$BRANCH_DIR/etc/tvmtool:/tvmtool_conf" \
       -v "$BRANCH_DIR/etc/oracle:/opt/oracle/%billing.instant_client_dir%/network/admin" \
       -v "/home/${USER}/.ssh:/root/.ssh" \
       %billing.dockerImage% \
       /run.sh

# print urls
echo "user:        https://user-%env.branch_id%.%billing.branch.host%"
echo "admin:       https://admin-%env.branch_id%.%billing.branch.host%"
echo "snout:       https://snout-%env.branch_id%.%billing.branch.host%/v1/"
echo "jupyter:     https://jupyter-%env.branch_id%.%billing.branch.host%"
echo "xmlrpc:      https://xmlrpc-%env.branch_id%.%billing.branch.host%/xmlrpc"
echo "test-xmlrpc: https://test-xmlrpc-%env.branch_id%.%billing.branch.host%/xmlrpc"
echo "upravlyator: https://balance-xmlrpc-tvm-%env.branch_id%.%billing.branch.host%:8004/idm"

echo "============================================"
echo "USE reclone OPTION IN CASE OF STRANGE ERRORS"
echo "============================================"

# Tag build
set -x

. /etc/oraprofile
. "%billing.ci-venv-dir%/bin/activate"

echo "##teamcity[blockOpened name='environment']"
env
echo "##teamcity[blockClosed name='environment']"

./ci/teamcity_deploy/teamcity_deploy.py \
teamcity_set_build_tag \
--build_id="%teamcity.build.id%" \
--tag_name="%env.branch_id_raw%"