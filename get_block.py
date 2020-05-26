from blockchain import blockexplorer

block = blockexplorer.get_block("0000000000000000001142eb9a7ec815500505555699aa93610a47d88ef1247d")

print(block.fee)
print(block.size)
print(block.transactions)


