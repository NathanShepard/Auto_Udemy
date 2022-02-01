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


#the email regular espresstion..
emailRegex = re.compile(r'''
#some+_thing@(\d{2,5}))?.com  notes for WHAT you are looing to find!

[a-zA-Z0-9_.+]+    #name part
@                  # @ symbol
[a-zA-z0-9_.+]+    #domain name part

''', re.VERBOSE

# TODO: Get the test off the clipboard

text = pyperclip.paste()

#TODO: EXTRACT the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

print(extractedPhone)
print(extractedEmail)
