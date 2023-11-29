
# Factors to make the calculator efficient
def converter(value, from_factor, to_factor):
    return value * from_factor / to_factor


# The 'main' calculates the factors to covert length/ weight into their respective unit
def main():
    # Dictionary of units
    length_factors = {'mm': 0.001,
                      'cm': 0.01,
                      'm': 1.0,
                      'km': 1000.0}

    weight_factors = {'mg': 0.001,
                      'g': 1.0,
                      'kg': 1000.0,
                      't': 1000000.0}

    time_factors = {'second': 1.0,
                    'minute': 60.0,
                    'hour': 3600.0,
                    'day': 86400.0,
                    'year': 31536000.0}

    categories = {'length': length_factors, 'weight': weight_factors, 'time': time_factors}

    print("Welcome to the Ultimate Conversion Calculator!")

    # Checks what the user has picked for conversion or to end the program

    while True:
        category = input("Choose a category (length/weight/time) or 'exit' to end: ").lower()

        if category == "exit":
            print("Exiting the program. Goodbye!")
            break

        if category not in categories:
            print("Invalid category. Please choose either 'length', 'weight', 'time', or 'exit'.")
            continue

        # Checks the number and unit to convert to and from

        value = float(input(f"Enter the {category} value: "))
        from_unit = input(f"Enter the current {category} unit: ").lower()
        to_unit = input(f"Enter the target {category} unit: ").lower()

        try:
            result = converter(value, categories[category][from_unit], categories[category][to_unit])
            print(f"{value} {from_unit} is equal to {result} {to_unit}")
        except KeyError:
            print("Invalid units provided. Please provide valid units.")


# Ends the program and restarts if wanted
if __name__ == "__main__":
    main()
