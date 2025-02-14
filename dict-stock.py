stock_list = {
    'info': [600,630,620], 
    'tcs': [2000, 2100, 2200], 
    'wipro': [250, 260, 270], 
    'hcl': [1000, 1100, 1200]
    }

def make_choice():
    print("Select any one from bewlo: ")
    print("1. Show")
    print("2. Add")
    print("3. Exit\n")
    return input("Enter your choice: ")

def operation():
    while True:
        choice = make_choice()
        if choice == "1":
            for key, value in stock_list.items():
                average = 0
                for i in value:
                    average += i
                print(key, "==>", value, "==>", average/len(value))
            print("\n\n")
        elif choice == "2":
            stock = input("Enter stock name: ")
            if stock in stock_list:
                value = int(input("Enter stock price: "))
                stock_list[stock].append(value)
                print("Stock value",stock, stock_list[stock] ,"added successfully\n\n")

            else:
                stock_list[stock] = [int(input("Enter stock price: "))]
                print("Stock",stock, stock_list[stock],"added successfully\n\n")
        elif choice == "3":
            break
        else:
            print("Invalid input, please select from show, add, exit\n")  
            break
    
operation()