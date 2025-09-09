# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 08:21:17 2025

@author: cirze
"""
#Matrix rotation
def matrixRotation(matrix, r):
    m, n = len(matrix), len(matrix[0])
    layers = []
    
    # Extract layers
    for layer in range(min(m, n) // 2):
        elements = []
        
        # top row
        for j in range(layer, n - layer):
            elements.append(matrix[layer][j])
        # right column
        for i in range(layer + 1, m - layer - 1):
            elements.append(matrix[i][n - layer - 1])
        # bottom row
        for j in range(n - layer - 1, layer - 1, -1):
            elements.append(matrix[m - layer - 1][j])
        # left column
        for i in range(m - layer - 2, layer, -1):
            elements.append(matrix[i][layer])
        
        layers.append(elements)
    
    # Rotate each layer
    for idx, elements in enumerate(layers):
        k = r % len(elements)
        rotated = elements[k:] + elements[:k]
        pos = 0
        
        # put back rotated values
        # top row
        for j in range(idx, n - idx):
            matrix[idx][j] = rotated[pos]; pos += 1
        # right column
        for i in range(idx + 1, m - idx - 1):
            matrix[i][n - idx - 1] = rotated[pos]; pos += 1
        # bottom row
        for j in range(n - idx - 1, idx - 1, -1):
            matrix[m - idx - 1][j] = rotated[pos]; pos += 1
        # left column
        for i in range(m - idx - 2, idx, -1):
            matrix[i][idx] = rotated[pos]; pos += 1
    
    # Print result
    for row in matrix:
        print(" ".join(map(str, row)))


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    m = int(first_multiple_input[0])
    n = int(first_multiple_input[1])
    r = int(first_multiple_input[2])

    matrix = []
    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
