# rotate_matix_list.py

from typing import List


def rotate(matrix: List[List[int]]) -> None:
    """
    Rotate square matrix 90 degrees clockwise in place.

    Input:
    - `matrix`: list of equal-length int lists mutated in place.

    Output:
    - `List[List[int]]`: rotated matrix reference (same object mutated in place).

    Time complexity: O(n^2) because loops traverse upper triangle once.
    Space complexity: O(1) because swaps reuse existing cells.
    """
    n = len(matrix)
    matrix.reverse() # Flip row order before transpose
    # Transpose matrix: use XOR operator to swap upper triangle
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j] = matrix[i][j]^matrix[j][i]
            matrix[j][i] = matrix[i][j]^matrix[j][i]
            matrix[i][j] = matrix[i][j]^matrix[j][i]

matrix=[[1,2],[3,4]]
print(matrix)
assert rotate(matrix) == [[3,1],[4,1]]
