s = 'I love china'
print(s[7:12:1])
print(s[7:12:2])

print(s.split(' '))

c = 'abcabc'
print('a' in c)
print('a' not in 'abc')

print(c.count('a'))
print(c.count('a', 2, 4))

print(c.find('bc'))
print(c.find('bc', 3, 6))

print(c.replace('abc', 'cba'))

fileName = 'xx.jpg'
print(fileName.endswith('jpg'))

ss = '   a    b    '
print(ss.strip())     # lstrip()  rstrip()

aa = ['yyyy', 'mm', 'dd']
print('-'.join(aa))




