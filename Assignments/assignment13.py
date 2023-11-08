def main():
    
    while (True):
        first = input("Enter first integer: ")
        if first == "exit":
            break
        second = input("Enter second integer: ")
        if second == "exit":
            break
        else:
            first = int(first)
            second = int(second)
            sum = first + second
        
        print(f'Answer: {sum}.')
        
if __name__ == '__main__':
    main()