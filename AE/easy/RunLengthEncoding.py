def runLengthEncoding(string: str):
    index = 0
    count = 1
    output = ""
    while index < (len(string) - 1):
        if string[index] == string[index + 1] and count < 9:
            count += 1
        else:
            output += str(count) + string[index]
            count = 1
        index += 1

    # Handling last character for the final output
    if string[index] == string[index - 1] and count <= 9:
        output += str(count) + string[index]
    else:
        count = 1
        output += str(count) + string[index]
    return output


class RunLengthEncoding:
    string = input()
    print(runLengthEncoding(string))
