operators = ['%','+', '-', '/', '*', '=', '<', '<=', '>=', '>', '==']
separators = ['[', ']', '{', '}', '(', ')', ';', ' ']
reservedWords = ['char', 'int', 'boolean', 'real', 'input', 'print', 'if', 'else', 'break', 'for', 'while']

everything = operators + separators + reservedWords
codification = dict([(everything[i], i + 2) for i in range(len(everything))])
codification['identifier'] = 1
codification['constant'] = 0


