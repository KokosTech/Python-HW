''' 
1. Напишете програма, която намира всички числа между 2000 и 5000, където ВСЯКА ЦИФРА от числото е четно число. Получените цифри ги принтирайте на екрана на 1 ред разделени с запетаи.
2. Напишете програма, която при зададен списък намира разликата между най-малкото и най-голямото число.
3. Напишете програма, която при зададен от input string преброява буквите и цифрите
'''
def num_chk(num):
    for dgt in num:
        if int(dgt) % 2 != 0:
            return False
    return True

def nums():
    print("EX 1.0\n\n")

    vnum = []

    for num in range(2000, 5001):
        if num_chk(str(num)):
            vnum.append(num)
            
    print(f"The Valid Numbers are:\n\n{', '.join(map(str, vnum))}")
    
def mm():
    print("\nEX 2.0\n")

    nice = [1, 2 ,84, 8, 9, 48, 9, 0, 993, 584, 654, 645, 435, 519]
    print("Min - Max is: ", min(nice) - max(nice))

def ln():
    print("\n\nEX 3.0\n\n")

    alph = 0
    intgr = 0

    inpt = input("Please enter a string: ");

    for x in range(len(inpt)):
        if inpt[x].isalpha():
            alph += 1
        if inpt[x].isnumeric():
            intgr += 1

    print(f"There are {alph} alphabetic symbols and {intgr} numeric symbols.")


nums()
mm()
ln()
