def c(l,p):
    cost = 0
    if len(p) <= 0:
        return cost
    else:
        cost = l
        return cost + min(c(p[-1],p[:-1]),c(l-p[0],p[1:]))


def main():
    sumu = input()
    stru = input()
    input_list = [int(x) for x in stru.split()]
    print(c(int(sumu),input_list))

main()
