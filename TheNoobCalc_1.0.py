from functools import reduce

VALUES_LIST = []
final_value: 0

MENU = [
    "Addition                                                        [+] |",
    "Subtraction                                                     [-] |",
    "Multiplication                                                  [*] |",
    "Division                                                        [/] |",
    "Integer division                                               [//] |",
    "Power                                                          [**] |",
    "Modulo                                                        [mod] |",
    "Percentages                                                     [%] |",
    "Quit program                                                    [x] |",
]
print(f"\n🖖 WELCOME TO THE NOOB CALCULATOR! 📟 [release 1.0, codename 'Aquarius']\n")

while True:
    
    print("_" * 72)
    for i, option in enumerate(MENU, 1):
        print(f"|{i}. {option}")
    print("_" * 72)
    choice = input(f"Choose an option in {range(1, len(MENU))}: ")

    if not (choice.isdigit() and int(choice) in range(1, len(MENU) + 1)):
        continue
    else:
        choice = int(choice)
        if choice == 9:
            print("Goodbye! 🖖")
            break
        
        how_many_values = int(input("Choose how many values you want to use: "))
        for i in range(how_many_values):
            val = float(input(f"Insert your value n°{i+1}: "))
            VALUES_LIST.append(val)
        
        VALUES_LIST = [float(x) for x in VALUES_LIST]
        
        if 1 <= choice <= 8:
            print("_" * 72)
            match choice:
                case 1:
                    final_value = sum(VALUES_LIST)
                    print(f"The sum of {VALUES_LIST} is {final_value}")
                case 2:
                    final_value = reduce(lambda x, y: x - y, VALUES_LIST)
                    print(f"The substraction of {VALUES_LIST} is {final_value}")
                case 3:
                    final_value = reduce(lambda x, y: x * y, VALUES_LIST)
                    print(f"The multiplication of {VALUES_LIST} is {final_value}")
                case 4:
                    final_value = reduce(lambda x, y: x / y, VALUES_LIST)
                    print(f"The division of {VALUES_LIST} is {final_value}")
                case 5:
                    final_value = reduce(lambda x, y: x // y, VALUES_LIST)
                    print(f"The integer division of {VALUES_LIST} is {final_value}")
                case 6:
                    final_value = reduce(lambda x, y: x ** y, VALUES_LIST)
                    print(f"The power operation of {VALUES_LIST} is {final_value}")
                case 7:
                    final_value = reduce(lambda x, y: x % y, VALUES_LIST)
                    print(f"The modulo operation of {VALUES_LIST} is {final_value}")
                case 8:
                    final_value = reduce(lambda x, y: float(y) / 100 * float(x), VALUES_LIST)
                    print(f"The percentage operation of {VALUES_LIST} is {final_value}")
