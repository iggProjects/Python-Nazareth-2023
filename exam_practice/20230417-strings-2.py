# page 9
texto = "This is a Long text and Only the letters with Capital letters will be Included"
texto2 = "This is a    Long     text    and Only the letters with Capital letters will be Included"
print(f"first text: {texto}")
print(f"second text: {texto2}")


a = texto.split(" ")
print(a)
print()

upperLettersInText = []
for i in a:
  print(i[0])
  if i[0].isupper():
     upperLettersInText.append(i[0])   
print(f"list of Upper Letters\n\t{upperLettersInText}\n")
print()

a_lower = [i.lower() for i in a]
print(f"list of Upper Letters\n\t{sorted(a_lower)}")
#print(sorted(a_lower))

