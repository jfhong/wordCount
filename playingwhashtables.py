f = open("/Users/julianhong/Desktop/future/stonks.txt", "r")
fred = f.readline().split()

hashtable = {}
for word in fred:
	word.lower()
	for char in ' ?,.!/;:':
		word = word.replace(char, '')
	# print(word)
	if word not in hashtable:
		newValue = {word: 1}
		hashtable.update(newValue)
		# print(word, "key:", hashtable[word])
	else:
		hashtable[word] = hashtable[word] + 1
		# print(word, "key:", hashtable[word])

total = sum(hashtable.values())
print(hashtable)
print("Number of total words:", total)