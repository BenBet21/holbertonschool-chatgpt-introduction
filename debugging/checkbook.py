#!/usr/bin/python3
class Checkbook:
    """
    Class representing a simple checkbook.

    Attributes:
        balance (float): Current balance in the checkbook.
    """

    def __init__(self):
        """
        Initializes the Checkbook object with a balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit money into the checkbook.

        Parameters:
            amount (float): The amount to be deposited.
        """
        try:
            amount = float(amount)
            self.balance += amount
            print("Deposited ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")

    def withdraw(self, amount):
        """
        Withdraw money from the checkbook.

        Parameters:
            amount (float): The amount to be withdrawn.
        """
        try:
            amount = float(amount)
            if amount > self.balance:
                print("Insufficient funds to complete the withdrawal.")
            else:
                self.balance -= amount
                print("Withdrew ${:.2f}".format(amount))
                print("Current Balance: ${:.2f}".format(self.balance))
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")

    def get_balance(self):
        """Prints the current balance in the checkbook."""
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Main function to interact with the Checkbook object.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            amount = input("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = input("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
