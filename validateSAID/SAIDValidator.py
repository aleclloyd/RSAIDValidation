def isSAIdValid(idNumber):

    if not idNumber or not isinstance(int(idNumber),int) or not len(idNumber) == 13:
        idObj = {"ID": idNumber, "Gender": "", "Valid": "false"}
        return idObj

    num1 = 0
    num2 = 0
    num3 = 0
    temp = ""
    tempNumber = 0
    i = 0

    while i <= 5:
        num1 += (int(idNumber[i * 2]))
        i += 1

    i = 0
    while i <= 5:
        temp = temp + (idNumber[i * 2 + 1])
        i += 1

    tempNumber = int(temp) * 2
    templen = len(str(tempNumber))
    # print(templen)
    for n in range(0, templen):
        # print(num2)
        num2 += int(str(tempNumber)[n])

    num3 = num1 + num2

    digit = 10 - (num3 % 10)
    # print(digit)
    if digit == 10:
        digit = 0

    if digit == int(idNumber[12]):
        genderCode = idNumber[6]

        if int(genderCode) in range(4):
            gender = 'f'
        else:
            gender = 'm'

        idObj = {"ID": idNumber, "Gender": gender, "Valid": "true"}
        return idObj

    idObj = {"ID": idNumber, "Gender": "", "Valid": "false"}
    return idObj
