Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #slicing
>>> a="codegnan"
>>> a[0:4]
'code'
>>> a[4:8]
'gnan'
>>> a[:4]
'code'
>>> a[4:]
'gnan'
>>> b="work until you succeed"
>>> b[:3]
'wor'
>>> b[:4]
'work'
>>> b[5:9]
'unti'
>>> b[5:10]
'until'
>>> b[12:15]
'ou '
>>> b[11:15]
'you '
>>> b[17:25]
'cceed'
>>> b[16:25]
'ucceed'
>>> b[15:]
'succeed'
>>> c="simple is better than complex"
>>> c[17:21]
'than'
>>> c[22:29]
'complex'
>>> c[10:16]
'better'
>>> c[0:6]
'simple'
>>> #negative
>>> a="codegnan it solutions"
a[-10:-1]
' solution'
a[-11:-1]
't solution'
a[-11:]
't solutions'
a[-10:]
' solutions'
a[13:11]
''
a[-13:-11]
' i'
a[-13:-10]
' it'
a[-21:-13]
'codegnan'
b="beautiful is better than ugly"
b[-5:]
' ugly'
b[-4:]
'ugly'
b[-16:10]
''
b[-16:-10]
'better'
b[-29:-20]
'beautiful'
#striding
a="data science"
a[::]
'data science'
a[::1]
'data science'
a[::3]
'dacn'
b="cloud computing"
b[::4]
'cdmi'
b[::2]
'codcmuig'
b[::6]
'cci'
b[5:]
' computing'
b[3:11]
'ud compu'
b[:9]
'cloud com'
c="machine learning"
c[2:12:4]
'cea'
c[3:15:6]
'he'
c[1:14:3]
'ai ai'
#negative
a="python course"
a[-1:-9:-2]
'ero '
a[-3:-12:-4]
'r t'
a="python course"
a[7:3:2]
''
a[-6:-5:-2]
''
a[::1]
'python course'
a[::-1]
'esruoc nohtyp'
