def knapsack_dp(values, weights, max_weight):
    n = len(values)
    # Create a 2D array to store the max value at each n and w
    dp = [[0 for j in range(max_weight + 1)] for i in range(n + 1)]
    # Build the dp table in bottom up manner
    for i in range(1, n + 1):
        for j in range(1, max_weight + 1):
            if weights[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
    return dp, dp[n][max_weight]

# Values and weights as per the given items, and the max weight of the knapsack
values = [4, 2, 2, 1, 10]
weights = [12, 2, 1, 1, 4]
max_weight = 15

# Calculate the maximum value that fits in the knapsack
dp_table, max_value = knapsack_dp(values, weights, max_weight)

# Output the selected items
print("Các món đồ được chọn:")
for i in range(len(values), 0, -1):
    if max_value <= 0:
        break
    # If the value comes from the item being included, we print it
    if dp_table[i][max_weight] != dp_table[i - 1][max_weight]:
        print(f"Item {i} (value={values[i - 1]}, weight={weights[i - 1]})")
        max_value -= values[i - 1]
        max_weight -= weights[i - 1]

# Output the total value of selected items
# We should use the already computed maximum value instead of recalculating it
print("Tổng giá trị của các món đồ được chọn là:", dp_table[len(values)][15])  # Use original max_weight
