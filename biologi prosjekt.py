# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 16:38:51 2017

@author: Kristoffer
"""

from pylab import *

fil = open("DNA.txt","r")
fil.readline()
#streng=fil.read()
Linje = []
DNA = []
RNA = []
kodon = []
amino = []
aminosyre=0

for rad in fil:
    Linje.append(rad)
    
fil.close()
#print(DNA)
#print(streng)
"""
for rad in DNA:
    for bokstav in rad:
        print(bokstav + "\n")
"""
a=0
#while a<7
for rad in Linje:
    for bokstav in rad:
        if bokstav == "<":      #fjerner teksten
            fil.readline()
            DNA.append("NY")
            print(a)
            a=0
        elif bokstav == "A" or bokstav == "T" or bokstav == "G" or bokstav == "C": #or bokstav == "a" or bokstav == "t" or bokstav == "g" or bokstav == "c":
            DNA.append(bokstav)
            a+=1
print(DNA)
            
for i in DNA:
    if i=="A":
        RNA.append("U")
    elif i=="G":
        RNA.append("C")
    elif i=="T":
        RNA.append("A")
    elif i=="C":
        RNA.append("G")
    elif i=="NY":
        RNA.append("NY")
        
    
print(RNA)        
for j in range(2,len(RNA),3):
    kodon.append(RNA[j-2]+RNA[j-1]+RNA[j])
  #  del RNA[j+1]
  #  del RNA[j+2]
   # print(j)
print(kodon)   
   
for kodon in kodon:
    if kodon == "UUU" or kodon == "UUC":
        aminosyre = "Fenylalanin"
    elif kodon == "UUA" or kodon == "UUG" or kodon == "CUU" or kodon == "CUC" or kodon == "CUA" or kodon == "CUG":
        aminosyre = "Leucin"
    elif kodon == "UCU" or kodon == "UCC" or kodon == "UCA" or kodon == "UCG":
        aminosyre = "Serin"
    elif kodon == "UAU" or kodon == "UAC" or kodon == "AGU" or kodon == "AGC":
        aminosyre = "Tyrosin"
    elif kodon == "UAA" or kodon == "UAG" or kodon == "UGA":
        aminosyre = "==========================================STOPP======================================"
    elif kodon == "UGU" or kodon == "UGC":
        aminosyre = "Cystein"
    elif kodon == "UGG":
        aminosyre = "Tryptofan"
    elif kodon == "CCU" or kodon == "CCC" or kodon == "CCA" or kodon == "CCG":
        aminosyre = "Prolin"
    elif kodon == "CAU" or kodon == "CAC":
        aminosyre = "Histidin"
    elif kodon == "CAA" or kodon == "CAG" or kodon == "GAA" or kodon == "GAG":
        aminosyre = "Glutamin"
    elif kodon == "CGU" or kodon == "CGC" or kodon == "CGA" or kodon == "CGG" or kodon == "AGA" or kodon == "AGG":
        aminosyre = "Arginin"
    elif kodon == "AUU" or kodon == "AUC" or kodon == "AUA":
        aminosyre = "Isoleucin"
    elif kodon == "AUG":
        aminosyre = "Metionin"
    elif kodon == "ACU" or kodon == "ACC" or kodon == "ACA" or kodon == "ACG":
        aminosyre = "Treonin"
    elif kodon == "AAU" or kodon == "AAC":
        aminosyre = "Aspargin"
    elif kodon == "AAA" or kodon == "AAG":
        aminosyre = "Lysin"
    elif kodon == "GUU" or kodon == "GUC" or kodon == "GUA" or kodon == "GUG":
        aminosyre = "Valin"
    elif kodon == "GCU" or kodon == "GCC" or kodon == "GCA" or kodon == "GCG":
        aminosyre = "Alanin"
    elif kodon == "GAU" or kodon == "GAC":
        aminosyre = "Asparaginsyre"
    elif kodon == "GGU" or kodon == "GGC" or kodon == "GGA" or kodon == "GGG":
        aminosyre = "Glysin"
    amino.append(aminosyre)
    
    
print(amino)