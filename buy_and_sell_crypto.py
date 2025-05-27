# https://neetcode.io/problems/buy-and-sell-crypto

# check if first index is lower than second index
feasible_indices = lambda i, j: True if i < j else False


# time complexity O(nlogn) because it requires sorting
def maxProfit_sorting(prices: list[int]) -> int:
    
    # set indices to first and last element of prices
    i, j = 0, len(prices)-1

    # sort prices and keep original indices too 
    sorted_indices, sorted_prices = zip(*sorted(enumerate(prices), key=lambda x: x[1]))

    while i < j:
        
        if not feasible_indices(sorted_indices[i], sorted_indices[j]):
            
            # check feasible combinations by increasing `i` or decreasing `j`
            feas_left = feasible_indices(sorted_indices[i+1], sorted_indices[j])
            feas_right = feasible_indices(sorted_indices[i], sorted_indices[j-1])

            # if both combinations are feasible: return max profit
            if feas_left and feas_right:
                return max(
                    sorted_prices[j] - sorted_prices[i+1],
                    sorted_prices[j-1] - sorted_prices[i],
                        )
            # return profit of the only feasible combination
            elif feas_left and not feas_right:
                return sorted_prices[j] - sorted_prices[i+1]
            elif not feas_left and feas_right:
                return sorted_prices[j-1] - sorted_prices[i]
            # increase `i` and decrease `j`
            else:
                i += 1
                j -= 1
        # if current combination is feasible, return profit
        else:
            return sorted_prices[j] - sorted_prices[i]
    # if you exit the loop without a feasible combination, return 0 (no trade)
    return 0

# more elegant solution with two pointers from the website
# time complexity O(n)
def maxProfit_twoPointer(prices: list[int]) -> int:
    left, right = 0, 1
    profit = 0
    while right < len(prices):
        current_net = prices[right] - prices[left]
        if current_net > 0:
            profit = max(current_net, profit)
        else:
            left += 1
        right += 1
    return profit            

import random
prices = [random.randint(1, 15) for _ in range(7)]
print(prices)
print(maxProfit_sorting(prices))
print(maxProfit_twoPointer(prices))
    
