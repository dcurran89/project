import re

dumbstring = 'find me'
pattern = re.compile(r'me')

match = pattern.findall(dumbstring)
print(match)
