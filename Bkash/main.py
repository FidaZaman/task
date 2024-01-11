from send_money import send_money
from recharge import recharge
from payment import payment
from add_money import add_money
from cash_out import cash_out
from my_account import my_account

def main():
  dial = input("dial a number [*247#]")
  while dial== "*247#":
    print("1. Sennd money")
    print("2. Mobile recharge")
    print("3. payment")
    print("4. add money")
    print("5. Cash out ")
    print("6. my Bkash")
    print("7. quit")
    choice = int(input("enter a number: "))

    if choice == 1: send_money()
    elif choice == 2: recharge()
    elif choice == 3: payment()
    elif choice == 4: add_money()
    elif choice == 5: cash_out()
    elif choice == 6: my_account()
    elif choice == 7: break
    else: print("invalid number")

info = {"name": "Fida", "phone": 123, "pin": 123, "balance": 1000}
main()
