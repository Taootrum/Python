# 这是单行注释
"""
这是多行注释
"""
import keyword
import time

print("Hello World")
a = 5
print(type(a))
a = "Hello World"
print(type(a))

print(keyword.kwlist)

a = None
print("a = ", a)

a = 1_000_000
print("a = ", a)
a = 0x1_000_000
print("a = ", a)
a = 0b1_000_000
print("a = ", a)

a = 'Hello Hi'
print(a)

s1 = "The Book price:"
p = 99
print(s1 + str(p))
print(s1 + repr(p))

print(repr(s1))

# msg = input("Please input:")
# print(type(msg))
# print(msg)

str1 = '''fdasfasfnasofajfasfjasfj;fantasists'''
print(str1)

str1 = r'"Let\'s go", said Charlie'
print(str1)

b1 = bytes()
print(b1)
b2 = b''
print(b2)
b3 = b'Hello'
print(b3)
print(b3.decode())
print(b3[0])
print(type(b3))
print(type(b3[0]))
# print(b3[0].decode())
print(b3[2:4])
print(b3[2:4].decode())
b4 = bytes('i love you', encoding='utf-8')
print(b4)
b5 = "i love you".encode('utf-8')
print(b5)

price = 108
print("the book's price is %s" % price)

str2 = "the book's price is "
b = "price" in str2
print(type(b))
print(b)
print("the" in str2)
print("the123" in str2)

print(dir(keyword))

print(str2.lower())
print(str2.upper())

str3 = "crazy.org is a good site"
table = str3.maketrans('abcd', 'rghj')
print(str3.translate(table))
print(table)
print(str3.split())
print(str3.split('.'))
print('/'.join(str3.split()))
print('/'.join(str3.split('.')))

print("5.2 % -2.9 = ", 5.2 % -2.9)

a = time.gmtime()
b = time.gmtime()
print(type(a))
print(type(b))
print(a)
print(b)
print(id(a))
print(id(b))
print(a is b)

a = time.gmtime(time.time())
print(a)
print('time.time() = ', time.time())

bookName = "疯狂Python"
price = 79
version = "正式版"
if bookName.endswith('Python') and (price < 50 or version == "正式版"):
    print("打算购买这本Python 图书")
else:
    print("不购买！")

a = 4
b = 1
print(b < a)
print(print("a > b") if a > b else print('b < a'))
print(print("a > b"), 'a > b' if a > b else print('b < a'))
str1 = 'a > b'; print("a > b") if a > b else print('b < a')
print(str1)
str1 = y = 100, 'a > b' if a > b else print('b < a')
print(str1)

str3 = "nihaoma fdajiaosfjdaf crazi tshi"
print('a' in str3)
print('taoshi' in str3)
print('tshi' in str3)

str1 = 'a > b'
print("a > b") if a > b else print('b < a')
print(str1)

str1 = 'a > b'
x = 20 if a > b else print('b < a')
print(str1)
print(x)
