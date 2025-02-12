# python-exercise
Revising my python skills by taking some test, exercise and short project

# ListEx.py
This program allows you to manage a dictionary of countries and their populations. You can add, delete, update, query, and print the countries and their populations through a menu-driven interface.

* Dictionary Initialization:
* Function to Display Menu and Get User Choice:
* Main Operation Function:
    This function contains a while True loop that keeps running until the user chooses to exit. It performs different operations based on the user's choice:

    Add a Country:

    Prompts the user to enter a country name and population.
    Adds the country to the dictionary if it doesn't already exist.
    Delete a Country:

    Prompts the user to enter a country name.
    Deletes the country from the dictionary if it exists.
    Update a Country's Population:

    Prompts the user to enter a country name and new population.
    Updates the population if the country exists in the dictionary.
    Query a Country's Population:

    Prompts the user to enter a country name.
    Displays the population if the country exists in the dictionary.
    Print All Countries and Populations:

    Prints all countries and their populations in the dictionary.
    Exit:

    Breaks the loop and exits the function.

* Example Usage
When you run the program, it will display the menu and prompt you to enter your choice. Based on your input, it will perform the corresponding operation. For example:

Select from the following options:
1. add
2. delete
3. update
4. query
5. print
exit
Enter your choice: 1
Enter country name: france
Enter population: 67
Country added successfully

This will add France with a population of 67 to the dictionary.

Summary
The program uses a dictionary to store country names and their populations.
It provides a menu-driven interface to add, delete, update, query, and print the countries and their populations.
The while True loop keeps the program running until the user chooses to exit.