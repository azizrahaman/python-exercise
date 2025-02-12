# expense = [2200, 2350, 2600, 2130, 2190]

# compare = expense[1] - expense[0]
# print("In February, I spent an extra amount of", compare, "over January")
# compare = expense[0] + expense[1] + expense[2]
# print("Total expense in first quarter is", compare)
# if 2000 in expense:
#     print("Expense of 2000 is recordeed")

# expense.append(1980)
# print("Expense of 1980 is added")
# expense.insert(3, 2330)
# print("Expense of Arpil is updated to: ", expense[3])

# heros=['spider man','thor','hulk','iron man','captain america']
# print("Length of list: ", len(heros))
# heros.append('black panther')
# print(heros)
# heros.remove('black panther')
# print(heros)
# heros.insert(3, 'black panther')
# print(heros)
# heros[1:3] = ['doctor strange']
# print(heros)
# heros.sort()
# print(heros)

countries = {'china': 143, 'india': 136, 'usa': 32, 'pakistan': 21}

def make_choice():
    print("Select from the following options:")
    print("1. add")
    print("2. delete")
    print("3. update")
    print("4. query")
    print("5. print")
    print("exit")
    return input("Enter your choice: ")

def operation():
    choice = make_choice()
    if choice == "1":
        country = input("Enter country name: ")
        if country in countries:
            print("Country already exists")
            # operation()
        else:
            population = int(input("Enter population:"))
            countries[country] = population
            print("Country added successfully")
            # operation()
    elif choice == "2":
        country = input("Enter country name: ")
        if country in countries:
            del countries[country]
            print("Country deleted successfully")
            # operation()
        else:
            print("Country does not exist")
            # operation()
    elif choice == "3":
        country = input("Enter country name: ")
        if country in countries:
            population = int(input("Enter population: "))
            countries[country] = population
            print("Country updated successfully")
            # operation()
        else:
            print("Country does not exist")
            # operation()
    elif choice == "4":
        country = input("Enter country name: ")
        if country in countries:
            print("population of",country,"is",countries[country])
            # operation()
        else:
            print("Country does not exist")
            # operation()
    elif choice == "5":
        for key, value in countries.items():
            print(key,"==>",value)
        # operation()
    elif choice == "exit":
        return
    else:
        print("Invalid input, plase select from add, delete, update, query, print")
        operation()
    operation()

operation()

# if user_input == "add":
#     country = input("Enter country name: ")
#     if country in countries:
#         print("Country already exists")
#         pass
#     else:
#         population = int(input("Enter population:"))
#         countries[country] = population
#         print("Country added successfully")
# elif user_input == "delete":
#     country = input("Enter country name: ")
#     if country in countries:
#         del countries[country]
#         print("Country deleted successfully")
#     else:
#         print("Country does not exist")
# elif user_input == "update":
#     country = input("Enter country name: ")
#     if country in countries:
#         population = int(input("Enter population: "))
#         countries[country] = population
#         print("Country updated successfully")
#     else:
#         print("Country does not exist")
# elif user_input == "query":
#     country = input("Enter country name: ")
#     if country in countries:
#         print("population of",country,"is",countries[country])
#     else:
#         print("Country does not exist")
# elif user_input == "print":
#     for key, value in countries.items():
#         print(key,"==>",value)
# else:
#     print("Invalid input, plase select from add, delete, update, query, print")
