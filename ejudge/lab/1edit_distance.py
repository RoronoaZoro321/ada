def fn(u, v):
    m, n = len(u), len(v)

    # Create a matrix to store the edit distances
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the matrix with base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill the matrix using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If characters are equal, no operation is needed
            if u[i - 1] == v[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Minimum of insert, delete, or replace operations
                dp[i][j] = 1 + min(dp[i - 1][j],      # Delete
                                   dp[i][j - 1],      # Insert
                                   dp[i - 1][j - 1])  # Replace

    # The bottom-right cell contains the edit distance
    return dp[m][n]

input_1 = str(input(""))
input_2 = str(input(""))
input_3 = str(input(""))

print(fn(input_1, input_2))

#  Input Specification
# The input consists of three lines.
# The first line contains the string u.
# The second line contains the string v.
# The last line contains a single characterr $ to mark the end of the input.
# The strings u and v can be assumed to be made up of English capital letters (A-Z) only. 
# The length of each string, u and v, can be assumed to be in the range 0...1000. 


# 	 Output Specification
# The output is the edit distance of the given strings u and v.


# Sample Input	 
# BOAT
# BOOT
# $
# Sample Output
# 1

# BOAT
# BAT
# $
# 1

# BOAT
# BLOAT
# $
# 1

# BOAT
# BATH
# $
# 2

# BOAT
# BARN
# $
# 3
