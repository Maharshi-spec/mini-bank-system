import random

# -------------------- DATA STORAGE --------------------
names = []
acc_nums = []
passwords = []
balances = []

FILE_NAME = "account_data_2.txt"

# -------------------- SAVE FUNCTION --------------------
def save_data():
    with open(FILE_NAME, "w") as fd:
        for i in range(len(names)):
            fd.write(f"{names[i]}, {acc_nums[i]}, {passwords[i]}, {balances[i]}\n")

# -------------------- LOAD FUNCTION --------------------
def load_data():
    try:
        with open(FILE_NAME, "r") as fd:
            for line in fd:
                line = line.strip()
                if not line:
                    continue

                parts = [p.strip() for p in line.split(",")]
                if len(parts) != 4:
                    continue  # skip bad lines safely

                names.append(parts[0])
                acc_nums.append(parts[1])
                passwords.append(parts[2])

                try:
                    balances.append(float(parts[3]))
                except ValueError:
                    balances.append(0.0)
    except FileNotFoundError:
        print("No existing database found. Starting fresh.")

# -------------------- INIT LOAD --------------------
load_data()

# -------------------- MAIN LOOP --------------------
while True:
    print("\n--- Mini Bank System ---")
    print("c: Create | s: Search | d: Deposit | w: Withdraw | e: Exit")
    choice = input("Enter choice: ").lower()

    # -------------------- EXIT --------------------
    if choice == 'e':
        save_data()
        print("All data saved. Goodbye!")
        break

    # -------------------- CREATE --------------------
    elif choice == 'c':
        print("\n--- Create Account ---")
        new_name = input("Enter full name: ").strip()

        while True:
            new_acc = str(random.randint(1000000000, 9999999999))
            if new_acc not in acc_nums:
                break

        print(f"Your Account Number: {new_acc}")
        new_pw = input("Set password: ")

        names.append(new_name)
        acc_nums.append(new_acc)
        passwords.append(new_pw)
        balances.append(0.0)

        save_data()

        print("Account created successfully!")

    # -------------------- SEARCH --------------------
    elif choice == 's':
        search = input("Enter first name: ").strip().lower()
        found = False

        for i in range(len(names)):
            first = names[i].strip().split()[0].lower()
            if first == search:
                print(f"Name: {names[i]}, Acc: {acc_nums[i]}, Balance: {balances[i]}")
                found = True

        if not found:
            print("No account found.")

    # -------------------- DEPOSIT --------------------
    elif choice == 'd':
        acc = input("Enter account number: ").strip()
        try:
            amount = float(input("Enter deposit amount: "))
        except ValueError:
            print("Invalid amount.")
            continue

        if amount <= 0:
            print("Amount must be positive.")
            continue

        found = False
        for i in range(len(acc_nums)):
            if acc_nums[i] == acc:
                balances[i] += amount
                save_data()
                print(f"Deposit successful! New balance: {balances[i]}")
                found = True
                break

        if not found:
            print("Account number not found.")

    # -------------------- WITHDRAW --------------------
    elif choice == 'w':
        acc = input("Enter account number: ").strip()
        pw = input("Enter password: ").strip()
        found = False

        for i in range(len(acc_nums)):
            if acc_nums[i] == acc:
                found = True
                if passwords[i] != pw:
                    print("Incorrect password!")
                    break

                try:
                    amount = float(input("Enter withdrawal amount: "))
                except ValueError:
                    print("Invalid amount.")
                    break

                if amount <= 0:
                    print("Amount must be positive.")
                elif amount > balances[i]:
                    print("Insufficient funds!")
                else:
                    balances[i] -= amount
                    save_data()
                    print(f"Withdrawal successful! Balance left: {balances[i]}")
                break

        if not found:
            print("Account number not found.")

    else:
        print("Invalid choice!")
