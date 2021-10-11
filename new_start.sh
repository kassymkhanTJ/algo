BALANCE_DOCKER_NAME=balance-kasimtj
BALANCE_ARCADIA_REVISION=
BALANCE_ARCADIA_PR_ID=1488163
ENV_BRANCH_DIR=/home/$USER/default_env_branch
ENV_BRANCH_ID=default_env_branch_id
ENV_BRANCH_ID_RAW=default_env_branch_id

BILLING_INSTANT_CLIENT_DIR=instantclient_19_3
BALANCE_ARCADIA_DIR=/home/$USER/arc/arcadia
BILLING_BRANCH_MAX_TTL=14
BILLING_RUNCRON=no
BILLING_BRANCHTTL=1
BILLING_NEEDQAWEB=no
TEAMCITY_BUILD_ID=None
BILLING_RUNTVMTOOL=yes
BILLING_BRANCH_LOGS_MAX_TTL=14
BILLING_PYTHONVERSION=2.7
BILLING_NEEDSTORYBOOK=no
BILLING_DOCKERIMAGE=registry.yandex.net/balance/toolsrun-binary:trusty
BILLING_BRANCH_LOGS_DIR=~/log/branches-testing
BILLING_BRANCH_WORK_DIR=branches-testing
BILLING_DOCKERINCREASEWORKERS=no
BILLING_BRANCH_BALANCE_DB=TEST_BALANCE_YANDEX_RU
BILLING_BRANCH_HOST=greed-branch.paysys.yandex.ru
BALANCE_SNOUT_PROXY_BINARY_URL=
BILLING_VHOST_CODE=clean
BILLING_VHOST_STABLEBRANCH=RELEASE-2_245
BILLING_VHOST_BRANCH=$BILLING_VHOST_STABLEBRANCH
BILLING_QA_BRANCH=master

echo "##teamcity[blockOpened name='environment']"
env
echo "##teamcity[blockClosed name='environment']"

set -ex

if [ "$BALANCE_DOCKER_NAME" != "" ] ; then
    branch_id_raw="$BALANCE_DOCKER_NAME"
elif [ "$BALANCE_ARCADIA_PR_ID" != "" ] ; then
    branch_id_raw="pr-$BALANCE_ARCADIA_PR_ID"
elif [ "$BILLING_VHOST_BRANCH" != "$BILLING_VHOST_STABLEBRANCH" ] && [ "$BILLING_VHOST_BRANCH" != "" ] ; then
    branch_id_raw="$BILLING_VHOST_BRANCH"
else
    echo "At least one of this must be specified: balance.docker_name, balance.arcadia_pr_id or not released billing.vhost.branch"
    exit 1
fi
branch_id=`echo "$branch_id_raw" | tr [:upper:] [:lower:] | tr "./_" "-"`
branch_dir="/home/${USER}/$BILLING_BRANCH_WORK_DIR/$branch_id"
echo "ENV VARS"

echo "##teamcity[setParameter name='env.branch_id_raw' value='$branch_id_raw']"
echo "##teamcity[setParameter name='env.branch_id' value='$branch_id']"
echo "##teamcity[setParameter name='env.branch_dir' value='$branch_dir']"
echo "##teamcity[setParameter name='balance.arcadia_dir' value='$branch_dir/arcadia']"

# prepare branch
set -xe
USERNAME="$USER"

echo "REMOVING OLD REPOS..."
find "/home/$USERNAME/$BILLING_BRANCH_WORK_DIR" -maxdepth 1 -mtime "+$BILLING_BRANCH_MAX_TTL" -type d -exec sudo rm -Rf "{}" \;

echo "REMOVING OLD LOGS..."
find "$BILLING_BRANCH_LOGS_DIR" -maxdepth 1 -mtime "+$BILLING_BRANCH_LOGS_MAX_TTL" -type d -exec sudo rm -Rf "{}" \;
find "$BILLING_BRANCH_LOGS_DIR" -name *.log* -mtime "+$BILLING_BRANCH_LOGS_MAX_TTL" -type f -exec sudo rm -Rf "{}" \;

echo "CREATING BRANCH DIR..."
mkdir -p "$ENV_BRANCH_DIR"
echo $BALANCE_ARCADIA_PR_ID > "$ENV_BRANCH_DIR/arcadia_pr_id"

echo "PULLING CONFIGS..."
test -f /mnt/remote/greed-tm1h.paysys.yandex.net/etc/oracle/tnsnames.ora
test -f /mnt/remote/greed-tm1h.paysys.yandex.net/etc/yandex/balance-common/components.cfg.xml
if [ "$BILLING_RUNTVMTOOL" = "yes" ]
then
  test -f /mnt/remote/greed-tm1h.paysys.yandex.net/etc/tvmtool/tvmtool.conf
fi

rm -rf /home/$USERNAME/$BILLING_BRANCH_WORK_DIR/$ENV_BRANCH_ID/etc
cp -r --no-dereference --no-preserve=mode,ownership /mnt/remote/greed-tm1h.paysys.yandex.net/etc /home/$USERNAME/$BILLING_BRANCH_WORK_DIR/$ENV_BRANCH_ID/etc 2>/dev/null || :

# Checkouting billing folder in this instance of svn.
svn update "$BALANCE_ARCADIA_DIR/billing"

# Svn up
if [ "$BALANCE_ARCADIA_REVISION" != "" ]; then
  svn up "-r$BALANCE_ARCADIA_REVISION" "$BALANCE_ARCADIA_DIR"
fi

# Prep binaries
set -ex

BINARIES_DIR="/home/$USER/$BILLING_BRANCH_WORK_DIR/$ENV_BRANCH_ID/binaries"
BALANCE_BINARY_DIR = /home/$USER/arc/arcadia/billing/balance/bin/balance-binary
YB_BALANCE_SNOUT_PROXY_BINARY_DIR = /home/$USER/arc/arcadia/billing/snout/yb_snout_proxy/binary/yb-snout-proxy-binary

docker stop "$ENV_BRANCH_ID" || true

mkdir -p "$BINARIES_DIR"

if [ ! -f $BALANCE_BINARY_DIR ] ; then
    echo "balance-binary is absent"
fi
if [ ! -f $YB_BALANCE_SNOUT_PROXY_BINARY_DIR ] ; then
    echo "yb-snout-proxy-binary is absent"
fi

cp $BALANCE_BINARY_DIR "$BINARIES_DIR/balance-binary"
cp $YB_BALANCE_SNOUT_PROXY_BINARY_DIR "$BINARIES_DIR/yb-snout-proxy-binary"

chmod a+x "$BINARIES_DIR/balance-binary"
chmod a+x "$BINARIES_DIR/yb-snout-proxy-binary"

# Update vhost
set -x
branch_dir="/home/${USER}/$BILLING_BRANCH_WORK_DIR/$ENV_BRANCH_ID"
vhost_checkout_dir="$branch_dir/vhost"

echo "This tools directory is legacy. This is vhost rep now"
vhost_dir="vhost"

if [ "$BILLING_VHOST_CODE" = "clean" ] ; then
    echo "Removing vhost dir"
    sudo rm -Rf "$vhost_checkout_dir"
fi

if [ ! -d "$vhost_checkout_dir" ] ; then
    echo "NO VHOST DIR FOUND. CLONING..."
    git clone --single-branch -b "$BILLING_VHOST_BRANCH" ssh://git@bb.yandex-team.ru/billing/tools.git "$vhost_checkout_dir"
elif [ "$BILLING_VHOST_CODE" = "existing" ] ; then
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

if [ "$BILLING_NEEDQAWEB" = "yes" ] ; then
    echo "Clone QA web app"

    set -x

    cd "/home/$(whoami)/$BILLING_BRANCH_WORK_DIR/$ENV_BRANCH_ID"

    sudo rm -Rf "$qa_dir"

    git clone "git@github.yandex-team.ru:Billing/yb-qa-web.git" "$qa_dir"

    cd "$qa_dir"

    sudo -n git clean -fdx

    git reset --hard
    git checkout develop
    git pull
    git fetch origin "$BILLING_QA_BRANCH"
    git branch -D "$BILLING_QA_BRANCH" || true
    git checkout -b "$BILLING_QA_BRANCH" FETCH_HEAD || true
else
    mkdir -p "$qa_dir"
fi

# Docker prepare
set -x

docker pull "$BILLING_DOCKERIMAGE"
docker rm -f "$ENV_BRANCH_ID" || true
docker network disconnect -f bridge "$ENV_BRANCH_ID" || true

# Docker build
set -ex

docker run \
       --rm \
       --name "$ENV_BRANCH_ID" \
       -e DOCKER_BALANCE_DB="$BILLING_BRANCH_BALANCE_DB" \
       -e NEED_STORYBOOK=$BILLING_NEEDSTORYBOOK \
       -e NEED_QA_WEB=$BILLING_NEEDQAWEB \
       -v /home/${USER}/.secret:/.secret:ro \
       -v "$BALANCE_ARCADIA_DIR/billing/balance:/tools" \
       -v "/home/${USER}/$BILLING_BRANCH_WORK_DIR/$ENV_BRANCH_ID/venvs:/venvs" \
       -v "$BALANCE_ARCADIA_DIR/billing/snout:/snout" \
       -v "$BALANCE_ARCADIA_DIR/billing/balance_utils:/balance-utils" \
       -v "/home/${USER}/$BILLING_BRANCH_WORK_DIR/$ENV_BRANCH_ID/vhost:/vhost" \
       -v "/home/${USER}/$BILLING_BRANCH_WORK_DIR/$ENV_BRANCH_ID/qa:/qa" \
       -v /var/cache/geobase:/var/cache/geobase \
       -v "/home/${USER}/.ssh:/root/.ssh" \
       $BILLING_DOCKERIMAGE \
       /build.sh

# docker run
set -x

BRANCH_DIR="/home/$(whoami)/$BILLING_BRANCH_WORK_DIR/$ENV_BRANCH_ID"

docker run \
       -d \
       -P \
       --name "$ENV_BRANCH_ID" \
       -e DOCKER_BALANCE_DB="$BILLING_BRANCH_BALANCE_DB" \
       -e CONTAINER_TTL="$BILLING_BRANCHTTLd" \
       -e PYTHON_SUFFIX="$BILLING_PYTHONVERSION" \
       -e RUN_CRON="$BILLING_RUNCRON" \
       -e RUN_TVMTOOL="$BILLING_RUNTVMTOOL" \
       -e DOCKER_INCREASE_WORKERS="$BILLING_DOCKERINCREASEWORKERS" \
       -v "$BALANCE_ARCADIA_DIR/billing/balance:/tools" \
       -v "$BALANCE_ARCADIA_DIR/billing/snout:/snout" \
       -v "$BALANCE_ARCADIA_DIR/billing/balance_utils:/balance-utils" \
       -v "$BRANCH_DIR/vhost:/vhost" \
       -v "$BRANCH_DIR/binaries:/binaries" \
       -v "$BRANCH_DIR/qa:/qa" \
       -v "$BILLING_BRANCH_LOGS_DIR/$ENV_BRANCH_ID:/var/log/yb" \
       -v /var/cache/geobase:/var/cache/geobase \
       -v "$BRANCH_DIR/etc/yandex:/etc/yandex" \
       -v "$BRANCH_DIR/etc/tvmtool:/tvmtool_conf" \
       -v "$BRANCH_DIR/etc/oracle:/opt/oracle/$BILLING_INSTANT_CLIENT_DIR/network/admin" \
       -v "/home/${USER}/.ssh:/root/.ssh" \
       $BILLING_DOCKERIMAGE \
       /run.sh

# print urls
echo "user:        https://user-$ENV_BRANCH_ID.$BILLING_BRANCH_HOST"
echo "admin:       https://admin-$ENV_BRANCH_ID.$BILLING_BRANCH_HOST"
echo "snout:       https://snout-$ENV_BRANCH_ID.$BILLING_BRANCH_HOST/v1/"
echo "jupyter:     https://jupyter-$ENV_BRANCH_ID.$BILLING_BRANCH_HOST"
echo "xmlrpc:      https://xmlrpc-$ENV_BRANCH_ID.$BILLING_BRANCH_HOST/xmlrpc"
echo "test-xmlrpc: https://test-xmlrpc-$ENV_BRANCH_ID.$BILLING_BRANCH_HOST/xmlrpc"
echo "upravlyator: https://balance-xmlrpc-tvm-$ENV_BRANCH_ID.$BILLING_BRANCH_HOST:8004/idm"

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
--build_id="$TEAMCITY_BUILD_ID" \
--tag_name="$ENV_BRANCH_ID_RAW"