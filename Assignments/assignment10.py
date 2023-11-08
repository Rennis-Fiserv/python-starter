import re

def main():
    
    word = input("Enter a string: ")
    
    vowelCount = len(re.findall(r'[aeiou]', word.lower()))
    
    consonantCount = len(re.findall(r'[bcdfghjklmnpqrustvwxyz]', word.lower()))
            
    print(f'Vowels: {vowelCount}')
    print(f'Consonants: {consonantCount}')
        
if __name__ == '__main__':
    main()

