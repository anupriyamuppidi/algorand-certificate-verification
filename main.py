from algosdk import account, mnemonic

def create_account():
    private_key, address = account.generate_account()
    print("Address:", address)
    print("Private Key:", private_key)

if __name__ == "__main__":
    create_account()
