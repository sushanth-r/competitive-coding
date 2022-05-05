def phoneNumberMnemonics(phone_number):
    phone_number_map = dict()
    phone_number_map["0"] = ["0"]
    phone_number_map["1"] = ["1"]
    phone_number_map["2"] = ["a", "b", "c"]
    phone_number_map["3"] = ["d", "e", "f"]
    phone_number_map["4"] = ["g", "h", "i"]
    phone_number_map["5"] = ["j", "k", "l"]
    phone_number_map["6"] = ["m", "n", "o"]
    phone_number_map["7"] = ["p", "q", "r", "s"]
    phone_number_map["8"] = ["t", "u", "v"]
    phone_number_map["9"] = ["w", "x", "y", "z"]
    result = []

    def mnemonics_helper(index, combination):
        if len(combination) == len(phone_number):
            result.append(combination)
            return
        values = phone_number_map[phone_number[index]]
        for value in values:
            mnemonics_helper(index + 1, combination + value)

    mnemonics_helper(0, "")
    return result


class PhoneNumberMnemonics:
    phone_number = str(input())
    print(phoneNumberMnemonics(phone_number))
