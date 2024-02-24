def recur(list):
    counting_result = []
    while len(list)!=0:
        count = 0
        prev = float('-inf')
        for i in list:
            if i > prev:
                count += 1
                prev = i
        counting_result.append(count)
        list.pop(0)
    return max(counting_result) 

def main():
    stru = input()
    input_list = [int(x) for x in stru.split()]
    print(recur(input_list))

main()
