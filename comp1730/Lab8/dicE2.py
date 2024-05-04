def histogram(seq):
	count = dict()
	for elem in seq:
		if elem not in count:
			count[elem] = 1
		else:
			count[elem] += 1
	return count

# result= histogram('neverending')
# result= histogram('mississippi')
# result= histogram([2, 1, 4, 6, 5, 5, 3, 4, 4, 6])

wordlist = ['test', 'your', 'function', 'with', 'a', 'diverse',
 'range', 'of', 'examples', 'your', 'tests', 'should', 'cover',
 'all', 'cases', 'for', 'example', 'test', 'words', 'beginning',
 'with', 'a', 'vowel', 'and', 'word', 'beginning', 'with', 'a',
 'consonant', 'pay', 'particular', 'attention', 'to', 'edge',
 'cases', 'for', 'example', 'what', 'happens', 'if', 'the',
 'word', 'consists', 'of', 'just', 'one', 'vowel', 'like',
 'a', 'what', 'happens', 'if', 'the', 'string', 'is', 'empty']

# result= histogram(wordlist)
histogram([[1,2], [2,1], [1,2], [1], [2]])
print(result)