def caesarCipherEncryptor(string: str, key: int):
    key = key % 26
    output = ""
    for character in string:
        ascii_value = ord(character)
        ascii_value += key
        extra = 0
        if ascii_value > 122:
            extra = ascii_value - 122
            ascii_value = 96 + extra
        output += chr(ascii_value)
    return output


class CaesarCypherEncryptor:
    string = input()
    key = int(input())
    print(caesarCipherEncryptor(string, key))
