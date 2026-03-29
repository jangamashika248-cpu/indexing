Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #indexing
>>> a="vijayawada"
>>> a[1]
'i'
>>> a[3]
'a'
>>> a[5]
'a'
>>> a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'vijaya'
>>> b="iam in a class"
>>> b[1]
'a'
>>> b[5]
'n'
>>> b[8]+b[9]+b[10]+b[11]+b[12]
' clas'
>>> b[8]+b[9]+b[10]+b[11]+b[12]+b[13]
' class'
>>> c="time is a very precious"
>>> c[3]
'e'
>>> c[4]
' '
>>> c[10]
'v'
>>> d="time is very precious"
>>> d[10]
'r'
>>> d[9]+d[10]+d[11]+d[12]
'ery '
>>> d[8]+d[9]+d[10]+d[11]+d[12]
'very '
>>> d[13]+d[14]+d[15]+d[16]+d[17]+d[18]+d[19]+d[20]
'precious'
>>> #negative
>>> a="i love python"
>>> a[-1]
'n'
>>> a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'python'
a[-11]+a[-10]+a[-9]+a[-8]
'love'
b="vizag is a city of destiny"
a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
' python'
b[-7]+b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'destiny'
b[-26]+b[-25]+b[-24]+b[-23]+b[-22]
'vizag'
