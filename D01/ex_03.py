import string

string1 = "MaRviN THE bOt"
# string1lowercase = string1.casefold()
string1lowercase = string1.lower()
string1uppercase = string1.upper()
string1nospace = string1.replace(" ", "")
# string1nospace = string1.translate({ord(c): None for c in string.whitespace})
print(string1lowercase)
print(string1uppercase)
print(string1nospace)