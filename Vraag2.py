#vraag 2a:
Dictionary= {"Voornaam:": "Harry", "Achternaam:": "van Winkel", "Geboortedatum:" : "27-3-1939"}
for k, v in Dictionary.items():
  print(k, v)
#vraag 2b:
print(Dictionary ["Voornaam:"])
#vraag 2c:
Dictionary.update({"Voornaam:": "Henrikus"})
for k, v in Dictionary.items():
  print(k, v)