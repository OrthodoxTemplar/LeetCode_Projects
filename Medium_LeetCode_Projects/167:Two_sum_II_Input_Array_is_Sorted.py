#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 07:57:40 2022

@author: alexandre
"""

import math

def twoSum(numbers, target):
        
        list_index = list()
        
        n = len(numbers)
        
        max_iter = int(math.log2(n))
        
        print("max_iter", max_iter)
        
        somme = 0
        
        if n>6:
            
            for i in range(n):
                
                somme = numbers[i]
                
                if somme+numbers[-1]<target:
                    
                    continue
                    
                elif somme + numbers[-1] == target:
                    
                    list_index.extend([i+1, n])
                    
                    return list_index
                
                elif somme + numbers[-1]>target:
                    
                    j = 1
                    
                    index = 1
                    
                    while j<max_iter:
                        
                        somme = numbers[i]
                        
                        somme+= numbers[index]
                        
                        print("somme", somme)
                        
                        if somme < target:
                            
                            index = min(index + n//(2**j), n-1)
                            
                        elif somme>target:
                            
                            index = max(index - n//(2**j),0)
                            
                        elif somme==target:
                            
                            list_index.extend([i+1, index+1])
                            
                            return list_index
                        
                        j+=1
                        
                        print(index)
                        
                count = 1
                
                while count<5:
                    
                    somme = numbers[i]
                    
                    if somme+numbers[index]<target:
                        
                        index = min(index+1, n-1)
                        
                    elif somme+numbers[index]==target:
                        
                        print("Got it!")
                        
                        print("index",index)
                        
                        list_index.extend([i+1, index+1])
                        
                        return list_index
                    
                    elif somme+numbers[index]>target:
                        
                        index = max(index-1,0)
                        
                    count+=1
          
        else:

        
            for i in range(n):

                somme = numbers[i]

                #print(somme)

                if i<n-1:

                    for j in range(i+1, n):

                        somme = numbers[i]

                        somme+=numbers[j]

                        #print("after",somme)

                        if somme==target:

                            list_index.extend([i+1, j+1])

                            return list_index

                elif i==n-1:

                    continue
                    
        return list_index
    
s1 = [2,3,4], 6
s2 = [3,24,50,79,88,150,345], 200
s3 = [1,2,3,4,4,9,56,90], 8 #True:[4,5] Pour ce probl??me on peut demander ?? l'algo de
# continuer si i==index.

"""Dans ce cas, pour les valeurs de n qui sont grandes, n>5, il faut sauter directement ?? l'autre moitit?? de l'array consid??r?? et v??rifier si l'??l??ment sur lequel on tombe est sup??rieur ?? la diff??rence
        entre target et l'??element 1. Si c'est pas le cas, on fait le m??me processus vers la droite, 
        et si c'est le cas, on va vers la gauche. Le nombre de sauts sera ??gal ?? max_iter = log2(n).
        Apr??s, on incr??mentera un par un la recherche puisqu'on sera tout pr??s."
        
        On peut directement tester si un nombre de d??part est potentiel candidat en faisant la somme de cenombre avec le dernier ??l??ment de la liste. Si la somme est inf??rieure ?? target,
        on passe directement au suivant et on ne s'int??resse qu'?? ceux dont la somme est sup??rieure ou ??gale ?? target."""
                