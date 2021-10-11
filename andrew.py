def a(nums):
    for i in nums:
        i = abs(i) - 1
        if nums[i] > 0:
            nums[i] *= -1
    return [i + 1 for i in range(len(nums)) if nums[i] > 0]
nums = [1, 2, 5, 4, 2, 2]
print(a(nums))

class A:
    a: str
    async def fetch_by_inn(self):