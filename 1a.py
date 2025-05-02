import re

patterns = {
    'IMPORTS' : r'<stdio.h>|<conio.h>|<stdlib.h>',
    'STRINGS' : r'\".*\"',
    'KEYWORDS' : r'#include|for|if|else|while|break|char|string',
    'FUNCTIONS' : r'printf|scanf|getch|clrscr',
    'INT' : r'\d+',
    'FLOAT' : r'\d+\.\d+',
    'OPERATOR' : r'\+?\+|\-|\*|/|=|==|<|>',
    'ID' : r'[a-zA-Z_][a-zA-Z0-9_]*',
    'LPARAN' : r'\(',
    'RPARAN' : r'\)',
    'SEPARATORS' : r'[:;,]',
    'LBRACE' : r'\{',
    'RBRACE' : r'\}'
}

def lex_anz(input):
    tokens = []
    regex_patt = '|'.join(f'(?P<{tok}>{patterns[tok]})' for tok in patterns)
    for match in re.finditer(regex_patt, input):
        tok_type = match.lastgroup
        tok_val = match.group()
        tokens.append((tok_type, tok_val))
    return tokens

with open('text.cpp', 'r') as file:
    code = file.read()

result = lex_anz(code)

for t, v in result:
    print(f'{v} -> {t}')