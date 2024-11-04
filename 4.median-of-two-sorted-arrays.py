#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

import math


# @lc code=start
class Solution:

    def merge_and_get_middle_element(self, A: List[int], B: List[int]):
        result = []
        i = j = 0
        what_over = False
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                result.append(A[i])
                i += 1
                if i == len(A):
                    what_over = False
            else:
                result.append(B[j])
                j += 1
                if j == len(B):
                    what_over = True
        if not what_over:
            result.extend(B[j : len(B)])
        else:
            result.extend(A[i : len(A)])

        print("RESULT", result)
        if len(result) % 2 == 0:
            return (
                result[int((len(result)) / 2)] + result[int((len(result) - 2) / 2)]
            ) / 2
        else:
            print("in here")
            print(result[math.floor(len(result) / 2)])
            return float(result[math.floor(len(result) / 2)])

    def trim(self, A: List[int]):
        print(A)
        if len(A) % 2 == 0:
            return A[math.floor(len(A) / 2) - 1 : math.floor(len(A) / 2)]
        else:
            return A[math.floor(len(A) / 2) - 1 : math.floor(len(A) / 2) + 1]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n_1 = len(nums1)
        n_2 = len(nums2)
        if n_1 > n_2:
            nums1, nums2 = nums2, nums1
        if n_1 < 3:
            if n_2 < 3:
                return self.merge_and_get_middle_element(nums1, nums2)
            else:
                nums2 = self.trim(nums2)
                return self.merge_and_get_middle_element(nums1, nums2)

        median_n1_idx = math.floor(n_1 / 2)
        median_n1 = nums1[median_n1_idx]

        median_n2_idx = math.floor(n_2 / 2)
        median_n2 = nums2[median_n2_idx]

        if median_n1 > median_n2:
            drop_elements = min(n_1 - median_n1_idx, median_n2_idx - 0)
            self.findMedianSortedArrays(
                nums1[0 : n_1 - drop_elements], nums2[drop_elements:n_2]
            )

        else:
            drop_elements = min(median_n1_idx - 0, n_2 - median_n2_idx)
            self.findMedianSortedArrays(
                nums1[drop_elements:n_1], nums2[0 : n_2 - drop_elements]
            )


# @lc code=end
