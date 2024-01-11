def payment():
  p_number = int(input("Enter Marchent Account no. : "))
  p_amount = int(input("Enter amount: "))
  pin = int(input("enter pin:"))
  if pin == info.get('pin'):
    current_balance = info.get("balance")
    info["balance"] = current_balance - p_amount
    print(f"Payment of BDT {p_amount} succesfull to {p_number}. your current balance is {info.get('balance')}.")
