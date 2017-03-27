#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from CNPJ import ConsultaCNPJ
import os

# Onde gerar o PNG
folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/')
file   = os.path.join(folder, 'image.png')

# Instancia uma sessao
Sessao = ConsultaCNPJ()
Resposta, Imagem = Sessao.newSession()

# Gera um PNG do captcha
if os.path.exists(folder):
    fp = open(file, 'wb')
    fp.write(Imagem)
    fp.close()
    
# Faz uma consulta
#cnpj    = input('CNPJ: ')
cnpj    = '81591786000160' 
captcha = input('Captcha: ')

# Faz uma consulta
consulta = Sessao.newQuery(Resposta, cnpj, captcha)
print(consulta) 
