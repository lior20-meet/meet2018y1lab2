Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a=5
>>> b=10
>>> temp=5
>>> a=b
>>> b=temp
>>> a
10
>>> b
5
>>> four='4'
>>> print(four*3)
444
>>> five=4
>>> print(five)
4
>>> print(five*3)
12
>>> print(five*3)
12
>>> print(four*3)
444
>>> Hi, student
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    Hi, student
NameError: name 'Hi' is not defined
>>>  my_name = ‘student’
SyntaxError: unexpected indent
>>> my_name= 'student'
>>> print("Hi'"+myName')
	  
SyntaxError: EOL while scanning string literal
>>> print("Hi,"+'student')
	  
Hi,student
>>> print("Hi,"+'myaName')
	  
Hi,myaName
>>> 'myName'='student'
	  
SyntaxError: can't assign to literal
>>> print('Hi,'+"myName")
	  
Hi,myName
>>> print("Hi,"+'my_name')
	  
Hi,my_name
>>> 'myName'="student"
