from blockchain import statistics

stats = statistics.get()

print("Bitcoin Trade Volume: %s\n" % stats.trade_volume_btc)

print("Bitcoin mined: %s\n" % stats.btc_mined)

print("Bitcoin market price in USD: %s" %stats.market_price_usd)