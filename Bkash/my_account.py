def my_account():
  pin = int(input("To see you account information please,\nenter pin:"))
  if (pin == info.get('pin')):
    print(f"Name : {info.get('name')}.")
    print(f"phone Number : {info.get('phone')}.")
    print(f"Your available balance is {info.get('balance')}.")
