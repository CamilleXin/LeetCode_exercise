# ！usr/bin/env python

__author__ = 'Camille'


def twoSum(nums, target):
    length = len(nums)
    for n in range(0, length - 1):
        for j in range(n + 1, length):
            if nums[n] + nums[j] == target:
                print([n,j])
                return [n, j]
            else:
                continue


if __name__ == '__main__':
    nums = [7, 11, 2, 15]
    target = 9
    twoSum(nums, target)
