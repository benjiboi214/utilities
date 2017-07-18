from sys import argv
import os
from secrets import SystemRandom

CWD = os.getcwd()
DICEWARE = 'eff_large_wordlist.txt'
DICEWARE_FP = os.path.join(CWD, DICEWARE)


def load_diceware_dict():
    '''Loads the diceware text file, converts to dict object.'''
    with open(DICEWARE_FP, 'rU') as diceware_file:
        dw_list = diceware_file.read().split('\n')
    dw_dict = {}
    for item in dw_list:
        if len(item) > 0:
            split = item.split('\t')
            dw_dict[split[0]] = split[1]
    return dw_dict


def roll_dice(times):
    '''Given an integer, roll a dice that many times, returning a concatenated
    string containing the result of those die rolls.'''
    rng = SystemRandom()
    string = ''
    for _ in range(times):
        string += str(rng.randint(1, 6))
    return string


def generate_password(dw_dict):
    '''Given a dictionary of words, where the keys are combinations of 5 die
    rolls, return a string containing three random words, a random number and
    a random symbol.'''
    rng = SystemRandom()
    symbols = ['~', '!', '@', '#', '$', '%', '^', '&',
               '*', '(', ')', '_', '+', '-', '=']
    rw1 = dw_dict[roll_dice(5)]
    rw2 = dw_dict[roll_dice(5)]
    rw3 = dw_dict[roll_dice(5)]
    rn1 = rng.randint(0, 100)
    rs1 = symbols[rng.randint(0, 14)]

    return '%s%s%s%s%s' % (rw1, rn1, rs1, rw2, rw3)


def main():
    '''Main function for executing program logic.'''
    dw_dict = load_diceware_dict()
    script, cycle = argv
    try:
        cycle = int(cycle)
    except ValueError:
        exit("Please use int for argv")

    for _ in range(cycle):
        print (generate_password(dw_dict))
    return


if __name__ == '__main__':
    main()
