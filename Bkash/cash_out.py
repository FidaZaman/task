def cash_out():
  c_number = int(input("Enter agent Account no. : "))
  c_amount = int(input("Enter amount: "))
  fees = c_amount*.02
  pin = int(input("enter pin:"))
  if pin == info.get('pin'):
    current_balance = info.get("balance")
    info["balance"] = current_balance - c_amount - fees
    print(f"Cash out of BDT {c_amount} succesfull to {c_number}. fees {fees} your current balance is {info.get('balance')}.")
