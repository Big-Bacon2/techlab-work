word = input("type a word.")
total = 0
for letter in word:
	if letter in ['a','e','i','o','u']:
		total = total + 1

print total