s = raw_input("Enter a string: ")

letters = []

for i in s:
	letters.append(i)

letters.reverse()

nothing = ""

finishedString = nothing.join(letters)

print finishedString
