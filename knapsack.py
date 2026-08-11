# 0/1 Knapsack Problem using Dynamic Programming

# Function for Bottom-Up approach
def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)              
    w=[2,5,6,7]  
    v=[10,20,30,40]  
    0 1 2 3
    1 2 3 4
    # Create DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            # If current item can fit
            if weights[i - 1] <= w:

                # Maximum of:
                # 1. Including the item
                # 2. Excluding the item
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )

            else:
                # Cannot include the item
                dp[i][w] = dp[i - 1][w]

    # Find selected items
    selected_items = []
    w = capacity

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i)
            w = w - weights[i - 1]

    selected_items.reverse()

    return dp[n][capacity], selected_items, dp


# Function for Top-Down approach
def knapsack_top_down(weights, values, capacity):
    n = len(weights)

    # Memoization table
    memo = [[-1 for _ in range(capacity + 1)] for _ in range(n + 1)]

    def solve(i, w):

        # Base condition
        if i == 0 or w == 0:
            return 0

        # Return already calculated value
        if memo[i][w] != -1:
            return memo[i][w]

        # If item weight is greater than current capacity
        if weights[i - 1] > w:
            memo[i][w] = solve(i - 1, w)

        else:
            # Maximum of including and excluding the item
            include = values[i - 1] + solve(
                i - 1,
                w - weights[i - 1]
            )

            exclude = solve(i - 1, w)

            memo[i][w] = max(include, exclude)

        return memo[i][w]

    maximum_value = solve(n, capacity)

    # Find selected items
    selected_items = []
    w = capacity

    for i in range(n, 0, -1):
        if solve(i, w) != solve(i - 1, w):
            selected_items.append(i)
            w = w - weights[i - 1]

    selected_items.reverse()

    return maximum_value, selected_items


# -------------------------------
# Main Program
# -------------------------------

weights = [2, 1, 3, 2]
values = [12, 10, 20, 15]
capacity = 5

print("0/1 KNAPSACK PROBLEM")
print("--------------------")

print("\nItems:")
for i in range(len(weights)):
    print(
        f"Item {i + 1}: Weight = {weights[i]}, "
        f"Value = {values[i]}"
    )

print("\nKnapsack Capacity:", capacity)

# Bottom-Up
value1, items1, dp_table = knapsack_bottom_up(
    weights, values, capacity
)

print("\n--- Bottom-Up Approach ---")
print("Maximum Value:", value1)
print("Selected Items:", items1)

# Top-Down
value2, items2 = knapsack_top_down(
    weights, values, capacity
)

print("\n--- Top-Down Approach ---")
print("Maximum Value:", value2)
print("Selected Items:", items2)