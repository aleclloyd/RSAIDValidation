from SAIDValidator import isSAIdValid

if __name__ == '__main__':

    num = input('Enter an id number: ')

    # num='8004125094080'
    idResult = isSAIdValid(num)
    print(idResult)
