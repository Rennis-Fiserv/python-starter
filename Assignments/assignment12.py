def main():
    
    num = input("Enter integer: ")
    
    if num.find(".") != -1:
        print("Error! Please enter an integer.")
        return
    else:
        num = int(num)
        num = num * -1
    
        
    print(num)
        
if __name__ == '__main__':
    main()