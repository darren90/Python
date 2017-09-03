#-*- coding: UTF-8 -*-


import base64


s = '我是字符串Base64编码是一种“防君子不防小人”的编码方式。广泛应用于MIME协议，作为电子邮件的传输编码，生成的编码可逆，后一两位可能有“=”，生成的编码都是ascii字符。优点：速度快，ascii字符，肉眼不可理解\缺点：编码比较长，非常容易被破解，仅适用于加密非关键信息的场合'
a = base64.b64encode(s)
print a

print base64.b64decode(a)