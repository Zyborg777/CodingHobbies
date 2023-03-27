from functools import reduce

VALUES_LIST = []
SEPARATOR_LINE = "_" * 72
MENU = ("➕  Addition", "➖  Subtraction", "✖️   Multiplication", "➗  Division", "➗  Integer division", "🔺  Power", "Ⓜ️   Modulo", "❌  Exit")
final_value = 0
stop = False
## the 'x_signs' lists from line 9 to line 15 are very useful from line 38 to 50 where I pass multiple elif conditions using any (which is gonna check multiple strings)
addition_signs = ['+', ' + ', '+ ', ' +']
subtraction_signs = ['-', ' - ','- ', ' -']
multiplication_signs = ['*', ' * ', '* ', ' *']
division_signs = ['/', ' / ', '/ ', ' /']
int_division_signs = ['//', ' // ', '// ', ' //']
power_signs = ['**', ' ** ', '** ', ' **']
modulo_signs = ['m', ' m ', 'm ', ' m']
print("\n🖖 WELCOME TO THE NOOB CALCULATOR! 📟 [release 1.1, codename 'Aquarius']\n")

while True:
    
    print(SEPARATOR_LINE)
    for i, option in enumerate(MENU, 1):
        print(f"{i}. {option}")
    print(SEPARATOR_LINE)
    choice = input(f"Choose an option in {range(1, len(MENU))}: ")

    if not (choice.isdigit() and int(choice) in range(1, len(MENU) + 1)):
        continue
    else:
        choice = int(choice)
        if choice == 8:
            print("Goodbye! 🖖")
            break
        
        while True:
            val = input(f"Insert your values: ")
            VALUES_LIST = val
            val = 0
            if any([x in VALUES_LIST for x in addition_signs]):
                VALUES_LIST = VALUES_LIST.split('+')
            elif any([x in VALUES_LIST for x in subtraction_signs]):
                VALUES_LIST = VALUES_LIST.split('-')
            elif any([x in VALUES_LIST for x in multiplication_signs]):
                VALUES_LIST = VALUES_LIST.split('*')
            elif any([x in VALUES_LIST for x in division_signs]):  
                VALUES_LIST = VALUES_LIST.split('/')
            elif any([x in VALUES_LIST for x in int_division_signs]):  
                VALUES_LIST = VALUES_LIST.split('//')
            elif any([x in VALUES_LIST for x in power_signs]):  
                VALUES_LIST = VALUES_LIST.split('*')
            elif any([x in VALUES_LIST for x in modulo_signs]):  
                VALUES_LIST = VALUES_LIST.split('m')  
            
            list(VALUES_LIST)
            break
        
        VALUES_LIST = [float(x) for x in VALUES_LIST]
        
        if 1 <= choice <= 7:
            print(SEPARATOR_LINE)
            match choice:
                case 1:
                    final_value = sum(VALUES_LIST)
                    print(f"The sum of {VALUES_LIST} is {final_value}")
                case 2:
                    final_value = reduce(lambda x, y: x - y, VALUES_LIST)
                    print(f"The subtraction of {VALUES_LIST} is {final_value}")
                case 3:
                    final_value = reduce(lambda x, y: x * y, VALUES_LIST)
                    print(f"The multiplication of {VALUES_LIST} is {final_value}")
                case 4:
                    final_value = reduce(lambda x, y: x / y, VALUES_LIST)
                    print(f"The division of {VALUES_LIST} is {final_value}")
                case 5:
                    final_value = reduce(lambda x, y: x // y, VALUES_LIST)
                    print(f"The integer division of {VALUES_LIST} is {int(final_value)}")
                case 6:
                    final_value = reduce(lambda x, y: x ** y, VALUES_LIST)
                    print(f"The power operation of {VALUES_LIST} is {final_value}")
                case 7:
                    final_value = reduce(lambda x, y: x % y, VALUES_LIST)
                    print(f"The modulo operation of {VALUES_LIST} is {final_value}")
