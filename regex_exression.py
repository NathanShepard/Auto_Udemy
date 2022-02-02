import re, pyperclip

#the regular espresstions  for the phone numbers


# phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?                           #area code(optional)
-                                #first separator
\d\d\d                           #first 3 digits
(\s|-)?                                #separator
\d\d\d\d                         #last for numbers
)
''',re.VERBOSE)

#the email regular espresstion..
emailRegex = re.compile(r'''
#some+_thing@(\d{2,5}))?.com  notes for WHAT you are looing to find!

[a-zA-Z0-9_.+]+    #name part
@                  # @ symbol
[a-zA-z0-9_.+]+    #domain name part

''',re.VERBOSE)

# TODO: Get the test off the clipboard
# clipboard is a Lagacy Code item I (as a 2019 "programer? " didn't know about!!!)
# Nathan when something DOES NOT MAKE SENCE WHEN YOU READ IT  >>>>>> LOOK IT UP !!!!! <<<<<<

text = pyperclip.paste()


#TODO: EXTRACT the email/phone from this text



extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
# why can't I see what this is ?
# Find all? = what? right its the recompiled intantied object
# now I can use the tools from re to work on that instance of that object?
# here is the idea that I can go through a for loop on each "obkect that python "sees"?
# I can do something to "it"( that part, that object? )
print(extractedPhone)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

#HOW to make a data strucer that works well. ?



#print('\n',extractedPhone)

#print('\n',extractedEmail)

print('\n',allPhoneNumbers)
