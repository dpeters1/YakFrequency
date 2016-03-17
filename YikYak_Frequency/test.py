import re

wordList = ['hello', 'test?', 'cow', 'moo']

regex = re.compile(r'([^\s\w]|_)+',)

print [regex.sub("", word) for word in wordList]

