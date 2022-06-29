import re
A = 'test'
B = 't.'
if re.match(B, A):
    print('일치함')
else:
    print('일치하지 않음')