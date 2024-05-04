wordlist = ['test', 'your', 'function', 'with', 'a', 'diverse',
 'range', 'of', 'examples', 'your', 'tests', 'should', 'cover',
 'all', 'cases', 'for', 'example', 'test', 'words', 'beginning',
 'with', 'a', 'vowel', 'and', 'word', 'beginning', 'with', 'a',
 'consonant', 'pay', 'particular', 'attention', 'to', 'edge',
 'cases', 'for', 'example', 'what', 'happens', 'if', 'the',
 'word', 'consists', 'of', 'just', 'one', 'vowel', 'like',
 'a', 'what', 'happens', 'if', 'the', 'string', 'is', 'empty']

wordlen={word:len(word) for word in wordlist}
print(wordlen)