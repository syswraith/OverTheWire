import os
from pwn import *
import enchant

URL = 'bandit.labs.overthewire.org'
PORT = 2220

USER = 'bandit8'
MAGIC_COMMAND = 'cat data.txt | sort | uniq -u'

with open('password.txt', 'r') as file:
    PASSWORD = file.read()

eng_dictionary = enchant.Dict('en_US')
shell = ssh(USER, URL, password=PASSWORD, port=PORT)

#interactive_shell = shell.process('/bin/sh')
#interactive_shell.interactive()

sh = shell.run(MAGIC_COMMAND)
output = sh.recvallS()

wordlist = output.split()
possible_passwords = [string for string in wordlist if not eng_dictionary.check(string)]

for passw in possible_passwords: 
    if len(passw) == 32:
        with open('password.txt', 'w') as file: file.write(passw)

print()
print('Possible passwords:')
for x in possible_passwords: print(f'- {x}')
print()
print('Original output:')
print(output)
print()

shell.close()
