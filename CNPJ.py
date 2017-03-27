# -*- coding: utf-8 -*-

import requests
import json


class ConsultaCNPJ():
	'''	
	Main Functions:
			-> Validate CNPJ:							Checksum(CNPJ)
			-> Retrieve information from the compan 	newQuery(CNPJ_1, 'NPJ_2, CNPJ_3, ...)
			-> Return a masked CNPJ						maskedCNPJ(CNPJ)	
	'''


	def __init__(self):
		'''Nothing to be implemented on the constructor'''
		
		self.url = 'http://receitaws.com.br/v1/cnpj/{0}' 
		
	
	def clearCGC(self, CGC):
		
		result = CGC
		result.replace('.', '')
		result.replace('-', '')
		result.replace('/', '')
		
		return result
		
	
	def Checksum(self, cgc):
		'''Verify if CNPJ is valid'''
		
		CGC = self.clearCGC(cgc)
		
		if len(CGC) != 14:
			raise "CNPJ: Wrong amount of chars"
			return
		
		# valida se todos os caracteres sao iguais
		Counter = 0
		for char in range(len(CGC)):
			if CGC[0] == CGC[char]:
				Counter += 1
				if Counter == 14:
					raise "CNPJ: Execption found"
					return
		
		# Valida o primeiro digito
		soma = 0
		soma = soma + (int(CGC[0])*5)
		soma = soma + (int(CGC[1])*4)
		soma = soma + (int(CGC[2])*3)
		soma = soma + (int(CGC[3])*2)
		soma = soma + (int(CGC[4])*9)
		soma = soma + (int(CGC[5])*8)
		soma = soma + (int(CGC[6])*7)
		soma = soma + (int(CGC[7])*6)
		soma = soma + (int(CGC[8])*5)
		soma = soma + (int(CGC[9])*4)
		soma = soma + (int(CGC[10])*3)
		soma = soma + (int(CGC[11])*2)
		soma = soma % 11
		if soma < 2:
			soma = 0
		else:
			soma = 11 - soma
		if soma != int(CGC[12]):
			raise "CNPJ: First digit (%s) is incorrect: %d" % (CGC[12], soma)
			return
		
		# Valida o segundo digito
		soma = 0
		soma = soma + (int(CGC[0])*6)
		soma = soma + (int(CGC[1])*5)
		soma = soma + (int(CGC[2])*4)
		soma = soma + (int(CGC[3])*3)
		soma = soma + (int(CGC[4])*2)
		soma = soma + (int(CGC[5])*9)
		soma = soma + (int(CGC[6])*8)
		soma = soma + (int(CGC[7])*7)
		soma = soma + (int(CGC[8])*6)
		soma = soma + (int(CGC[9])*5)
		soma = soma + (int(CGC[10])*4)
		soma = soma + (int(CGC[11])*3)
		soma = soma + (int(CGC[12])*2)
		soma = soma % 11
		if soma < 2:
			soma = 0
		else:
			soma = 11 - soma
		if soma != int(CGC[13]):
			raise "CNPJ: Second digit (%s) is incorrect: %d" % (CGC[13], soma)
			return
		else:
			return True
	
	
	def maskedCNPJ(self, cgc):
		'''Return masked CNPJ'''
		
		CGC = self.clearCGC(cgc)
		
		if not self.Checksum(CGC):
			return
		
		masked  = CGC[0:2]  + '.'
		masked += CGC[2:5]  + '.'
		masked += CGC[5:8]  + '/'
		masked += CGC[8:12] + '-'
		masked += CGC[12:]
	
		return masked
	
	
	def newQuery(self, *cnpj):
		''' 
		Session var is the response from <newSession> method. 
		Dont use masked CNPJ on <cnpj>
		'''
		
		result = {}
		
		for item in cnpj:
			
			if self.Checksum(item):
				req  = requests.get(self.url.format(item))
				result[item] = json.loads(req.content)
			
			else:
				raise 'bad checksum for %s'
				return
			
		return result