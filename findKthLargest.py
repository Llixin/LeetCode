class Solution:
    def partition(self, nums, l, r):
        rand = randint(l, r)
        nums[l], nums[rand], nums[r] = nums[rand], nums[r], nums[l]
        i, j = l, r
        tmp = nums[i]
        while i < j:
            while i < j and nums[j] >= tmp:
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] <= tmp:
                i += 1
            nums[j] = nums[i]
        nums[i] = tmp
        return i

    def quickSort(self, nums, l, r, idx):
        index = self.partition(nums, l, r)
        if index < idx:     return self.quickSort(nums, index + 1, r, idx)
        elif index > idx:   return self.quickSort(nums, l, index - 1, idx)
        else:   return nums[index]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        idx = len(nums) - k
        return self.quickSort(nums, 0, len(nums) - 1, idx)


def main():
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    solu = Solution()
    res = solu.findKthLargest(nums, k)
    print(res)
    
if __name__ == "__main__":
    main()
