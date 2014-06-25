word = input("type a word.")
total = 0
for letter in word:
	if letter in ['q','w','r','t','p','s','d','f','g','h','j','k''l','z','x','c','v','b','n','m']:
		total = total + 1

print total