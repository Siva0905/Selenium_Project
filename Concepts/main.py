
#Constructor
class BankAccount:
    def __init__(self, account_holder, balance=0):
        # Constructor to initialize account holder and balance
        self.account_holder = account_holder
        self.balance = balance
        print(f"Account created for {self.account_holder} with balance ₹{self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.balance}")

    def display_balance(self):
        print(f"{self.account_holder}'s current balance: ₹{self.balance}")

# Creating an object of BankAccount
account1 = BankAccount("Siva Prakasam", 5000)

# Performing operations
account1.deposit(1500)
account1.withdraw(2000)
account1.display_balance()

#if-else
price = 120
if price > 100:
    print("Premium item")
else:
    print("Budget item")

#Loops
menu = ["Pizza", "Burger", "Juice"]
for item in menu:
    print("Menu item:", item)

i = 0
while i < len(menu):
    print("Item at position", i, "is", menu[i])
    i += 1

#Method
class BillCalculator:
    def calculate_total(self, price, quantity=1, discount=0):
        total = price * quantity
        if discount > 0:
            total -= total * (discount / 100)
        return total

calculator = BillCalculator()
print("Total without discount:", calculator.calculate_total(200, 2))
print("Total with discount:", calculator.calculate_total(200, 2, 10))


#Strings
item = "pizza"
print(item.upper())
print(item.replace("z", "s"))

#Type Casting
input_quantity = "3"
quantity = int(input_quantity)
print("Total quantity:", quantity)

#File Handling
# Writing order to a file
order_items = ["Pizza - ₹250", "Juice - ₹60", "Burger - ₹150"]
with open("order_summary.txt", "w") as file:
    file.write("Customer Order Summary\n")
    for item in order_items:
        file.write(item + "\n")

# Reading order from the file
with open("order_summary.txt", "r") as file:
    content = file.read()
    print("Order Details from File:")
    print(content)


