import os
from pwn import *
import enchant

USER = 'bandit0'
PASSWORD = 'bandit0'
URL = 'bandit.labs.overthewire.org'
PORT = 2220
MAGIC_COMMAND = 'cat readme | grep "password"'

eng_dictionary = enchant.Dict('en_US')
shell = ssh(USER, URL, password=PASSWORD, port=PORT)
sh = shell.run(MAGIC_COMMAND)

wordlist = sh.recvallS().split() 
possible_passwords = [f'- {string}' for string in wordlist if not eng_dictionary.check(string)]
print()
print('Possible passwords:')
print('\n'.join(possible_passwords))
print()
print('Original output:')
print(' '.join(wordlist))
print()

shell.close()
