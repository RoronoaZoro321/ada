def subset(list,sum):
    if len(list) == 0:
        return sum == 0
    else:
        # if last element is greater than sum, then ignore it
        if list[-1] > sum:
            return subset(list[:-1], sum)
        new_list = list[:-1]
        return subset(new_list, sum) or subset(new_list, sum - list[-1])
    
str = input("")
sum = input("")
input_list = [int(x) for x in str.split(" ")]

print(subset(input_list, int(sum)))
