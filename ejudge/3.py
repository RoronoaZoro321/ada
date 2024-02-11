# cutting edge

def c(l,p):
    cost = 0
    if len(p) <= 0:
        return cost
    else:
        cost = l
        return cost + min(c(p[-1],p[:-1]),c(l-p[0],p[1:]))

l = input("")
str = input("")
input_list = [int(x) for x in str.split(" ")]

print(c(l,input_list))