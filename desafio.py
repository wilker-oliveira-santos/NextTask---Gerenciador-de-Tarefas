def sum_digitos(n):
   if n < 10:
      return n
   else:
      return (n % 10) + sum_digitos(n //10)
   
print(sum_digitos(1234))
print(sum_digitos(7))