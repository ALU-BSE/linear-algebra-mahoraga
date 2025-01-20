import pandas as pd



Prices = [[300, 500],
          [1000, 120.85]]

Array2 = [200, 100]


print(Prices[0][0])
print(Prices[0][1])
print(Prices[1][0])
print(Prices[1][1])  

# Initialize an empty list to store the results
Ans = []

# Calculate the sum of products for each row
# (200 * 300 + 100 * 500) as an example calculation
for i in range(len(Prices)):
    row_sum = 0
    for j in range(len(Prices[0])):
        index_prod = Prices[i][j] * Array2[j]  # Multiply corresponding elements
        row_sum += index_prod  # Add to the row sum
    Ans.append(row_sum)  # Append the row sum to the results list

# Print the resulting sums
print(Ans)
