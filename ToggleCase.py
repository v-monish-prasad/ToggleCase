def toggleCase(string):
    stringList = list(string)

    for i in range(len(string)):
        if stringList[i].isalpha():
            stringList[i] = chr(ord(stringList[i]) ^ 1 << 5)

    return "".join(stringList)


if __name__ == "__main__":
    A = input()

    print(toggleCase(A))
