R = range(10)
D = []
omega = dict()
for x in R:
  omega[x] = 0 if x % 2 == 0 else 1
  D.append((x,x))

# lambda expression in sort call below can acess variable in scope, e.g., omega
D.sort( lambda x,y: omega[x[0]] - omega[y[0]] )
print D

C = [("aa", 100), ("A", 100), ("adnan",10), ("aa", 1000), ("b",5)]

zeta = {}
zeta["b"] = -1
zeta["aa"] = -1
zeta["adnan"] = 0
zeta["A"] = 1

# lambda expression in sort call below can acess variable in scope, zeta in this case
# would be much clumsier if we had to explicitly send it to lambda.
C.sort( lambda x,y: (zeta[x[0]] - zeta[y[0]]) if ( x[0] != y[0] ) else cmp(x[1], y[1]) )
print C
