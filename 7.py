gram = {
    "S": ["S+S", "S*S", "S-S", "(S)", "id"]
}
start = "S"
inp = "(id+id)$"
stack = "$"

print(f'{"Stack": <15}' + "|" + f'{"Input Buffer": <15}' + "|" + 'Parsing Action')
print(f'{"-":-<50}')

while True:
    reduced = False
    # Try to reduce
    for prod in gram[start]:
        if prod in stack:
            stack = stack.replace(prod, start)
            print(f'{stack: <15}' + "|" + f'{inp: <15}' + "|" + f'Reduce > {prod}')
            reduced = True
            break  # Only one reduction at a time

    if not reduced:
        # Shift if no reduction happened
        if len(inp) > 1:
            stack += inp[0]
            inp = inp[1:]
            print(f'{stack: <15}' + "|" + f'{inp: <15}' + "|" + 'Shift')
        else:
            # End of input
            if stack == ("$" + start) and inp == '$':
                print(f'{stack: <15}' + "|" + f'{inp: <15}' + "|" + 'Accepted')
            else:
                print(f'{stack: <15}' + "|" + f'{inp: <15}' + "|" + 'Rejected')
            break
