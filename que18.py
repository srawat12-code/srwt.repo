def print_age_category():
    try:
        age = int(input("Enter age: "))
        if age < 13:
            print("Child")
        elif 13 <= age <= 19:
            print("Teenager")
        else:
            print("Adult")
    except ValueError:
        print("Invalid input. Please enter a valid age.")

print_age_category()