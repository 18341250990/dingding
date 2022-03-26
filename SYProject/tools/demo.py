# -*- coding: utf-8 -*-
"""
@Description : 
@File        : demo.py
@Project     : SYProject
@Time        : 2022/3/2 下午7:33
@Author      : dj
@Software    : PyCharm
"""


class Demo:

    # 冒泡排序 时间复杂度也为O(n^2) 空间复杂度也为O(1)
    def bubble(self, arr):
        for i in range(len(arr) - 1):
            for j in range(len(arr) - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j+1], arr[j] = arr[j], arr[j+1]
        return arr


    #选择排序 时间复杂度也为O(n^2) 空间复杂度也为O(1)
    def selection(self, arr):
        for i in range(len(arr)-1):
            min = i
            for j in range(i+1,len(arr)):
                if arr[j] < arr[min]:
                    min = j
            if i != min:
                arr[min], arr[i] = arr[i], arr[min]

        return arr


    #插入排序 时间复杂度也为O(n^2) 空间复杂度也为O(1)
    def insertion(self, arr):
        for i in range(1, len(arr)):
            cur = arr[i]
            pre_min = i - 1
            while pre_min >= 0 and arr[pre_min] > cur:
                arr[pre_min + 1] = arr[pre_min]
                pre_min -= 1
            arr[pre_min+1] = cur
        return arr


    #归并排序 时间复杂度： 复杂度为O(nlog^n) 空间复杂度也为O(n)
    def merge_sort(self,arr):
        if len(arr) == 1:
            return arr
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        return self.merge(self.merge_sort(left), self.merge_sort(right))

    def merge(self, left, right):
        res = []
        while len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                res.append(left.pop(0))
            else:
                res.append(right.pop(0))
        res += left
        res += right
        return res

    #希尔排序
    def shellSort(self, arr):
        gap = 1
        while (gap < len(arr) / 3):
            gap = gap * 3 + 1
        while gap > 0:
            for i in range(gap, len(arr)):
                temp = arr[i]
                j = i - gap
                while j >= 0 and arr[j] > temp:
                    arr[j + gap] = arr[j]
                    j -= gap
                arr[j + gap] = temp
            gap //=3
        return arr

    #记数排序 需要列表的最大值
    def countingSort(self, arr, maxValue):
        bucketLen = maxValue + 1
        bucket = [0] * bucketLen
        sortedIndex = 0
        arrLen = len(arr)
        for i in range(arrLen):
            if not bucket[arr[i]]:
                bucket[arr[i]] = 0
            bucket[arr[i]] += 1
        for j in range(bucketLen):
            while bucket[j] > 0:
                arr[sortedIndex] = j
                sortedIndex += 1
                bucket[j] -= 1
        return arr


    #快速排序 时间复杂度：O(nlogn) 空间复杂度：O(nlogn)
    def quick_sort(self, arr):
        if len(arr) == 1:
            return arr
        mid = arr.pop(len(arr) // 2)
        left, right = [], []
        for item in arr:
            if item >= mid:
                right.append(item)
            else:
                left.append(item)
        return self.quick_sort(left) + [mid] + self.quick_sort(right)


    #找出一个列表中重复数字的个数
    def duplicate(self,arr):
        import collections
        li = {}
        dict = {}
        for i in arr:
            dict[i] = dict.get(i, 0) + 1
        print(dict)

        nums = collections.Counter(arr)
        e = collections.Counter("ANKAJSHDAK")

        # print(sorted(e.elements()))
        for num in nums:
            li[num] = nums[num]
        return li




if __name__ == '__main__':
    d = Demo()
    arr = [1, 3, 45, 6, 7, 23, 42, 31, 21, 8, 7]

    # arry = Demo().bubble(arr)
    # arry = d.selection(arr)
    # arry = d.insertion(arr)
    # arry = d.merge_sort(arr)
    # arry = d.shellSort(arr)
    # arry = d.countingSort(arr,45)
    arry = d.quick_sort(arr)
    print(arry)
    li = d.duplicate(arr)




def chengfa():
    for i in range(1,10):
        for j in range(1,i+1):
            print(f"{i}*{j}={i*j} ",end='')
        print()
# chengfa()