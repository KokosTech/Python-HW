def ex1():
    print("Ex. 1")
    num = int(input("Enter num: "))
    count = int(input("Enter count: "))
    dev = []

    for x in range(1, count + 1):
        dev.append(x * num)

    print(f"The multiples of the number {num} are: {', '.join(map(str, dev))}")

def ex2():
    print("Ex. 2")

    count = 0
    string = input("Type a string: ")

    for chr in string:
        if chr in "AEIOUaeiouАЪОУЕИаъоуеи":
            count += 1

    print(f'The string "{string}" has {count} vowels.')

def ex3():
    print("Ex. 3")

    list = ["my", 1, "turtle", "explain", 3.14]

    for itm in list:
        if isinstance(itm, int) or isinstance(itm, float):
            list.remove(itm)

    print(list)

def ex4():
    print("Ex. 4")

def bonus():
    print("Ex. Bonus")
    string = input("Type a string: ")
    string = string.split()

    for comp in string:
        for chr in comp:
            if chr in "AEIOUaeiouАЪОУЕИаъоуеи":
                string.replace(comp, comp.replace(chr, "*"))
                break

    print(" ".join(string))



bonus()