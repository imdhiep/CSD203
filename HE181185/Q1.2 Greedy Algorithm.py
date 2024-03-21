def knapsack_greedy(values, weights, max_weight):
    n = len(values)
    # Pair up the values and weights and sort by value-to-weight ratio in descending order
    items = sorted(zip(values, weights), key=lambda x: x[0]/x[1], reverse=True)
    total_value = 0
    for v, w in items:
        if max_weight >= w:
            max_weight -= w
            total_value += v
        else:
            # Take a fraction of the item
            total_value += max_weight * (v / w)
            break  # Since we cannot take any more weight, we break the loop
    return total_value

# Define the values, weights, and the maximum weight of the knapsack
values = [4, 2, 2, 1, 10]
weights = [12, 2, 1, 1, 4]
max_weight = 15

# Calculate the maximum value we can get using the greedy approach
max_value = knapsack_greedy(values, weights, max_weight)

print("Tổng giá trị tối đa có thể lấy được là:", max_value)