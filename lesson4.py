# -*- coding: utf-8 -*-
# рядочок зверху потрібен для того, щоб можна було використовувати кирилицю в наших
# коментарях, детальніше про це тут: http://www.python.org/dev/peps/pep-0263/
#Цикли і Умовні оператори
i = 0
while i < 10:
	print(i)
	i +=1
print('I after while', i)

#
i = 1
while i <= 20:
	if i % 2 == 0:
		print(i)
	i +=1
print ('Done')
print('I after while', i)


i = 10
while i > 0:
	#print(i)
	if i > 5:
		print("Bigger than 5!")
	elif i % 2 != 0:
		print("this is ODD number and i <= 5 i = ", i)
	else:
		print("this is EVEN number, not ODD and i <= 5 i = ", i)
	i = i - 1

print("we are after 'while' loop")
print("the end")
