# -*- coding: utf-8 -*-

import requests
import json

class ConsultaCNPJ():

	def __init__(self):
		'''Nothing to be implemented on the constructor'''
		
		self.url = 'http://receitaws.com.br/v1/cnpj/{0}' 
		
	
	def Checksum(self, cnpj):
		'''To be implemented'''
		
		return True
		
	
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