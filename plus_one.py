# plus_one.py

# both solutions, recursive and not, have time/memory complexity of O(n)
def plusOne(digits: list[int]) -> list[int]:
    if not digits:
        return [1]
    else:
        if digits[-1] < 9:
            digits[-1] += 1
        else:
            tmp = int("".join(str(i) for i in digits))+1

            digits = [int(i) for i in str(tmp)]
        return digits

def plusOne_recursive(digits: list[int]) -> list[int]:
    if not digits:
        return [1]
    else:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            if len(digits) == 1:
                return [1,0]
            else: 
                return plusOne_recursive(digits[:-1]) + [0]

#digits = [1,2,3,4]
digits = []

print(plusOne_recursive(digits))
