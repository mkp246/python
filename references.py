def f(d):
	return d
c = [6,4,5]
e = f(c)
print(c is e)


def banner(message, border='-'):
	line = border * len(message)
	print(line)
	print(message)
	print(line)


banner("I am Don")
banner('I am Don', '+')
banner('I am Don', border='/')
banner(border='^', message= 'I am Don')


# check eval of keyword params
import time
print(time.ctime())
def show_default(arg=time.ctime()):
	print(arg)

show_default()

def add_spam(menu=[]):
	menu.append("spam")
	return menu

breakfast = ['egg', 'becon']
add_spam(breakfast)
print(breakfast)
print(add_spam())
print(add_spam())
print(add_spam())

# eg default is evaluated at def call 
# once and created new ref for default
# which retains values there is subsequent calls
#fix use None
def add_spam_1(menu=None):
	if menu is None:
		menu =[]
	menu.append('spam')
	return menu

print(add_spam_1())
print(add_spam_1())
print(add_spam_1())