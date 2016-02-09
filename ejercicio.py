#!/usr/bin/python
# -*- coding: utf-8 -*-

fichero_pass = open ('/etc/passwd')
linea = fichero_pass.readline
diccionario = {}
for linea in fichero_pass :
	lista = linea.split(":")
	diccionario[lista[0]] = lista [-1][:-1]

try : 
	print diccionario["root"]
	print diccionario["imaginario"]

except : 
	
	print "Usuario no encontrado"