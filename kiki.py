transactions = {
    "t1": {"user": "Alice", "amount": 120},
    "t2": {"user": "Bob", "amount": 75},
    "t3": {"user": "Alice", "amount": 200},
    "t4": {"user": "Charlie", "amount": 50},
    "t5": {"user": "Bob", "amount": 130},
}

mtlianobashi_daxarjuli = {}
for transaction_id, data in transactions.items():
    user = data["user"]
    amount = data["amount"]
    mtlianobashi_daxarjuli[user] = mtlianobashi_daxarjuli.get(user, 0) + amount


meti_150_ze = [user for user, total in mtlianobashi_daxarjuli.items() if total > 150]


meti_gadaxdili_tranzakciashi_vidre_100 = {}

for transaction_id, data in transactions.items():
    user = data["user"]
    amount = data["amount"]

    if amount > 100:
        if user not in meti_gadaxdili_tranzakciashi_vidre_100:
            meti_gadaxdili_tranzakciashi_vidre_100[user] = []

        meti_gadaxdili_tranzakciashi_vidre_100[user].append(transaction_id)

print(mtlianobashi_daxarjuli)
print(meti_150_ze)
print(meti_gadaxdili_tranzakciashi_vidre_100)