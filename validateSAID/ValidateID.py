from SAIDValidator import isSAIdValid

from validateSAID.SAIDValidator import getdob

if __name__ == '__main__':

    num = input('Enter an id number: ')

    # num='8004125094080'
    idResult = isSAIdValid(num)
    x = getdob()
    print(x)
    print(idResult)
