#!/usr/bin/env python3
from unidecode import unidecode

import string
import matplotlib.pyplot as plt

# help functin
alphabet = list(string.ascii_lowercase)

# french word distribution
# https://fr.wikipedia.org/wiki/Fr%C3%A9quence_d%27apparition_des_lettres
freq = []
freq.append(["e",12.1])
freq.append(["a",7.11])
freq.append(["i",6.59])
freq.append(["s",6.51])
freq.append(["n",6.39])
freq.append(["r",6.07])
freq.append(["t",5.92])
freq.append(["o",5.02])
freq.append(["l",4.96])
freq.append(["u",4.49])
freq.append(["d",3.67])
freq.append(["c",3.18])
freq.append(["m",2.62])
freq.append(["p",2.49])
freq.append(["g",1.23])
freq.append(["b",1.14])
freq.append(["v",1.11])
freq.append(["h",1.11])
freq.append(["f",1.11])
freq.append(["q",0.65])
freq.append(["y",0.46])
freq.append(["x",0.38])
freq.append(["j",0.34])
freq.append(["k",0.29])
freq.append(["w",0.17])
freq.append(["z",0.15])

def clear_on_the_fly():
    f = open("cipher.txt", "r")
    txt = ""
    for x in f:
        txt = txt + x.replace("\n","")
    
    explore_dico = {}
    explore_dico[" "] = " "
    explore_dico["v"] = "e" 
    explore_dico["c"] = "a"  
    explore_dico["j"] = "s" 
    explore_dico["d"] = "i" 
    explore_dico["e"] = "t" 
    explore_dico["w"] = "n"      
    explore_dico["m"] = "r" 
    explore_dico["y"] = "u" 
    explore_dico["n"] = "l"    
    explore_dico["b"] = "o" 
    explore_dico["a"] = "d"         
    explore_dico["t"] = "m" 
    explore_dico["h"] = "p" 
    explore_dico["g"] = "c"  
    explore_dico["r"] = "v"
    explore_dico["z"] = "b"   
    explore_dico["q"] = "g" 
    explore_dico["x"] = "f"
    explore_dico["p"] = "q" 
    explore_dico["s"] = "h"
    explore_dico["f"] = "j"
    explore_dico["o"] = "x"
    explore_dico["k"] = "y"
    explore_dico["l"] = "k"
    explore_dico["u"] = "w"
    explore_dico["i"] = "z"
    # add more letters here and explore :)
    
    clear = ""
    for c in (txt):
        if c in explore_dico.keys():
            clear = clear + explore_dico[c]
        else:
            clear = clear + "-"
    print(clear)
    f.close()
    

def main():
    clear_on_the_fly()

main()