def main():
    
    while (True):
        first = input("Enter first integer: ")
        if first == "exit":
            break
        second = input("Enter second integer: ")
        if second == "exit":
            break
        ops = input ("Enter operation (add, sub, mul, div): ")
        if ops == "exit":
            break
        elif ops == "add":
            first = int(first)
            second = int(second)
            sum = first + second
        elif ops == "sub":
            first = int(first)
            second = int(second)
            sum = first - second
        elif ops == "mul":
            first = int(first)
            second = int(second)
            sum = first * second
        elif ops == "div":
            first = int(first)
            second = int(second)
            sum = first / second
        else:
            print("bad input smelly.")
        
        print(f'Answer: {sum}')
        
if __name__ == '__main__':
    main()