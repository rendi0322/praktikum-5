hobi = input("masukan hobi kamu: ")
print (f"Hobi anda ada: {hobi}")
nama = input("masukan nama anda: ").upper()
print(f"Huruf Awal Nama Anda: {nama[0]}")
from random import randint
x = randint (0,100)
y = randint (0,100)
hasil = int(input(f"berapakah perkalian {x} dan {y} : "))
print (f"Jawaban Kamu {hasil==x * y}")
print("Names: Panik")
print("UNICODE: U0001F631")
print("\U0001F631")
kalimat = "Belajar Pemrograman Python"
print (f"1. {kalimat[0:7]}")
print (f"2. {kalimat[3:7]}")
print (f"3. {kalimat[8:19]}")
print (f"4. {kalimat[13:17]}")
print (f"5. {kalimat[20:26]}")
print (f"6. {kalimat[20:22]}")
print (f"7. {kalimat[13:17]} {kalimat[20:26]}")
print (f"8. {kalimat[8:19]} {kalimat[20:22]}")
def isEmailValid(email):
	content = email.split("@") 
	haveNoSpace = email.find(" ") == -1 
	isContent = len(content) == 2 
	isIdentifier = content[0].isidentifier() 
	isDomain = len(content) == 2 and content[1].find(".") != -1 and (not content[1].startswith(".")) and (not content[1].endswith(".")) 
	return haveNoSpace and isContent and isIdentifier and isDomain 
emails = ["alunsujjada@gmailcom", "alunsujjada@gmail.com", "alun.sujjada@gmail.com", "alunsujjada.gmail.com", "alun.sujjada@gmailcom"] 
for email in emails:
	isValid = isEmailValid(email) 
	print(f"{email} -> {isValid}")
