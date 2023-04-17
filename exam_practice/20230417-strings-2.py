# page 9

texto = "This is a Long text and Only the letters with Capital letters will be Included"
a = texto.split(" ")
print(a)
for i in a:
  print(i[0])

a_lower = [i.lower() for i in a]
print(sorted(a_lower))
