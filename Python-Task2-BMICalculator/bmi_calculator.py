try:
    # Take input from the user
    weight = float(input("Enter your weight (in kg): "))
    height = float(input("Enter your height (in meters): "))

    # Validate input
    if weight <= 0 or height <= 0:
        print("Weight and height must be greater than zero.")
    else:
        # Calculate BMI
        bmi = weight / (height ** 2)

        # Display BMI rounded to 2 decimal places
        print(f"\nYour BMI is: {bmi:.2f}")

        # Determine BMI category
        if bmi < 18.5:
            print("Category: Underweight")
        elif bmi < 25:
            print("Category: Normal Weight")
        elif bmi < 30:
            print("Category: Overweight")
        else:
            print("Category: Obese")

except ValueError:
    print("Invalid input! Please enter numeric values.")