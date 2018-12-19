from SAIDValidator import isSAIdValid
import json
import string
if __name__ == '__main__':
    filename = input('Please enter a path to a input file: ')
    if not filename:
        filename='sample.json'

    # print(filename)
    idNumbers = json.loads(open(filename).read())
    # print(idNumbers)
    for id in idNumbers:
        idResult = isSAIdValid(id)
        print(idResult)
