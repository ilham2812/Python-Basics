# Leap Year Checker using user input and elif
while True:  # Allows repeated input
    year = int(input("Enter year: "))
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            print(f"{year} is not a leap year")
        else:
            print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
