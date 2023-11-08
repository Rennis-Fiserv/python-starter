def main():
    myList = [1,2,3]
    mySet = {3,4,5}
    
    mySet.update(myList)
    
    print(mySet)

if __name__ == '__main__':
    main()