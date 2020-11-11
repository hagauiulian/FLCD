from model.FiniteAutomata import FiniteAutomata

if __name__ == '__main__':

    finiteAutomata = FiniteAutomata.fromFile('fa1.txt')
    print(finiteAutomata)
    print("Is deterministic:")
    print(finiteAutomata.checkDeterministic())
