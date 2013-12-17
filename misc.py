
def main():
    num = int(input("enter a number"))
    f = factorial(num)
    print(num, "factorial is", f)

def factorial(num):
    if num == 1 or num == 0:
        return 1
    res = factorial(num-1) * num
    return res

main()