from bitcoin import *

private_key1 = random_key()
private_key2 = random_key()
private_key3 = random_key()


public_key1 = privtopub(private_key1)
public_key2 = privtopub(private_key2)
public_key3 = privtopub(private_key3)


my_multi_sig = mk_multisig_script(public_key1, public_key2, public_key3, 2, 3)
my_multi_address = scriptaddr(my_multi_sig)
print(my_multi_address)