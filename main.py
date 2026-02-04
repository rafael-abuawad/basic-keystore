import getpass
import json

from eth_account import Account


def main():
    print("/*´:°•.°+.*•´.*:˚.°*.˚•´.°:°•.°•.*•´.*:˚.°*.˚•´.°:°•.°+.*•´.*:*/")
    print("/*                      KEYSTORE MANAGER                      */")
    print("/*.•°:°.´+˚.*°.˚:*.´•*.+°.•°:´*.´•*.•°.•°:°.´:•˚°.*°.˚:*.´+°.•*/")

    private_key = getpass.getpass("\n Enter your private key: ")

    password = getpass.getpass("\n Enter a password: ")
    password_confirm = getpass.getpass("Confirm your password: ")

    if password != password_confirm:
        print("\n ---ERROR \nPasswords do not match")
        return

    loaded_account = Account.from_key(private_key)
    json_key_store = loaded_account.encrypt(password=password)

    with open("account.keystore.json", "w") as fp:
        json.dump(json_key_store, fp)
        print("\n Keystore created successfully")
        return


if __name__ == "__main__":
    main()
