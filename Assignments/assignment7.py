import random

def main():
    randomNum=random.randint(1,100)
    
    
    
    while True:

        
        if randomNum < 10:
            print(f'{randomNum} You lose, you idiot!')
            break
        elif randomNum > 10 and randomNum < 50:
            print(f'{randomNum} Try again.')
            randomNum=random.randint(1,100)
        else:
            print(f'{randomNum} Good job!')
            break

if __name__ == '__main__':
    main()
    