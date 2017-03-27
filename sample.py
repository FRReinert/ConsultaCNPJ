#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from CNPJ import ConsultaCNPJ
import os

# Query some company
query = ConsultaCNPJ()
data  = query.newQuery('33592510000154', '02916265000160')

# print data
for cnpj, dados in data.items():
    
    print('\n\n\nConsulta para %s' % cnpj)
    
    for atributos, valores in dados.items():
        
        if isinstance(valores, list):
            
            print('%s' % atributos)
            
            for item in valores:
       
                for Codigo, Texto in item.items():
                    
                    print('    %s: %s' % (Codigo, Texto))
        
        else:
            
            print('%s: %s' % (atributos, valores))



