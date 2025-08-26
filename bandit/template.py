import os
from pwn import *
import enchant

USER = 'bandit1'
URL = 'bandit.labs.overthewire.org'
PORT = 2220
MAGIC_COMMAND = 'cat ~/-'
PASSWORD = 'ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If'

eng_dictionary = enchant.Dict('en_US')
shell = ssh(USER, URL, password=PASSWORD, port=PORT)
sh = shell.run(MAGIC_COMMAND)

output = sh.recvallS()
wordlist = output.split()
possible_passwords = [f'- {string}' for string in wordlist if not eng_dictionary.check(string)]
print()
print('Possible passwords:')
print('\n'.join(possible_passwords))
print()
print('Original output:')
print(output)
print()

shell.close()
