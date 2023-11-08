import random

def main():
    sum = 0
    myList = []

    for i in range(1,10):
        randomNum=random.randint(0,100)
        myList.append(randomNum)
        sum+=randomNum

    print(f'sum: {sum}')

if __name__ == '__main__':
    main()
    