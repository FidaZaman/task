def recharge():
  print("1. Robi")
  print("2. Grameenphone")
  print("3. Banglalink")
  print("4. Teletalk")
  print("5. Airtel")
  choice = int(input("select a oparetor [1-5]: "))
  r_number = int(input("Enter Phone number: "))
  r_amount = int(input("Enter amount: "))
  pin = int(input("enter pin:"))
  if pin == info.get('pin'):
    current_balance = info.get("balance")
    info["balance"] = current_balance - r_amount
    print(
      f"Mobile recharge of BDT {r_amount} succesfull to {r_number}. your current balance is {info.get('balance')}.")
    info["balance"] = current_balance - r_amount
