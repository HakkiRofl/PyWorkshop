money = int(input())
tax = 0
if money > 15527 and money < 42708:
  tax = 15
elif money > 42707 and money < 132407:
  tax = 25
elif money > 132406:
  tax = 28
print(f"The tax for {money} is {tax}%. That is {money*tax/100} dollars!")