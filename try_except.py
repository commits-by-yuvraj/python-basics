try:
    # answer = 10/0
    number = float(input("Enter a number: "))
    print(number)

except ZeroDivisionError as err:
    print(err)
    
except ValueError:
    print("Invalid Input!")


# These are called except blocks. They tell Python what to do if a specific type of error (exception) occurs.