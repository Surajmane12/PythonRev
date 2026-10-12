import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

logger=logging.getLogger(__name__)

class InsufficientBalanceError(Exception):
    """ Raise when the withdrawl exceeds the balance."""

class InvalidAmountError(Exception):
    """ Raise when the amount is invalid."""

class BankAccount:
    def __init__(self,owner:str,balance:float=0):
        if balance < 0:
            raise InvalidAmountError("Inital Amount cannot be negative!!")
        self.owner=owner
        self.balance=balance

    def withdraw(self,amt:float)->float:
        if amt<=0:
            raise InvalidAmountError("Amount must be greater than zero..")
        if amt>self.balance:
            raise InsufficientBalanceError("Insufficent Balance")
        self.balance-=amt
        return self.balance

def main():
    account=BankAccount("Surya",10000)

    try:
        amount=float(input("Enter a amount to withdraw: "))
        remain=account.withdraw(amount)
        
    except ValueError:
        logger.warning("User entered an invalid number.")
        print("Please enter a valid numeric amount.")

    except InvalidAmountError as exc:
        logger.warning("Invalid transaction: %s", exc)
        print(f"Transaction rejected: {exc}")

    except InsufficientBalanceError as exc:
        logger.warning("Withdrawal rejected: %s", exc)
        print(f"Transaction failed: {exc}")

    except Exception:
        logger.exception("Unexpected error occurred.")
        print("Something went wrong. Please try again later.")

    else:
        print(f"Withdrawal successful. Remaining balance: {remain:.2f}")

    finally:
        logger.info("Withdrawal attempt completed.")

if __name__=="__main__":
    main()