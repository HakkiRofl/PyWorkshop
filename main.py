mounths = ["Jan", "Feb", "Mar", "Apr", "May", "Jul", "Jun", "Aug", "Sep", "Oct", "Nov", "Dec"]
prices = [1000, 1400, 600, 700, 5000, 4500, 1200, 7000, 8000, 10000, 1000, 2500]
procent = "n/a "
profit = "n/a"
i = 0
for mon, price in zip(mounths, prices):
  i += 1
  if i < len(prices):
    print(f"{mon} {price} {procent}% {profit}")
    procent = round((prices[i] - price) / price * 100)
  if procent > 50:
    profit = "great"
  elif procent > 25 and procent <= 50:
    profit = "decent"
  elif procent >= 0 and procent <= 25:
    profit = "need follow up"
  elif procent < 0:
    profit = "critical"