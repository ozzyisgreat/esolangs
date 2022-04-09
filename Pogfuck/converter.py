e = input("what brainfuck file would you like to convert to pogfuck: ")
c = open(e, "r")
bf = c.read()
c.close()

p = bf.replace(">", "pog")
p = p.replace("<", "poog")
p = p.replace("+", "pooog")
p = p.replace("-", "poooog")
p = p.replace(".", "pooooog")
p = p.replace(",", "poooooog")
p = p.replace("[", "pooooooog")
p = p.replace("]", "poooooooog")

f = open("code.pf", "w")
f.write(p)
f.close()

print(f"your equivelent pogfuck code\n {p} \n your pogfuck code can be found in code.pf")

