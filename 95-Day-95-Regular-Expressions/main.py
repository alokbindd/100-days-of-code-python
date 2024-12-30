# https://regexr.com/
import re

# pattern = r"[A-z]+egular"
# text = '''
# A regular expression (shortened as regex or regexp),[1] sometimes referred to as rational expression,[2][3] is a sequence of characters that specifies a match pattern in text. Usually such patterns are used by string-searching algorithms for "find" or "find and replace" operations on strings, or for input validation. Regular expression techniques are developed in theoretical computer science and formal language theory.
# The concept of regular expressions began in the 1950s, when the American mathematician Stephen Cole Kleene formalized the concept of a regular language. They came into common use with Unix text-processing utilities. Different syntaxes for writing regular expressions have existed since the 1980s, one being the POSIX standard and another, widely used, being the Perl syntax.
# '''

# match = re.search(pattern,text)
# print(match.span()[0])


# matches = re.finditer(pattern, text)
# for match in matches:
#     print(text[match.span()[0]:match.span()[1]])

pattern = r"\w+@\w+\.\w+"
text = '''
	alok@mail.com 
	dhiraj12@mail.com
	yahoo23@mail.com

'''
matches = re.finditer(pattern,text)
for match in matches:
    print(text[match.span()[0]:match.span()[1]])