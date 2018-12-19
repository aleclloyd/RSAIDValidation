def isSAIdValid(idNumber):
    try:
        id = int(idNumber)
    except:
        idObj = {"ID": idNumber, "Gender": "", "Valid": "false"}
        return idObj

    if not id or not isinstance(id, int) or not len(str(id)) == 13:
        idObj = {"ID": id, "Gender": "", "Valid": "false"}
        return idObj

    num1 = 0
    num2 = 0
    num3 = 0
    temp = ""
    tempNumber = 0
    i = 0

    while i <= 5:
        num1 += (int(str(id)[i * 2]))
        i += 1

    i = 0
    while i <= 5:
        temp = temp + (str(id)[i * 2 + 1])
        i += 1

    tempNumber = int(temp) * 2
    templen = len(str(tempNumber))
    for n in range(0, templen):
        num2 += int(str(tempNumber)[n])

    num3 = num1 + num2

    digit = 10 - (num3 % 10)
    # print(digit)
    if digit == 10:
        digit = 0

    if digit == int(str(id)[12]):
        genderCode = str(id)[6]
        # print (genderCode)
        if int(genderCode) in range(4):
            gender = 'f'
        else:
            gender = 'm'

        idObj = {"ID": id, "Gender": gender, "Valid": "true"}
        return idObj

    idObj = {"ID": id, "Gender": "", "Valid": "false"}
    return idObj
