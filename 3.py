e = '\u03b5'
p = []

class Prod:
    def __init__(self, name, products):
        self.name = name
        self.products = products
    def print(self):
        s = f'{self.name} -> '
        for prod in self.products:
            s += f'{prod} |'
        s = s.rstrip('|')
        print(s)

def trans():
    for x in p:
        alpha = []
        beta = []
        for products in x.products:
            if x.name == products[0]:
                alpha.append(products[1:])
            else:
                beta.append(products)
            
        if alpha:
            for i in range(len(beta)):
                beta[i] = f"{beta[i]}{x.name}'"
            for i in range(len(alpha)):
                alpha[i] = f"{alpha[i]}{x.name}"
            alpha.append(e)
            x.products = beta
            p.append(Prod(f"{x.name}'", alpha))

num = int(input("Enter number of productions : "))
for i in range(num):
    ip = input(f"Enter {i+1} production : ")
    name, prod = ip.split(' -> ') 
    productions = prod.split(' | ')
    p.append(Prod(name, productions))

print('Productions')
for x in p:
    x.print()

print('After Transformation') 
trans()

for x in p:
    x.print()