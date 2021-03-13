#docker build -t fubini .
#docker run fubini <natürliche Zahl>




#Idee: Berechnung a(n)=summe_{i=1}^n (n über i) * a(n-i)


import sys
import binomial
n=int(sys.argv[1]) #eingegebene Zahl n

#Berechne (b über a) für a,b∈{0,..,n} -> Speicherplatzverbrauch ∈ O(n^2) ( (n+1)^2 integer == für n<=32 ist das weniger als 4 kB)
binomiales = binomial.generate_lookup(n)

fubini = [1]
for k in range(1,n): # berechnung der k-ten fubini-zahl
#	val = 0
#	for i in range(1,k+1):
#		val += binomiales[k][i] * fubini[k-i]
#	fubini += [val]
	fubini += [sum([binomiales[k][i] * fubini[k-i] for i in range(1,k+1)])]

print(binomiales)
print(fubini)