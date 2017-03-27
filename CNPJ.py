# -*- coding: utf-8 -*-

import requests
import os
from bs4 import BeautifulSoup

class ConsultaCNPJ():

	def __init__(self):
		'''
		Nothing to be implemented on the constructor
		'''
		
		self.url = 'http://www.receita.fazenda.gov.br/PessoaJuridica/CNPJ/cnpjreva/' 
		
	def newSession(self):

		session  = requests.session()
		request  = session.get(self.url + '/cnpjreva_solicitacao2.asp')
		parser   = BeautifulSoup(request.text, 'html.parser')
		img_src  = parser.find(id='imgCaptcha')['src']
		png      = session.get(self.url + img_src)

		return (session, png.content)

	def newQuery(self, session, cnpj, captcha):
		''' 
		Session var is the response from <newSession> method. 
		Dont use masked CNPJ on <cnpj>
		'''
	
		page = self.url + '/valida.asp'
		payload = {
				'origem': 'comprovante',
				'cnpj': cnpj,
				'txtTexto_captcha_serpro_gov_br': captcha,
			}
		response = session.post(page, data=payload)
		print(response)
		return response.content
	