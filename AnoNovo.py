"""This module provides a completely unuseful function to the New Year Eve (unless that you want to have a Python party) and another so simple as more convenient.
The two functions named in Portuguese isn't mine, they can't be just yours too, because they are from time
	"""
from time import localtime as agora, sleep as esperar, struct_time as momento

anoNovo = [31, 12]	# (Dia, Mês) da Virada

def bissextile (ano=agora().tm_year):
	"""bissextile([year]) -> bool
	
Retorn if the year is bissextile according to the Gregorian calendar. If it isn't, returns too, but the other boolean value.
When 'year' is not passed in, use the current year."""
	return ano%400==0 or (ano%4==0 and ano%100!=0)

def newYear ():
	"""newYear() -> str
	Wait for the New Year Eve last 10 seconds to return a short message in Portuguese....
"""
	while (True):
		if (agora().tm_mon==anoNovo[1] and agora().tm_mday==anoNovo[0]
			and agora().tm_hour==23 and agora().tm_min==59):
			if(60-agora().tm_sec<=10):	# contagem regressiva
				print(60-agora().tm_sec)
		
		if (agora().tm_mon==1 and agora().tm_mday==1
			and agora().tm_hour==0 and agora().tm_min==0):
			a = 'FELIZ ANO NOVO !!!'
			print(a + (" ", '!')[bissextile()], end = "\t\a")
			return a

		try:
			esperar (1)
		except KeyboardInterrupt: #comentários inseridos em linhas estratégicas explicando o que é óbvio
			return 'ADEUS ANO VELHO !!' + ("!", '\a')[bissextile()]


if __name__ == "__main__":
	print ('\t'+str(agora().tm_year)+'\a\n')
	#Happy!
	newYear ()

"""isso foi só para dar 42 linhas mesmo!"""