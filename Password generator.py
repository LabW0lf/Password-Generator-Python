
import time
import random
import string

# generates password

# difficulties:
# 1 = numbers
# 2 = numbers and letters
# 3 = numbers, letters and characters
# 4 = numbers, mixed-case letters and characters

def choose_difficulty():
    while True:
        try:
            print("Choose the password difficulty. (1-4)")
            difficulty = int(input("Password Difficulty: "))
            print()
            print("Choose the pasword length")
            length = int(input("Password Length: "))

            
        except:
            print()
            time.sleep(0.5)
            print("Both inputs must be numbers")
            print()
        else:
            if difficulty not in range(1,5):
                print()
                time.sleep(0.5)
                print("invalid difficulty!")
                print()
            else:
                break
    
    return difficulty,length


# Index 0 = difficulty
# Index 1 = length
password_data = list(choose_difficulty())

# all Password characters:
alphabet_lower = string.ascii_lowercase   # lowercase alphabet   # a
alphabet_upper = string.ascii_uppercase   # uppercase alphabet   # b
numbers = "1234567890"                    # numbers              # c
characters = "!§$%&/()#=?+*~-_.:,;'"      # characters           # d



def one(numbers,length):
    a = 0
    result = []
    while a < length:
        result.append(numbers[random.randint(0,9)])
        a += 1
    return "".join(result)


def two(numbers,lowercase_letters,length):
    a = 0
    result = []
    while a < length:
        result.append(numbers[random.randint(0,9)])
        a += 1

    
    
    b = 0
    while b < length:
        result.insert(random.randint(0,len(result)),lowercase_letters[random.randint(0,25)])
        b += 1
    return "".join(result[0:length])


def three(numbers,lowercase_letters,characters,length):
    a = 0
    result = []
    while a < length:
        result.append(numbers[random.randint(0,9)])
        a += 1

    
    
    b = 0
    while b < length:
        result.insert(random.randint(0,len(result)),lowercase_letters[random.randint(0,25)])
        b += 1


    c = 0
    while c < length:
        result.insert(random.randint(0,len(result)),characters[random.randint(0,20)])
        c += 1
    


    return "".join(result[0:length])


def four(numbers,lowercase_letters,uppercase_letters,characters,length):
    a = 0
    result = []
    while a < length:
        result.append(numbers[random.randint(0,9)])
        a += 1
    
    b = 0
    while b < length:
        result.insert(random.randint(0,len(result)),lowercase_letters[random.randint(0,25)])
        b += 1

    c = 0
    while c < length:
        result.insert(random.randint(0,len(result)),characters[random.randint(0,20)])
        c += 1
    
    d = 0
    while d < length:
        
        result.insert(random.randint(0,len(result)),uppercase_letters[random.randint(0,25)])
        d += 1
    
    
    return "".join(result[0:length])



# output
if password_data[0] == 1:
    print("generating password...")
    print(one(numbers,password_data[1]))
elif password_data[0] == 2:
    print("generating password...")
    print(two(numbers,alphabet_lower,password_data[1]))
elif password_data[0] == 3:
    print("generating password...")
    print(three(numbers,alphabet_lower,characters,password_data[1]))
elif password_data[0] == 4: 
    print("generating password...")
    print(four(numbers,alphabet_lower,alphabet_upper,characters,password_data[1]))
