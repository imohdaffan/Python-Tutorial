def divisible5(n):
    if(n%2 == 0):
        return True
    return False

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

f = list(filter(divisible5, a))
print(f)