# Create a new Bitcoin wallet
private_key = 
bitcoin.random_key()
public_key = 
bitcoin.privtopub(private_key)address =
bitcoin.pubtoaddr(public_key)
print("Private Key:", private_key)
print("Public Key:", public_key)
print("Address:", address)
