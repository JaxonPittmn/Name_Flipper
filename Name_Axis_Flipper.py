school = input("School Name: ")
tm1 = input("Team Member 1: ")
tm2 = input("Team Member 2: ")
tm3 = input("Team Member 3: ")
spons = input("Sponsor: ")
print(" ")

print(school)
tm1Len = len(tm1)
tm2Len = len(tm2)
tm3Len = len(tm3)

for i in range(max(tm1Len, tm2Len, tm3Len)):
	if i >= tm1Len or tm1[i] == " ":
		tm1_letter = "_"
	else:
		tm1_letter = tm1[i]

	if i >= tm2Len or tm2[i] == " ":
		tm2_letter = "_"
	else:
		tm2_letter = tm2[i]

	if i >= tm3Len or tm3[i] == " ":
		tm3_letter = "_"
	else:
		tm3_letter = tm3[i]
		
	newString = f"{tm1_letter} {tm2_letter} {tm3_letter}"
	print(newString)
print(f"{spons} - Sponsor")
