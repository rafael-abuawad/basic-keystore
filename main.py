import getpass
import json

from eth_account import Account


def main():
    print("/*´:°•.°+.*•´.*:˚.°*.˚•´.°:°•.°•.*•´.*:˚.°*.˚•´.°:°•.°+.*•´.*:*/")
    print("/*                      KEYSTORE MANAGER                      */")
    print("/*.•°:°.´+˚.*°.˚:*.´•*.+°.•°:´*.´•*.•°.•°:°.´:•˚°.*°.˚:*.´+°.•*/")

    private_key = getpass.getpass("\n Ingrese su llave privada: ")

    password = getpass.getpass("\n Ingrese una contraseña: ")
    password_confirm = getpass.getpass("Confirme su contraseña: ")

    if password != password_confirm:
        print("\n ---ERROR \nLas contraseñas no son iguales")
        return

    loaded_account = Account.from_key(private_key)
    json_key_store = loaded_account.encrypt(password=password)

    with open("account.keystore.jsoe", "w") as fp:
        json.dump(json_key_store, fp)
        print("\n Keystore creada exitosamente")
        return


if __name__ == "__main__":
    main()
