import concurrent.futures
import time
import threading

class Account:
    def __init__(self):
        self.balance = 100
        self.lock = threading.Lock()

    def update(self, transaction, amount):
        print(f"{transaction} thread updating...")
        with self.lock:
            local_copy = self.balance
            local_copy += amount
            time.sleep(5)
            self.balance = local_copy
        print(f"{transaction} thread finishing..")

if __name__ == '__main__':
    print("main started")
    account = Account()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as tf:
        for transaction, amount in [('credit1',50),('debit2',-150),('credit3',150),('credit4',150),('debit5',-100),('debit6',-50)]:
            tf.submit(account.update(transaction,amount))
    print(f"balance after two transactions is {account.balance}")
    print("main ended")