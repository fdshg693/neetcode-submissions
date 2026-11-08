class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_dict = {}
        for idx, num in enumerate(nums):
            if target - num in seen_dict:
                return [seen_dict[target - num], idx]
            else:
                # 答えは一つしか存在しない
                # そのため、同一の数字が存在するして上書きが発生するとしても、
                # それは答えにはなりえないので気にしなくてよい
                seen_dict[num] = idx