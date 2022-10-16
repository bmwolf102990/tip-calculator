# Tip Calculator App

## JTC Project 01

This tip calculator app was created as an assigned project for Columbia University's **Justice Through Code** coding intensive. It is written in Python.

The purpose of the app is, as its name implies, to work as a **functional tip calculator** for anyone who wants to use it. It is an interactive application that offers users **command line input prompts** for them to enter:

    - the total cost of their meal
    - how many people (if any) are going to be splitting the bill
    - what percent to tip

This module of code also comes with **built-in case tests** (located in the *test_tip_calculator.py* file) that can be used to verify that the app's output is working as expected. **The current set of tests have been run and verified for accuracy**.

### Version

1.0

### Cloning the Tip Calculator Repository

In order to clone this repo, all you need to do is run the line of code provided below in your computer's command line tool:

`git clone https://github.com/bmwolf102990/tip-calculator.git`

### Runnning the Tip Calculator

Once you have cloned this repo, you can run the program from your computer's command line tool by navigating into the repo directory and running the line of code provided below:

`py tip_calculator.py`

**NOTE**: *your computer may use a different command to run python code. If the above line of code doesn't run properly, try replacing the "py" at the start with either "python" or "python3"***as shown below**.

`python tip_calculator.py`

`python3 tip_calculator.py`

### Running Built-In Case Tests

In your command line tool, first make sure you are in the repo directory, then run the line of code provided below:

`py -m unittest`

**NOTE**: *as stated above, you may need to use "python" or "python3" in place of "py" to run the commmand on your computer*.

### Using the Tip Calculator

Now that you have the app running, using it is simple and straightforward.

1. The first thing that will appear in your command line tool is a prompt asking you what the total cost of your meal is. This prompt requires you to input the dollar and cents amount listed on your bill. **This prompt will only accept numeric inputs**.

2. The next prompt will ask you how many people are splitting the bill. **This prompt will only accept whole number inputs that are greater than zero**.

3. The third prompt will ask you how much you would like to tip. **This prompt will only accept whole number inputs that are greater than or equal to zero**

4. The final prompt that you will receive will ask you whether or not you would like to continue using the app to calculate another tip. Answering yes will restart the program from the beginning. Answering no will end the program.

**NOTE**: *If you enter an invalid input the app will give you an error message with guidance on what is considered a valid input response for the current prompt and then display that prompt again*.
