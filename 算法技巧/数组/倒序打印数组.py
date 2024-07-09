from typing import List

def traverse(arr: List[int], i: int):
    if i == len(arr):
        return
    # 前序位置
    print(arr[i])
    traverse(arr, i + 1)
    # 后序位置
    print(arr[i])

lst = [1,3,2,4]
traverse(lst, 0)
