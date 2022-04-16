#convert brainfuck to PenisScript

e = input("what brainfuck file would you like to convert to PenisScript: ")
c = open(e, "r")
bf = c.read()
c.close()

p = bf.replace(">", "8=D")
p = p.replace("<", "8==D")
p = p.replace("+", "8===D")
p = p.replace("-", "8====D")
p = p.replace(".", "8=====D")
p = p.replace(",", "8======D")
p = p.replace("[", "8=======D")
p = p.replace("]", "8========D")

f = open("code.ps", "w")
f.write(p)
f.close()

print(f"your equivelent PenisScript code\n{p}\n your PenisScript code can be found in code.ps")
