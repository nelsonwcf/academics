import nltk

# Exercise 1

string = 'colorless'
print(string[0:4] + 'u' + string[4:]), '\n'

# Exercise 2

ex2list = ['dishes', 'running', 'nationality', 'undo', 'preheat']
print ex2list[0][:-2], ex2list[1][:-4], ex2list[2][:-5], ex2list[3][:-2], ex2list[4][:-4] + '\n'

# Exercise 3

print "This question is a bit ambiguous because the start of a String is on index 0" \
      "but python allows the use of negative strings to refer to the reverse of the word up to -len(string)."
print "So, no, you can't address any element before the beginning of the String per say, but if you go beyond" \
      "the negative length of string, the interpreter will return an IndexError as well."
print "Example: In the word 'dragon' any indexing from -6 to 5 is valid. Any value outside this range will" \
      "return IndexError." + '\n'

# Exercise 4

word = 'abcdefghijklmnopqrstuvxyz'
print word[::2]
print word[::-2]
print word[::-1]
print word[5:15:-1]
print word[15:5:-1] + '\n'
# print word[::0] // returns error as step can't be 0, obviously.

# Exercise 5

print "It is reasonable because it is going to count from 0 to the negative end" \
    "of the string, and the index in the string contain the string in reverse order." \
    "(-1 is the last character, -2 is the second last and so)." + '\n'

# Exercise 6

print '[a-zA-Z]+: Any word (excluding blank) that contains at least one upper or lower case character.'
nltk.re_show(r'[a-zA-Z]+', 'dragon')  # Yes
nltk.re_show(r'[a-zA-Z]+', 'eggs')  # Yes
nltk.re_show(r'[a-zA-Z]+', 'Abacus')  # Yes
nltk.re_show(r'[a-zA-Z]+', '')  # No
nltk.re_show(r'[a-zA-Z]+', '1Ab1cus')  # No but will match portions of the word
print

print '[A-Z][a-z]+: Any uppercase word (excluding blank) that contains the first uppercase character.'
nltk.re_show(r'[A-Z][a-z]+', 'dragon')  # No
nltk.re_show(r'[A-Z][a-z]+', 'Dragon')  # Yes
print

print 'p[aeiou]{,2}t: Words that start with p and ends with t with no more than 2 lowercase vowels in the middle'
nltk.re_show(r'p[aeiou]{,2}t', 'p')  # No
nltk.re_show(r'p[aeiou]{,2}t', 't')  # No
nltk.re_show(r'p[aeiou]{,2}t', 'pt')  # Yes
nltk.re_show(r'p[aeiou]{,2}t', 'pat')  # Yes
nltk.re_show(r'p[aeiou]{,2}t', 'paut')  # Yes
nltk.re_show(r'p[aeiou]{,2}t', 'pauut')  # No
nltk.re_show(r'p[aeiou]{,2}t', 'p1t')  # No
nltk.re_show(r'p[aeiou]{,2}t', 'pata')  # No but will match portions of the word
print

print '\d+(\.\d+)?: Any well formed number with decimals and decimals with fractions'
nltk.re_show(r'\d+(\.\d+)?', '1')  # Yes
nltk.re_show(r'\d+(\.\d+)?', '10')  # Yes
nltk.re_show(r'\d+(\.\d+)?', '10.')  # No but will match portions of the word
nltk.re_show(r'\d+(\.\d+)?', '10.1')  # Yes
nltk.re_show(r'\d+(\.\d+)?', '10..1')  # No but will match portions of the word
print

print '([^aeiou][aeiou][^aeiou])*: Any 3n character word with the n and n + 2 characters being anything' \
      ' but lowercase vowels and n + 1 being any lowercase vowel. Empty word also allowed.'
nltk.re_show(r'([^aeiou][aeiou][^aeiou])*', '')  # Yes
nltk.re_show(r'([^aeiou][aeiou][^aeiou])*', '1')  # No but will match portions of the word
nltk.re_show(r'([^aeiou][aeiou][^aeiou])*', 'aaa')  # No but will match portions of the word
nltk.re_show(r'([^aeiou][aeiou][^aeiou])*', 'Aaa')  # No but will match portions of the word
nltk.re_show(r'([^aeiou][aeiou][^aeiou])*', 'faD')  # Yes
nltk.re_show(r'([^aeiou][aeiou][^aeiou])*', 'faD1ux')  # Yes
print

print '\w+|[^\w\s]+: Any word including numbers, uppercase and lowercase characters OR any number ' \
      'of symbols (Non alphanumeric character) excluding whitespace characters. Looks like a simple' \
      'word tokenizer.'
nltk.re_show(r'\w+|[^\w\s]+', 'gadget')  # Yes
nltk.re_show(r'\w+|[^\w\s]+', 'This is my rifle. This is my gun.')  # All words and dots. Excludes spaces.
nltk.re_show(r'\w+|[^\w\s]+', 'jack-in-the-box;.')  # {jack}{-}{in}{-}{the}{-}{box}{;.}
print
