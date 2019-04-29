# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 16:04:23 2019

@author: Reborn
"""

# -*- coding:utf-8 -*-
import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import collections
from collections import OrderedDict
from matplotlib import pyplot as plt

def textmetrics():

    local=input(u'Digite o caminho para a pasta onde está seu arquivo de texto :')

    corpus_root=(str(local))

    wordlists=PlaintextCorpusReader(corpus_root,'.*')

    nomes=wordlists.fileids()

    print ("")
    print ("Arquivos de Texto Encontrados:")
    print (nomes)
    print ("")

    escolha=input("Escolha o arquivo que quer pesquisar :")

    print ("")
    u=open(local+'\\'+escolha,'rb').read().decode('latin-1')

    t=nltk.word_tokenize(u)
    tokens=len(t)
    tokensunicos=len(set(t))
    diver=tokens/tokensunicos   
    print (u"Número de tokens no texto: " + str(tokens))
    print (u"Número de tokens ùnicos no texto: " + str(tokensunicos))
    print (u"Diversidade Léxica: " + str(float(diver)))
    palavras=[]
    for i in range(len(t)):
        if t[i].isalpha():
            trans=t[i].lower()
            if len(trans)>1 and trans not in stopwords.words('portuguese'):
                palavras.append(trans)

    fdist1=FreqDist(palavras)
    vocab=(fdist1.items())
    vocab1=sorted([(tpl[1],tpl) for tpl in vocab],reverse=True)
    vocab2=OrderedDict([tpl[1] for tpl in vocab1])
    print('Lista das 50 palavras mais frequentes: ')
    print(list(vocab2)[:50])
    
    fdist1.plot(50,title=u'Distribuição de Frequencia (50 mais comuns):')
    
    
    
    
    
  
   

    
 

    
              
 
    



textmetrics()
