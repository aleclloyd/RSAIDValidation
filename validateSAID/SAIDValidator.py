import datetime
# pipenv run python RSAIDTool.py id validatebatch --path '/Users/aleclloyd/Documents/projects/python/RSAIDValidation/validateSAID/sample.json'
# pipenv run python RSAIDTool.py id validate --id 8004125094080


def isSAIdValid(idNumber):
    if not idNumber or not isinstance(int(idNumber), int) or not len(idNumber) == 13:
        idObj = {"ID": idNumber, "Gender": "", "Valid": "false"}
        return idObj

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
    # print(templen)
    for n in range(0, templen):
        # print(num2)
        num2 += int(str(tempnumber)[n])

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

        dob = getdob(idNumber)
        # print(type(dob))
        currentDate = datetime.datetime.today().strftime("%Y-%m-%d")
        print(dob)

        age = days_between(dob,currentDate)

        # age = dat currentDate-dob
        print("Age: " + str(age/365)[:2])
        idObj = {"ID": idNumber, "Gender": gender, "Valid": "true","Age":str(age/365)[:2]}
        return idObj

    idObj = {"ID": idNumber, "Gender": "", "Valid": "false"}
    return idObj


def days_between(d1, d2):
    d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
    print("D1 {0}, D2 {1}".format(d1,d2))
    return abs((d1 - d2).days)


def calculateage(idNumber):
    if not idNumber or not isinstance(int(idNumber), int) or not len(idNumber) == 13:
        return "none"
    # datetime.datetime.today().strftime("%Y-%m-%d")
    currentyear = datetime.datetime.today().strftime("%Y")


def getdob(idNumber):
    if not idNumber or not isinstance(int(idNumber), int) or not len(idNumber) == 13:
        return "none"

    currentDate = datetime.datetime.today().strftime("%Y-%m-%d")
    # print(currentDate)
    currentyear = datetime.datetime.today().strftime("%Y")
    currentyearYY=currentyear[2:]
    currentcentury=currentyear[:2]
    # print(currentyear)
    dobString=idNumber[:6]
    idYearYY = idNumber[:2]
    # print("IDYearYYx" + idYearYY)
    # print("currentyearx" + str(int(currentyear[2:]) - 10))
    if int(idYearYY) < int(currentyear[2:]) - 10:
        # print("IDYearYY" + idYearYY)
        # print("currentyear" + currentyear)
        dob = currentcentury + dobString
    else:
        dob = str(int(currentcentury)-1) + dobString

    date = datetime.datetime.strptime(dob, '%Y%m%d').strftime('%Y-%m-%d')
    # print(dob)
    return date

    # int    currentYear = LocalDate.now().getYear();
    # String    currentYearString = Integer.toString(currentYear);
    # int    currentCentury = Integer.parseInt(currentYearString.substring(0, 2));
    # int    currentYearYY = Integer.parseInt(currentYearString.substring(2, 4));
    #
    # int    idYearYY = Integer.parseInt(identificationNumber.substring(0, 2));
    # LocalDate    dob;
    # String    dobString = identificationNumber.substring(0, 6);
    # DateTimeFormatter    dateFormat = DateTimeFormatter.ofPattern("yyyyMMdd");
    # if (idYearYY < (currentYearYY - 10)) {
    # // current century
    # dob = LocalDate.parse(currentCentury + dobString, dateFormat);
    # } else {// currentcentury-1
    # dob = LocalDate.parse(currentCentury - 1 + dobString, dateFormat);
    # }
    # System.out.println(dob.toString());
