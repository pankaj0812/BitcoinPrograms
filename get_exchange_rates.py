from blockchain import exchangerates

ticker = exchangerates.get_ticker()

print("Bitcoin prices in all currencies:")
for k in ticker:
	print(k, ticker[k].p15min)


btc = exchangerates.to_btc('EUR', 100)
print("\n 100 euros in Bitcoin: %s"%btc)