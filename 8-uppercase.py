def uppercase(str):
    newstr = ''
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            newchar = chr(ord(char) - 32)
            newstr += newchar
        else:
            newstr += char
    print(newstr)