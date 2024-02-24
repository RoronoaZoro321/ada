def maximum_jobs(n, jobs):
    # Sort jobs based on finish times
    jobs.sort(key=lambda x: x[1])

    # Initialize variables
    max_jobs = 0
    last_finish_time = 0

    # Iterate through the sorted jobs
    for job in jobs:
        start_time, finish_time = job

        # If the current job doesn't conflict with the last selected job, take it
        if start_time >= last_finish_time:
            max_jobs += 1
            last_finish_time = finish_time

    return max_jobs

# Read input
n = int(input())
jobs = [list(map(int, input().split())) for _ in range(n)]

# Calculate and print the result
result = maximum_jobs(n, jobs)
print(result)


# Suppose on one day, there is a collection of available jobs that Mary can take. 
# Each job i is specified by its start time si and finish time fi, where si and fi are positive integers 
# and 0 <= si < fi <= 24. Mary may not take two jobs with conflicting times, i.e. the start time of one job 
# is between the start time and finish time of the other job.
# Given the collection of jobs, find out what is the maximum number of jobs that Mary could possibly take on that day.

#  Input Specification
# The first line of input contains the number n of jobs, which can be assumed to be a non-negative integer in the range 0...107. 

# Each of the next n lines contains the start time and the finish time of each job, separated by blank space. 
# The start time and finish time can be assumed to be integers in the range 0...24. 

# Output Specification
# The maximum number of jobs that Mary can possibly take.


#  Sample Input
# 8
# 0 6
# 1 4
# 3 5
# 3 8
# 4 7
# 5 9
# 6 10
# 8 11
#  Sample Output
# 3