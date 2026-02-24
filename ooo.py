balance = 1000.0
while True:
    print("1 თანხის გამოტანა")
    print("2 თანხის შეტანა")
    print("3 ბალანსის ნახვა")
    print("4 გასვლა")


    operation = int(input("შეიყვანეთ ერთ-ერთი ციფრი >>:"))

    if operation == 1:
        gamotana = float(input("გამოსატანი თანხის რაოდენობა >>:"))
        if gamotana > balance:
            print("ბალანსზე არ არის საჭირო თანხა!")
        elif gamotana < balance:
            balance -= gamotana
            print(f"თქვენ გამოიტანეთ {gamotana} ლარი! ბალანსი შეადგენს {balance}")

    if operation == 2:
        shetana = float(input("შესატანი თანხის რაოდენობა >>:"))
        balance += shetana
        print(f"თქვენ შეიტანეთ {shetana} ლარი! ბალანსი შეადგენს {balance}")

    if operation == 3:
        print(f"თქვენი ბალანსი შეადგენს {balance}")

    if operation == 4:
        print("თქვენ გამოდიხართ პროგრამიდან")
        break

    else:
        print("შეყვანილი პროგრამა არასწორია!")

