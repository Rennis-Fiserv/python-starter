def main():
    myList = [6,2,7,3,77,7,1]
    minSum = myList[0]
    
    for num in myList:
        if num < minSum:
            minSum = num
            
    print(minSum)


if __name__ == '__main__':
    main()