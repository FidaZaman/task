def send_money():
  s_number = int(input("Enter Phone number: "))
  s_amount = int(input("ammount: "))
  pin = int(input("enter pin:"))
  if pin == info.get('pin'):
    fees = 5
    current_balance = info.get("balance")
    info["balance"] = current_balance - s_amount - fees
    print(
      f"Send money of BDT {s_amount} succesfull to {s_number}. fees {fees}. your current balance is: {info.get('balance')}."
    )
