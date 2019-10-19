#!/usr/bin/env python
# -*- coding: utf-8 -*-
''''
	• Tempo de retorno médio – Refere-se ao tempo transcorrido entre o momento da
entrada do processo no sistema e o seu término.
	• Tempo de resposta médio – Intervalo de tempo entre a chegada do processo e o início
de sua execução.
	• Tempo de espera médio – Soma dos períodos em que um processo estava no seu
estado pronto.
'''
import sys
from py_memory import *
from secondChance import *
from greatAlg import *

def crt_l_pag(data):
	l_pag = []
	for x in data:
		l_pag.append(Page(x)) #cria uma pagina por loop
	return l_pag	

def main():
	n_Frame = sys.stdin.readline() #cria a memoria com seu tamanho
	pg = sys.stdin.readlines()
	mem1 = Memory(n_Frame)
	mem2 = Memory(n_Frame)
	pg1 = crt_l_pag(pg)
	pg2 = crt_l_pag(pg)

	sc = SecondChance()
	f_sc = sc.work(mem1, pg1)
	print(f_sc)

	otm = GreatAlg()
	f_otm = otm.work(mem2, pg2)
	print(f_otm)


if __name__ == '__main__':
    main()