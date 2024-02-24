def max_earning(n, jobs):
    # Sort jobs based on finish times
    jobs.sort(key=lambda x: x[1])

    # Initialize dp array to store maximum earnings at each time
    dp = [0] * (25)

    for i in range(1, n+1):
        start_time, finish_time, earning = jobs[i-1]

        # Find the maximum earning at the current finish time
        dp[finish_time] = max(dp[finish_time], dp[start_time] + earning)

        # Update dp array for the next time slots
        for j in range(finish_time+1, 25):
            dp[j] = max(dp[j], dp[finish_time])

    return max(dp)

# Read input
n = int(input())
jobs = [list(map(int, input().split())) for _ in range(n)]

# Calculate and print the result
result = max_earning(n, jobs)
print(result)


# Suppose on one day, there is a collection of available jobs that Mary can take. 
# Each job i is specified by its start time si, its finish time fi, and the earning ei, 
# where si and fi are positive integers and 0 <= si < fi <= 24, and ei is a positive integer. 
# Mary may not take two jobs with conflicting times, i.e. the start time of one job is between 
# the start time and finish time of the other job.
# # Given the collection of jobs, find out the maximum total earning Mary can possibly get from 
# taking some of the given jobs.

#  Input Specification
# The first line of input contains the number n of jobs, which can be assumed to be a 
# non-negative integer in the range 0...1000. 
# Each of the next n lines contains the start time, the finish time, and the earning of each job, 
# separated by blank space. The start time and finish time can be assumed to be integers in the 
# range 0...24. The earning can be assumed to be a positive integer in the range 1...1000.

# 	 Output Specification
# The maximum total earning possible

#  Sample Input
# 3
# 1 3 20
# 2 5 20
# 4 6 30

# 	 Sample Output
# 50

# Sample Input
# 3
# 1 3 10
# 2 5 20
# 2 6 30

# 	 Sample Output
# 30