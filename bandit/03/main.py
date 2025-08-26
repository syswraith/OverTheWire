import os
from pwn import *
import enchant

URL = 'bandit.labs.overthewire.org'
PORT = 2220

USER = 'bandit2'
MAGIC_COMMAND = 'cat < "--spaces in this filename--"'
PASSWORD = '263JGJPfgU6LtdEvgfWU1XP5yac29mFx'

eng_dictionary = enchant.Dict('en_US')
shell = ssh(USER, URL, password=PASSWORD, port=PORT)

#interactive_shell = shell.process('/bin/sh')
#interactive_shell.interactive()

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
