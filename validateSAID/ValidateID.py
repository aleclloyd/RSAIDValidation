from SAIDValidator import isSAIdValid
if __name__ == '__main__':

    num = input('Enter an id number: ')

    # num=8004125094080
    idResult = isSAIdValid(num)
    print(idResult)
    # for id in idResult:
        # print released.get("iphone 3G", "none")
    # valid= idResult.get("Valid",'false')
    # if valid=='true':
    #     print ("Valid ID number: {0}".format(num))
    # else:
    #     print("Invalid ID number: {0}".format(num))

    # if valid:
    #     print ("Valid ID number: {0}".format(num))
    # else:
    #     print("Invalid ID number: {0}".format(num))
