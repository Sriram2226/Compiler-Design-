e = '\u03b5'
p = []

class Prod : 
    def __init__(self, name, products):
        self.name = name
        self.products = products
    def print(self):
        s = f'{self.name} -> '
        for products in self.products : 
            s += f'{products} |'
        s = s.rstrip(' | ')
        print(s)

def trans():
    a = p[0]
    temp = a.products
    temp.sort()
    a.products = []

    while temp:
        group = []
        alpha = ''
        beta  = []

        for i in range(1, len(temp)):
            if temp[0][0] == temp[i][0]:
                group.append(temp[i])
        
        if group:
            group.insert(0, temp[0])
            temp = [j for j in temp if j not in group]

            for j in range(len(group)):
                group[j] += e
            
            for c in group[0]:
                f1 = 0
                for j in group:
                    if c!=j[0]:
                        f1 = 1
                if f1:
                    beta = group
                    break
                else:
                    alpha += group[0][0]
                    for j in range(len(group)):
                        group[j] = group[j][1:]
                
                for j in range(len(beta)):
                    if beta[j][0] != e:
                        beta[j] = beta[j][:-1]
            
            a.products.append(alpha+alpha[0]+"'")
            p.append(Prod(alpha[0]+"'",beta))
        else:
            a.products.append(temp[0])
            temp.pop(0)


num = int(input("Enter no. of Productions : "))
for i in range(num):
    ip = input(f"production {i+1} : ")
    name, prod = ip.split(' -> ')
    productions = prod.split(' | ')
    p.append(Prod(name, productions))

print("Productions")
for x in p:
    x.print()

print("After transforming")
trans()

for x in p:
    x.print()