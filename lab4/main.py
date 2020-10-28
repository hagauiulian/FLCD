from model.pif import ProgramInternalForm
from model.st import SymbolTable
from model.spec_language import *
from model.scanner import *

if __name__ == '__main__':
    fileName = input("Insert file name: ")

    file = open(fileName, 'r', errors='ignore', encoding="utf8")
    for line in file:
        print(line)

    with open(fileName, 'r', encoding="utf8") as file:
        for line in file:
            print([token for token in tokenGenerator(line, separators)])

    symbolTable = SymbolTable()
    pif = ProgramInternalForm()

    with open(fileName, 'r', encoding="utf8") as file:
        lineNo = 0
        for line in file:
            lineNo += 1
            for token in tokenGenerator(line[0:-1], separators):
                if token == ' ':
                    continue
                if token in separators + operators + reservedWords:
                    pif.add(token, -1)
                elif isIdentifier(token):
                    id = symbolTable.add(token)
                    pif.add(codification['identifier'], id)
                elif isConstant(token):
                    id = symbolTable.add(token)
                    pif.add(codification['constant'], id)
                else:
                    raise Exception('Unknown token ' + token + ' at line ' + str(lineNo))

    print('Program Internal Form: \n', pif)
    print('Symbol Table: \n', symbolTable)


