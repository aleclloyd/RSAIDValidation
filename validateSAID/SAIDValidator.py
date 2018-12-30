import datetime

# pipenv run python RSAIDTool.py id validatebatch --path '/Users/aleclloyd/Documents/projects/python/RSAIDValidation/validateSAID/sample.json'
# pipenv run python RSAIDTool.py id validate --id 8004125094080

pivotyear = 10


def isSAIdValid(idNumber):
    if not idNumber or not isinstance(int(idNumber), int) or not len(idNumber) == 13:
        idobject = {"ID": idNumber, "Gender": "", "Valid": "false"}
        return idobject

    num1 = 0
    num2 = 0
    num3 = 0
    temp = ""
    tempnumber = 0
    i = 0

    while i <= 5:
        num1 += (int(idNumber[i * 2]))
        i += 1

    i = 0
    while i <= 5:
        temp = temp + (idNumber[i * 2 + 1])
        i += 1

    tempnumber = int(temp) * 2
    templen = len(str(tempnumber))
    for n in range(0, templen):
        num2 += int(str(tempnumber)[n])

    num3 = num1 + num2

    digit = 10 - (num3 % 10)
    if digit == 10:
        digit = 0

    if digit == int(idNumber[12]):
        genderCode = idNumber[6]

        if int(genderCode) in range(4):
            gender = 'F'
        else:
            gender = 'M'

        dob = getdob(idNumber)
        currentdate = datetime.datetime.today().strftime("%Y-%m-%d")

        age = days_between(dob, currentdate)

        idobject = {"ID": idNumber, "Gender": gender, "Valid": "true", "Age": str(age / 365)[:2]}
        return idobject

    idobject = {"ID": idNumber, "Gender": "", "Valid": "false"}
    return idobject


def days_between(d1, d2):
    d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
    return abs((d1 - d2).days)


def getdob(idNumber):
    if not idNumber or not isinstance(int(idNumber), int) or not len(idNumber) == 13:
        return "none"

    currentDate = datetime.datetime.today().strftime("%Y-%m-%d")
    currentyear = datetime.datetime.today().strftime("%Y")
    currentyearYY = currentyear[2:]
    currentcentury = currentyear[:2]
    dobString = idNumber[:6]
    idYearYY = idNumber[:2]
    if int(idYearYY) < int(currentyear[2:]) - pivotyear:
        dob = currentcentury + dobString
    else:
        dob = str(int(currentcentury) - 1) + dobString

    date = datetime.datetime.strptime(dob, '%Y%m%d').strftime('%Y-%m-%d')
    return date


def luhn(purported):
    LUHN_ODD_LOOKUP = (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)  # sum_of_digits (index * 2)

    if not isinstance(purported, str):
        purported = str(purported)
    try:
        evens = sum(int(p) for p in purported[-1::-2])
        odds = sum(LUHN_ODD_LOOKUP[int(p)] for p in purported[-2::-2])
        return (evens + odds) % 10 == 0
    except ValueError:  # Raised if an int conversion fails
        return False
