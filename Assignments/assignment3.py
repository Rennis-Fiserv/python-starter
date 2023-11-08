def main():

    myList = []
    input2 = input("Enter list of numbers: ")

    for word in input2:
        word = input2.split(",")
    for x in word:
        myList.append(x)
    length2 = len(myList)
    if(myList[0]==myList[length2-1]):
        print("True")
    else:
        print("False")


if __name__ == '__main__':
    main()