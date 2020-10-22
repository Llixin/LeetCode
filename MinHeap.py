class MinHeap:

    def __init__(self, arr):
        print(id(arr))
        self.arr = arr
        self.buildHeap()

    def buildHeap(self):
        n = len(self.arr) - 1
        for i in range((n - 1) // 2, -1, -1):
            self.down(i)

    def down(self, idx=None):
        if idx is None:
            idx = 0
        n = len(self.arr)
        tmp = self.arr[idx]
        i = idx * 2 + 1
        while i < n:
            if i < n - 1 and self.arr[i] > self.arr[i + 1]:
                i += 1
            if tmp <= self.arr[i]:
                break
            self.arr[idx] = self.arr[i]
            idx = i
            i = i * 2 + 1
        self.arr[idx] = tmp

    def up(self, idx=None):
        if idx is None:
            idx = len(self.arr) - 1
        tmp = self.arr[idx]
        i = (idx - 1) // 2
        while i >= 0 and self.arr[i] > tmp:
            self.arr[idx] = self.arr[i]
            idx = i
            i = (idx - 1) // 2
        self.arr[idx] = tmp

    def pushpop(self, val: int):
        self.arr.append(val)
        self.up()
        res = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        self.down()
        return res

    def pop(self):
        val = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        self.down()
        return val


nums = [3, 7, 1, 6, 2, 4, 9, 8, 5]
print(id(nums))
k = 3

# heap = MinHeap(nums[:k])
# for i in range(k, len(nums)):
#     heap.pushpop(nums[i])

heap = MinHeap(nums)
for _ in range(len(nums) - k):
    heap.pop()

print(heap.arr[0])
