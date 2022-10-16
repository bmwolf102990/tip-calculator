'''
The tip_calculator function will offer a series of inputs to a user and utilize the given responses received from the user to produce a calculation of the total bill (with tip), as well as a calculation of what each person who is splitting the bill should pay (if necessary).
'''

def tip_calculator():
    # The food_cost_input function offers an input for a user to enter the total cost of their meal.
    def food_cost_input():
        # "food_cost" is the variable name that we have attached to our input. To the right of the equal sign is our actual input() and the string of text inside the parentheses is what will be displayed to the user.
        food_cost = input("\nWhat was the total cost of your meal?: $")
        # This try/except block of code (lines 12-20) will test the response given by the user to verify that it is valid. In this case we want the response to be a float that is not less than  0.01. 
        try:
            # If the user's response is either not a float, or if it is a float that is less than 0.01, an error will be triggered ("raised") that provides an error message with corrective instructions to the user.
            if float(food_cost) < 0.01:
                raise ValueError
            # If the user's response is valid, the response is returned by the food_cost_input function so that it can be used elsewhere in the tip_calculator function (see line 52).
            else:
                return float(food_cost)
        # The "except" portion of our try/except block is where we tell our program how to handle a given error/exception. NOTE: We raised a "ValueError" on line 15 and here we give instructions on how to handle that error.
        except ValueError:
            # This is the actual error message that will be displayed to the user.
            print("\nYou did not enter a valid number. Please try again...\n","NOTE: The tip calculator will not work if you enter a total cost that is less than $0.01")
            # We return the food_cost_input function here in order to create a loop that will offer the user another chance to enter a valid response. This loop will be triggered indefinitely until the user enters a valid response.
            return food_cost_input()
    # The bill_split_input function follows the same pattern as the food_cost_input function (line 8). Please refer back to comments in that function for more details.
    def bill_split_input():
        bill_split = input("\nHow many people are splitting the bill?: ")
        try:
            # For this function, we want the user's entered response to be an integer that is not less than 1.
            if int(bill_split) < 1: 
                raise ValueError
            else:
                # The user's response is returned and used elsewhere in the tip_calculator function (see line 53).
                return int(bill_split)
        except ValueError:
            print("\nYou did not enter a valid number. Please try again...\n","NOTE: If you are not splitting the bill with anyone else, then please enter the number 1.")
            return bill_split_input()
    # The tip_percentage_input function follows the same pattern as the food_cost_input function (line 8). Please refer back to comments in that function for more details.
    def tip_percentage_input():
        tip_percentage = input("\nWhat percent would you like to tip?: ")
        try:
            # For this function, we want the user's entered response to be a integer that is not less than 0.
            if int(tip_percentage) < 0:
                # The user's response is returned and used elsewhere in the tip_calculator function (see line 54).
                raise ValueError
            else:
                return int(tip_percentage)
        except ValueError:
            print("\nYou did not enter a valid number. Please try again...\n","NOTE: The tip calculator will not work if you enter a negative number.")
            return tip_percentage_input()
    # We create three different variables for our three input functions from above. Assigning our three input functions to these variables calls (runs) those functions when the tip_calculator program starts running. When these variables are used later in the program their values will be equal to the returned user responses from each of their associated ("assigned") functions.
    food_total = food_cost_input()
    number_of_splits = bill_split_input()
    tip = tip_percentage_input()
    # This is an assumed 10% sales tax that will be added into the final calculations. We write it in decimal form for convenience later on.
    sales_tax = 0.1
    # Here we calculate the cost for each person splitting the bill (before tax).
    individual_cost = food_total / number_of_splits
    # Here we calculate the tax for each person's portion of the bill by taking the value of individual cost (line 58) and multiplying it by the assumed 10% sales tax (line 56)
    individual_tax = individual_cost * sales_tax
    # Here we calculate the tip for each person by multiplying individual cost (line 58) by tip (line 54). NOTE: The user enters a tip percentage as an integer (whole number) so in order to convert it into a proper decimal form we must divide it by 100 (as seen on line 62)
    individual_tip = individual_cost * (tip / 100)
    # Here we calculate the total bill for each person by adding individual cost (line 58) and indivdual tax (line 60) together.
    individual_total = individual_cost + individual_tax
    # Here we calculate the total payment of each person by adding individual total (line 64) and individual tip (line 62) together.
    individual_payment = individual_total + individual_tip
    # Here we calculate the overall total of the bill by multiplying each person's individual payment (line 66) by the total number of people splitting the bill (line 53)
    total_bill = individual_payment * number_of_splits
    # If the bill is being paid in-full by only one person, our program only needs to output the calculation for the individual payment as the total bill payment
    if number_of_splits == 1:
        # This is our output print statement for the total bill of one person. It uses an f-string in order to utilize the calculated value of the variable "individual_payment". the variable value itself is formatted using the .format() method and the formatting specifiers "," and ".2f" to display commas and display two decimal spaces respectively. 
        print(f"\nTotal bill: ${'{:,.2f}'.format(round(individual_payment, 2))}")
    else:
        # This output print statement follows the same pattern as the previous one (line 72). See the comment on line 71 for more details.
        print(f"\nTotal bill: ${'{:,.2f}'.format(round(total_bill, 2))}\nEach person should pay ${'{:,.2f}'.format(round(individual_payment, 2))}")
# The calculate_another_tip_input function asks the user whether they would like to calculate another tip.
def calculate_another_tip_input():
    calculate_another_tip = input("\nWould you like to calculate another tip (y/n)?: ")
    try:
        # If the user enters an "n" for no, the program will terminate.
        if calculate_another_tip == "n":
            print("\nAlrighty, see you next time!")
        # If the user enters a "y" for yes, the tip_claculator function is called which will start the whole tip calculation process over again.
        elif calculate_another_tip == "y":
            tip_calculator()
            # The calculate_another_tip_input function is called so that after the next tip calculation is complete the user will be asked again whether they would like to calculate another tip. This creates a loop that can only be terminated by the user responding with no to the input prompt.
            calculate_another_tip_input()
        # If the user enters anything other than an "n" for no or "y" for yes, an exception/error will be triggered.
        else:
            raise Exception
    except Exception:
        print("\nYou entered an invalid response. Please respond with 'y' for yes or 'n' for no...\n")
        return calculate_another_tip_input()
# These function calls below are the inital calls that start the whole program.
tip_calculator()
calculate_another_tip_input()
