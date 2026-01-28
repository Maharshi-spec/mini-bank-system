# 1. Read data from the file into lists
names = []
acc_nums = []
passwords = []
balances = []

try:
    fd = open("account_data.txt", "r")
    for line in fd:
        if line.strip():
            parts = line.strip().split(", ")
            names.append(parts[0])
            acc_nums.append(parts[1])
            passwords.append(parts[2])
            balances.append(float(parts[3]))
    fd.close()
except FileNotFoundError:
    print("Error: account_data.txt not found!")

# 2. Main Program Loop
while True:
    print("\n--- Mini Bank System ---")
    print("s: Search | d: Deposit | w: Withdraw | e: Exit")
    choice = input("Enter your choice: ").lower()

    if choice == 'e':
        fd = open("account_data.txt", "w")
        for i in range(len(names)):
            fd.write(f"{names[i]}, {acc_nums[i]}, {passwords[i]}, {balances[i]}\n")
        fd.close()
        print("Changes saved. Thankyou for using our service! Goodbye!")
        break

    elif choice == 's':
        first_name = input("Enter first name to search: ")
        found = False
        for i in range(len(names)):
            if names[i].split()[0].lower() == first_name.lower():
                print(f"Result -> Name: {names[i]}, Acc: {acc_nums[i]}, Balance: {balances[i]}")
                found = True
        if not found:
            print("No account found.")

    elif choice == 'd':
        acc = input("Enter account number: ")
        amount = float(input("Enter deposit amount: "))
        
        # Check if amount is positive
        if amount > 0:
            for i in range(len(acc_nums)):
                if acc_nums[i] == acc:
                    balances[i] += amount
                    print(f"Success! New balance: {balances[i]}")
        else:
            print("Invalid entry! Amount must be greater then zero.")

    elif choice == 'w':
        acc = input("Enter account number: ")
        pw = input("Enter password: ")
        for i in range(len(acc_nums)):
            if acc_nums[i] == acc:
                if passwords[i] == pw:
                    amount = float(input("Enter withdrawal amount: "))
                    
                    # Check if amount is positive
                    if amount > 0:
                        if amount <= balances[i]:
                            balances[i] -= amount
                            print(f"Success! Remaining balance: {balances[i]}")
                        else:
                            print("Insufficient funds!")
                    else:
                        print("Invalid entry! Amount must be positive.")
                else:
                    print("Incorrect password!")