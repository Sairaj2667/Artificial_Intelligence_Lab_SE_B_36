def minimax(node, depth, maximizingPlayer, values, index=0):
    if depth == 0 or index >= len(values):
        return values[index]

    if maximizingPlayer:
        best = float('-inf')
        for i in range(2): 
            val = minimax(node*2+i, depth-1, False, values, index*2+i)
            best = max(best, val)
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = minimax(node*2+i, depth-1, True, values, index*2+i)
            best = min(best, val)
        return best

values = [3, 5, 6, 9, 1, 2, 0, -1]  
depth = 3
result = minimax(0, depth, True, values)

print("Optimal value (using Minimax):", result)
