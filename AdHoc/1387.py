# -*- coding: utf-8 -*-
 
while True:
     
    entrada = raw_input().split(" ")
     
    if entrada[0] == '0' and entrada[1] == '0':
        break
     
    print int(entrada[0])+int(entrada[1])