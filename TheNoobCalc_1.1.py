from functools import reduce

VALUES_LIST = []
SEPARATOR_LINE = "_" * 72
MENU = ("➕  Addition", "➖  Subtraction", "✖️   Multiplication", "➗  Division", "➗  Integer division", "🔺  Power", "Ⓜ️   Modulo", "❌  Exit")
final_value = 0
## the 'x_signs' sets from line 8 to line 14 are very useful from line 39 to 51 where I pass multiple elif conditions using any (which is gonna check multiple strings)
addition_signs = ('+', ' + ', '+ ', ' +')
subtraction_signs = ('-', ' - ','- ', ' -')
multiplication_signs = ('*', ' * ', '* ', ' *')
division_signs = ('/', ' / ', '/ ', ' /')
int_division_signs = ('//', ' // ', '// ', ' //')
power_signs = ('**', ' ** ', '** ', ' **')
modulo_signs = ('m', ' m ', 'm ', ' m')
print("\n🖖 WELCOME TO THE NOOB CALCULATOR! 📟 [release 1.1, codename 'Aquarius']\n")

while True:
    
    print(SEPARATOR_LINE)
    for i, option in enumerate(MENU, 1):
        print(f"{i}. {option}")
    print(SEPARATOR_LINE)
    option = input(f"Choose an option in {range(1, len(MENU))}: ")

    if not (option.isdigit() and int(option) in range(1, len(MENU) + 1)):
        print(f"ERROR: {option} IS AN INVALID OPTION, TRY AGAIN.")
        continue
    else:
        option = int(option)
        if option == 8:
            print("Goodbye! 🖖")
            break
        
        while True:
            val = input(f"Insert your values: ")
            VALUES_LIST = val
            val = 0
            ## These if conditions with 'any' search if there are matching signs from the earlier 'x_signs' sets in VALUES_LIST, and if yes then they split the elements in between the signs
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
            
            list(VALUES_LIST) # Then, once that's done I convert VALUES_LIST into a list
            break
        
        VALUES_LIST = [float(x) for x in VALUES_LIST] # Finally, I concatenate each element in VALUES_LIST to make them 'floats' with decimals
        
        if 1 <= option <= 7:
            print(SEPARATOR_LINE)
            # This match and case part of the code is to decide what to do with the list according to the option that the user chose (sum/sub/multi/divide/etc)
            match option:
                case 1:
                    final_value = sum(VALUES_LIST)
                    print(f"The sum of {VALUES_LIST} is {final_value}")
                case 2:
                    final_value = reduce(lambda x, y: x - y, VALUES_LIST) # Starting here I use the reduce function with lambda to tell instructions of what's going to happen with the values
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
