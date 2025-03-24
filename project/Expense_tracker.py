Total_Amount = 0
Items = []
limit = ""

def Enter_Amount():
    global Total_Amount, limit  
    total = int(input("Enter Your Budget:\n"))
    Total_Amount += total
    limit1 = input("1. Monthly \n2. Weekly\n")
    limit = "Monthly" if limit1 == "1" else "Weekly"

def Add_item():
    global Total_Amount, limit  

    if Total_Amount <= 0:
        print(f"You have reached your {limit} limit of {Total_Amount}.")
        print("-----Items You Purchased-----")
        for item in Items:
            print(item)
    else:
        print(f"You have ${Total_Amount} remaining in your {limit} budget.")
        item = input("Enter the name of the item:\n")
        Items.append(item)
        price = int(input("Enter the price of the item:\n"))
        
        Total_Amount -= price  

        if Total_Amount < 0:
            print(f"Warning: You have exceeded your {limit} budget!")

def expense_item():
    global Total_Amount, limit

    while True:
        print("--------------")
        select = input("Choose:\n 1. Set Budget \n 2. Add Item \n 3. Exit\n")
        print("--------------")

        if select == "1":
            Enter_Amount()
        elif select == "2":
            Add_item()
        elif select == "3":
            print("\nExiting program. Your purchases:")
            for item in Items:
                print(item)
            print(f"Remaining budget: ${Total_Amount}")
            break
        else:
            print("Invalid Input! Choose 1, 2, or 3.")

expense_item()
