import pandas as pd 
datos = list (range (10))
print (datos)

pf = pd.Series(datos)

print (pf)

pares = pf [pf %2 ==0]
print (pares)

impares = pf [pf %2 ==1]
print (impares)