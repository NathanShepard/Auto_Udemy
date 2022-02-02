import re, pyperclip


#the regular espresstion  for the phone numbers

phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d)))?         #area code(oprional)
(\s|-)                          #first separator
\d\d\d                          #first 3 digits
-                               #separator
\d\d\d\d                       #last for numbers
(((ext(\.?\s)|x)               #extention number
(\d(2,5)))?                    #extension numbers
)
''', re.VERBOSE)

# how do I run this on a text file?

this = pyperclip.paste()

print(this)

#phoneRegex.find()

# cool I see some of the ideas that this is helping me with I'd like to be able to
# work with this and not be pervented to work because of the

#the email regular espresstion..



# testing for the file in Airbook and moving into this ONE and THAT ONE...
