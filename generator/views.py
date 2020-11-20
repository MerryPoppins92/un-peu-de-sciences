from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .forms import PassWordForm
# from .models import PassWord2
import random as stdlib_random
from scipy import *
from django.db import IntegrityError

import matplotlib.pyplot as plt


from matplotlib import pylab
from pylab import *
import PIL, PIL.Image
from io import BytesIO


# Create your views here.

def home(request):
	return render(request, 'generator/home.html')

def about(request):
	return render(request, 'generator/about.html')

def primepage(request):
	return render(request, 'generator/primepage.html')

def fibopage(request):
	return render(request, 'generator/fibopage.html')

def romainpage(request):
	return render(request, 'generator/romainpage.html')

def factorpage(request):
	return render(request, 'generator/factorpage.html')

def base16page(request):
	return render(request, 'generator/base16page.html')
	
def base2page(request):
	return render(request, 'generator/base2page.html')

def seconddegrepage(request):
	return render(request, 'generator/seconddegrepage.html')

def cesaerpage(request):
	return render(request, 'generator/cesaerpage.html')

def sysdeqpage(request):
	return render(request, 'generator/sysdeqpage.html')

def pgcd(a,b):
    """pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre les 2 nombres entiers a et b"""
    while b!=0:
        r=a%b
        a,b=b,r
    return a


def sysdeq(request):
	a = int(request.GET.get('a'))
	b = int(request.GET.get('b'))
	c = int(request.GET.get('c'))
	ap = int(request.GET.get('ap'))
	bp = int(request.GET.get('bp'))
	cp = int(request.GET.get('cp'))
	try:
		d = int(request.GET.get('d'))
		dp = int(request.GET.get('dp'))
		app = int(request.GET.get('app'))
		bpp = int(request.GET.get('bpp'))
		cpp = int(request.GET.get('cpp'))
		dpp = int(request.GET.get('dpp'))
	except TypeError:
		d = 'a'
		dp = '0'
		app = '0'
		bpp = '0'
		cpp = '0'
		dpp = '0'


	if d == 'a':
		x = 0
		y = 0
		z = None
	  	# calculating the determinant of matrix 
		detx = b * cp - bp * c # np.linalg.det(dx)
		dety = a * cp - ap * c 
		detc = a * bp - ap * b
		print(dety)
		print(detx)
		print(detc)
		if detc == 0:
			if (a * bp == ap * b) and (a * cp != ap * c):
				x = "Les droites sont strictement paralleles"
				y = "Le systeme n'admet pas de solution"
				return render(request, 'generator/sysdeq.html', {'x':x, 'y':y})
			elif (a * bp == ap * b) and (a * cp == ap * c):
				x = "Les droites sont confondues"
				y = "Tous les couples (x;y) qui verifient l'equation ax+by+c=0 sont solutions, il y en a une infinite"
				return render(request, 'generator/sysdeq.html', {'x':x, 'y':y})
		else:
			x = detx/detc
			y = -(dety/detc)  
			return render(request, 'generator/sysdeq.html', {'x':x, 'y':y})
	else:
		x = 0
		y = 0
		z = 0

		detx = (b * ((cp * dpp) - (cpp * dp))) + (c * ((bpp * dp) - (bp * dpp))) + (d * ((bp * cpp) - (bpp * cp)))
		dety = (a * ((cp * dpp) - (cpp * dp))) + (c * ((app * dp) - (ap * dpp))) + (d * ((ap * cpp) - (app * cp)))
		detz = (a * ((bp * dpp) - (bpp * dp))) + (b * ((app * dp) - (ap * dpp))) + (d * ((ap * bpp) - (app * bp)))
		detd = (a * ((bp * cpp) - (bpp * cp))) + (b * ((app * cp) - (ap * cpp))) + (c * ((ap * bpp) - (app * bp)))
		print(detx)
		print(dety)
		print(detz)
		print(detd)
		if detd == 0:
			x = "si les coeficients (a,b,c,d) sont proportionnels alors les plans P1, P2 et P3 sont confondus"
			y = "si les coeficients (a,b,c) sont proportionnels alors les plans P1, P2 et P3 sont paralleles"
			z = "Les plans se coupent par une droite"
			return render(request, 'generator/sysdeq.html', {'x':x, 'y':y, 'z': z})			

		else:
			x = -detx/detd
			y = dety/detd
			z = -detz/detd
			return render(request, 'generator/sysdeq.html', {'x':x, 'y':y, 'z': z})

def cesaer(request):
	try:
		string = request.GET.get('text')
		decalage = int(request.GET.get('x'))
		x = 0
		l = ""
		for i in string:
		    if (ord(i) >= 65 and ord(i) <= (90 - decalage)) or (ord(i) >= 97 and ord(i) <= (122 - decalage)):
		        i = ord(i) + decalage
		        l = l + chr(i)
		        x += 1
		    elif (ord(i) >= (90 - decalage) and ord(i) <= 90) or (ord(i) >= (122 - decalage) and ord(i) <= 122):
		        i = ord(i) + decalage - 26
		        l = l + chr(i)
		        x += 1
		    else:
		        l = l + i
		print(l)
		return render(request, 'generator/cesaer.html', {'l': l})
	except:
		return render(request, 'generator/cesaerpage.html', {'error': "Vous avez entre des valeurs incorrectes"})

def seconddegre(request):
	try:
		a = int(request.GET.get('a'))
		b = int(request.GET.get('b'))
		c = int(request.GET.get('c'))
		delta = b**2 - 4 * a * c
		string_equation = f"Pour l'equation: {a}x2 + {b}x + {c} = 0 // Discriminant egale a {delta}"
		maxi = -b/(2*a)
		if delta < 0:
			string_title = "L'equation n'a pas de solution"
		elif delta == 0:
			string_title = f"L'equation n'admet qu'une solution x0 = {maxi:.2f}"
		elif delta > 0:
			x1 = (-b-sqrt(delta))/(2*a)
			x2 = (-b+sqrt(delta))/(2*a)
			string_title = f"L'equation admet deux solutions x1 = {x1:.2f} et x2 = {x2:.2f}"


		x = arange(maxi - 10, maxi + 10, 0.01)
		s = a*x**2 + b*x + c
		plot(x, s)

		xlabel(string_equation)
		ylabel('ylabel(Y)')

		title(string_title)
		grid(True)

		# Store image in a string buffer
		buffer = BytesIO() #.StringIO()
		canvas = pylab.get_current_fig_manager().canvas
		canvas.draw()
		pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
		pilImage.save(buffer, "PNG")
		pylab.close()

		# Send buffer in a http response the the browser with the mime type image/png set
		return HttpResponse(buffer.getvalue(), content_type="image/png")
	except:
		return render(request, 'generator/seconddegrepage.html', {'error':'Vous devez renter un nombre'})

def password(request):

	characters = list('abcdefghijklmnopqrstuvwxyz')

	if request.GET.get('uppercase'):
		characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')) #pour ajouter les capital a la liste
	if request.GET.get('numbers'):
		characters.extend(list('0123456789')) #pour ajouter les capital a la liste
	if request.GET.get('special'):
		characters.extend(list('!@#$%^&*()-_=+')) #pour ajouter les capital a la liste
	try:
		length = int(request.GET.get('length')) # pour donner la valeur choisi dans le selector, on vient chercher le name dans le tag select de home.html
											# si on met pas int 'str' object cannot be interpreted as an integer
		thepassword = ''

		for x in range(length):
			thepassword += stdlib_random.choice(characters)

		return render(request, 'generator/password.html', {'password':thepassword})
	except:
		return render(request, 'generator/about.html', {'error':'Vous devez renter un nombre'})

def prime(request):
	try:
		num = int(request.GET.get('num'))
		
		
		counter_prime = 0
		prime = 0
		#rac = int(num ** 0.5) + 1
		listprime = []
		for i in range(2,num):
			counter_prime = 0
			for x in range(2,i):
				if i%x == 0:
					counter_prime += 1
				else:
					counter_prime = counter_prime
			if counter_prime == 0:
				listprime.append(i)
				prime += 1
		# print(listprime)
		#return prime
		return render(request, 'generator/prime.html', {'test':listprime})
	except ValueError:
			return render(request, 'generator/primepage.html', {'error':'Vous devez renter un nombre'})


def base16(request):
	choix = request.GET.get('choix')
	if choix == '1':

		try:
			M = int(request.GET.get('num'))
			dico = dict([('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),('6', '6'), ('7', '7'), ('8', '8'),
		    ('9', '9'), ('10', 'A'), ('11', 'B'), ('12', 'C'), ('13', 'D'), ('14', 'E'),('15', 'F'), 
		    ])

			m = M
			base = 16
			x = 0
			if m <= base:
				x = 1
			else:
				while m >= base:
					m = M / (base ** x)
					if m > base:
						x += 1

			list16 = []
			for i in range(x,0,-1):
			    if i > 1:
			        d = M // base ** i
			        r = M % base ** i
			        list16.append(d)
			        M = r
			    else:
			        d = M // base ** i
			        r = M % base ** i
			        list16.append(d)
			        list16.append(r)
			       
			txt = ''
			for i in list16:
			    txt = txt + dico[str(i)]
			    
			txt = '0x' + txt
			return render(request, 'generator/base16.html', {'b16':txt})
		except ValueError:
				return render(request, 'generator/base16page.html', {'error':'Votre saisi contient un caractere non autorise'})
	else:
		dico = dict([('0', 0), ('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5),('6', 6), ('7', 7), ('8', 8),
		    ('9', 9), ('A', 10), ('B', 11), ('C', 12), ('D', 13), ('E', 14),('F', 15), ('a', 10), ('b', 11), 
		    ('c', 12), ('d', 13), ('e', 14),('f', 15),
		    ])

		M = request.GET.get('num')
		base = 16
		m = M
		x = []
		y = 0
		increment = 0

		for i in M:
		    if i in dico.keys():
		        i = dico[i]
		        x.append(i)
		    else:
		        return render(request, 'generator/base16page.html', {'error':'Votre saisi contient un caractere non autorise'})

		for i in x[::-1]:
		    y = y + i * base ** increment
		    increment += 1
		return render(request, 'generator/base16.html', {'b16':y})


def base2(request):
	choix = request.GET.get('choix')
	if choix == '1':

		try:
			M = int(request.GET.get('num'))
			dico = dict([('0', '0'), ('1', '1')])

			m = M
			base = 2
			x = 0
			if m <= base * 4:
				x = 3
			else:
				while m >= base:
					m = M / (base ** x)
					if m > base:
						x += 1

			print(x)
			list16 = []
			for i in range(x,0,-1):
			    if i > 1:
			        d = M // base ** i
			        r = M % base ** i
			        list16.append(d)
			        M = r
			    else:
			        d = M // base ** i
			        r = M % base ** i
			        list16.append(d)
			        list16.append(r)
			       
			txt = ''
			for i in list16:
			    txt = txt + dico[str(i)]
			    
			txt = '0b' + txt
			return render(request, 'generator/base2.html', {'b16':txt})
		except ValueError:
				return render(request, 'generator/base2page.html', {'error':'Votre saisi contient un caractere non autorise'})
	else:
		dico = dict([('0', 0), ('1', 1)])

		M = request.GET.get('num')
		base = 2
		m = M
		x = []
		y = 0
		increment = 0

		for i in M:
		    if i in dico.keys():
		        i = dico[i]
		        x.append(i)
		    else:
		        return render(request, 'generator/base2page.html', {'error':'Votre saisi contient un caractere non autorise'})

		for i in x[::-1]:
		    y = y + i * base ** increment
		    increment += 1
		return render(request, 'generator/base2.html', {'b16':y})

def factor(request):
	try:
		num = int(request.GET.get('num'))
		num2 = num
		counter_prime = 0
		prime = 0
		#rac = int(num ** 0.5) + 1
		listprime = []
		for i in range(2, num + 1):
		    counter_prime = 0
		    for x in range(2,i):
		        if i%x == 0:
		            counter_prime += 1
		        else:
		            counter_prime = counter_prime
		    if counter_prime == 0:
		        listprime.append(i)
		        prime += 1
		listprime = listprime[::-1] 

		x = 1
		y = num / 2
		for i in listprime[1:]:
		    if i > y:
		        listprime.pop(x)

		x = 0
		C=[0 for i in range(len(listprime))]
		for i in listprime:
		    if num % i != 0:
		        x += 1
		    else:
		        while num % i == 0:
		            num = num / i
		            C[x] = C[x] + 1
		        x += 1    
		#     if num % i == 0:

		phrase = ''
		x = 0
		for i in C:
		    if i != 0:
		        phrase = phrase + str(listprime[x]) + '^' + str(i) + ' x '
		    x+=1
		phrase = str(num2) + ' = ' + phrase     
		phrase = phrase[:-2]
		return render(request, 'generator/factor.html', {'phrase':phrase})
	except ValueError:
			return render(request, 'generator/factorpage.html', {'error':'Vous devez saisir un nombre'})

def fibo(request):
	try:
		num = int(request.GET.get('num'))
		a = 0
		b = 1
		c = []
		for x in range(0,num):
		    x = a + b
		    b = a
		    a = x
		    c.append(x)
		return render(request, 'generator/fibo.html', {'fibz':c})
	except:
		return render(request, 'generator/fibopage.html', {'error':'Vous devez renter un nombre'})

def romain(request):
	RO = ''
	try:
		x = int(request.GET.get('x'))
		# x = str(x)
		# a = len(x)

		# POUR LES MILLIER
		if x / 1000 > 1:
		    b = x // 1000
		    x = x % 1000
		    RO = 'M' * b

		# POUR LES CENTAINES    
		if x >= 900:
		    RO = RO + 'CM'
		    x = x - 900
		elif x >= 500:
		    x = x - 500
		    RO = RO + 'D'
		    b = x // 100
		    x = x - 100 * b
		    RO = RO + b * 'C'    
		    
		elif x >= 400:
		    RO = RO + 'CD'
		    x = x - 400
		else:
		    b = x // 100
		    x = x - 100 * b
		    RO = RO + b * 'C'

		# POUR LES DIZAINES
		if x >= 90:
		    RO = RO + 'XC'
		    x = x - 90
		elif x >= 50:
		    x = x - 50
		    RO = RO + 'L'
		    b = x // 10
		    x = x - 10 * b
		    RO = RO + b * 'X'
		elif x >= 40:
		    RO = RO + 'XL'
		    x = x - 40
		else:
		    b = x // 10
		    x = x - 10 * b
		    RO = RO + b * 'L'

		# POUR LES UNITES
		if x >= 9:
		    RO = RO + 'IX'
		elif x >= 8:
		    RO = RO + 'VIII'
		elif x >= 7:
		    RO = RO + 'VII'
		elif x >= 6:
		    RO = RO + 'VI'
		elif x >= 5:
		    RO = RO + 'V'
		elif x >= 4:
		    RO = RO + 'IV'
		    x = x - 4
		else:
		    b = x // 1
		    RO = RO + b * 'I'
		return render(request, 'generator/romain.html', {'ro':RO})
	except:
		return render(request, 'generator/romainpage.html', {'error':'Vous devez renter un nombre'})
