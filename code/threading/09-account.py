import concurrent.futures
import time

class Account:
    def __init__(self):
        self.balance = 100

    def update(self, transaction, amount):
        print(f"{transaction} thread updating...")
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
#       tf.map(account.update(),[i[0] for i in [('credit1',50),('debit2',-150),('credit3',150),('credit4',150),('debit5',-100),('debit6',-50)]], 
#         [int(i[1]) for i in [('credit1',50),('debit2',-150),('credit3',150),('credit4',150),('debit5',-100),('debit6',-50)]]
#         )
    print(f"balance after two transactions is {account.balance}")
    print("main ended")