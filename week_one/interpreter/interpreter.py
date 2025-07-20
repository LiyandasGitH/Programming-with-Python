while True:
    try:
        # Ask for input
        expression = input("Expression (x y z): ").strip()

        # Make a quit option
        if expression.lower() in ["quit", "q", "exit"]:
             print("Goodbye!")
             break

        # x , y , z
        # Make y the operator
        x_str, sign, z_str = expression.split()
        # Make x & z int/floats
        x = float(x_str)
        z = float(z_str)

        if sign == "+":
            result = x + z
        elif sign == "*":
            result = x * z
        elif sign == "-":
            result = x - z
        elif sign == "/":
            if z == 0:
                 print("Cannot divide by zer.")
                 continue
            result = x / z
        else:
            print("Invalid. Please use: +, -, * or /.")
            continue
        # Make answer always be equal to one decimal
        print(f"{result:1f}")

    except ValueError:
            print("Invalid input. Please use format x y z(i.e., 3 + 4)")





'''
        # Make an exit option
        if expression == "q" or expression == "quit":
         print("Goodbye!")
        if expression == "exit":
         print("Goodbye!")
         break
'''

'''
            match operator:
                        case "+":
                            result = x + z
                        case "-":
                            result = x - z
                        case "*":
                            result = x * z
                        case "/":
                            result = x / z
                        case _:
                            print("Unsupported operator.")
                            continue

                print(f"{result:.f}")

                    except ValueError:
        print("Invalid input. Enter in format: x y z")

'''
