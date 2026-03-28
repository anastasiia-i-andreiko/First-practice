while True:
    try:
        age = int(input("Enter a number: "))
        break
    except ValueError:
        print("Please enter a number")

dogs_years = age * 7
print(f"Your age in dog years is: {dogs_years}")