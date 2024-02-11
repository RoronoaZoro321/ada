
def two(given_sum, input_list):
    input_list.sort()
    l = 0
    r = len(input_list) - 1
    while l < r:
        current_sum = input_list[l] + input_list[r]
        if current_sum == given_sum:
            return "Yes"
        elif current_sum < given_sum:
            l += 1
        else:
            r -= 1
    return "No"

sum = input("")
str = input("")
input_list = [int(x) for x in str.split(" ")]

print(two(int(sum),input_list))
