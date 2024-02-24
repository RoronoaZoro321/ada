def recur(list, num_pick):
    if len(list) == 0:
        return "Yes"
    else:
        if num_pick == -100000:
            return recur(list[1:], list[0]) or recur(list[:-1], list[-1])
        else:
            if abs(num_pick - list[-1]) <= 9 and abs(num_pick - list[-1]) <= 9:
                return recur(list[1:], list[0]) or recur(list[:-1], list[-1])
            elif abs(num_pick - list[0]) <= 9:
                return recur(list[1:], list[0])
            elif abs(num_pick - list[-1]) <= 9:
                return recur(list[:-1], list[-1])
            else:
                return

def main():
    stru = input()
    input_list = [int(x) for x in stru.split()]
    result = recur(input_list,-100000)
    if result == "Yes":
        print(result)
    else:
        print("No")
        

main()
