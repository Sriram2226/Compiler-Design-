print("Recursive Descent Parsing For following grammar\n")
print("E -> T E'\nE' -> + T E' / @\nT -> F T'\nT' -> * F T' / @\nF -> (E) / i\n")
print("Enter the string you want to be checked:\n")

# Global variables
s = list(input())
i = 0

def match(a):
    global s, i
    if i >= len(s):
        return False
    elif s[i] == a:
        i += 1
        return True
    else:
        return False

def F():
    if match('('):
        if E():
            return match(')')
        else:
            return False
    else:
        return match('i')

def Tx():
    if match('*'):
        if F():
            return Tx()
        else:
            return False
    else:
        return True  # epsilon transition

def T():
    if F():
        return Tx()
    else:
        return False

def Ex():
    if match('+'):
        if T():
            return Ex()
        else:
            return False
    else:
        return True  # epsilon transition

def E():
    if T():
        return Ex()
    else:
        return False

# Final check
if E() and i == len(s):
    print("String is accepted")
else:
    print("String is not accepted")
