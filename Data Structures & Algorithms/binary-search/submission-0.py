from bisect import bisect_left, bisect_right

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # target 以上になる最小インデックス
        possible_index = bisect_left(nums, target)
        
        # 配列の長さと一致、つまり配列は全てtargetより小さくマッチがない
        if possible_index == len(nums):
            return -1
        # possible_index が配列内にあることが確定したので、インデックスにアクセスしても安全
        elif nums[possible_index] == target:
            return possible_index
        else:
            return -1
        