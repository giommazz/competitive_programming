# https://neetcode.io/problems/two-integer-sum


def twoSum(nums: list[int], target: int) -> list[int]:
    # sort `enumerate(nums)` based on its keys, but also keep sorted (original) indices
    # `key` in `sorted` takes a function as argument, which is why here we are using `lambda`
    sorted_numpairs = sorted(enumerate(nums), key = lambda x:x[1])
    
    # unzip the sorted indices anmd the sorted keys
    # `*` needed because there is mmore than one argument in `sorted_numpairs`
    sorted_indices, sorted_keys = zip(*sorted_numpairs)
    
    # browse `sorted_keys` with two indices, one at the start and one at the end
    i_start, i_end = 0, len(sorted_keys)-1
    while i_start < i_end:
        curr_target = sorted_keys[i_start] + sorted_keys[i_end]
        
        
        if curr_target == target:
            # retrieve original indices from `sorted_indices`, ordered (hence using `min` and `max`)
            return [
                min(sorted_indices[i_start], sorted_indices[i_end]), 
                max(sorted_indices[i_start], sorted_indices[i_end])
                ]
        if curr_target > target:
            i_end -= 1
        if curr_target < target:
            i_start += 1