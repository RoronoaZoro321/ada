
def two(given_sum, input_list):
    seen = []
    for i in input_list:
        if given_sum - i in seen:
            return "Yes"
        seen.append(i)
    return "No"

def main():
    sumu = input()
    stru = input()
    input_list = [int(x) for x in stru.split()]
    print(two(int(sumu),input_list))

main()
