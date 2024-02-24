# Booth rental that give most profit in consicutive days
def booth(rent, profits_days):
    if len(profits_days) == 1:
        if profits_days[0] - rent > 0:
            return profits_days[0] - rent
        return "No"
    
    else:
        now = 0
        prev = 0
        highest = []
        for day in profits_days:
            prev = now
            profit = day - rent
            if  profit > 0:
                now += profit
            else:
                if now + profit < 0:
                    now = 0
                    highest.append(prev)
                    prev = 0
                elif now + profit > 0:
                    highest.append(prev)
                    now += profit
        if max(highest) > 0:
            return max(highest)
        return "No"
    
rent = int(input())
profit_days = list(map(int, input().split()))

print(booth(rent, profit_days))
