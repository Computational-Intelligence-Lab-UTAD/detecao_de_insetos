# # -*- coding: utf-8 -*-
# """
# Created on Thu Dec  9 11:19:56 2021

# @author: accar
# """


import os
import pandas as pd

import cv2

# ########################
# #TREINO
# ########################

train_df = pd.read_csv('C:/accar/Desktop/Faster_percevejo/train/_annotations.csv')

with open("train_annotation.txt","w+") as f:

    for idx, row in train_df.iterrows():
        
        nome=str(row['filename'])
        #nome = nome.rstrip(".0")
        
        #path='train/'+str(nome) +'.jpg'
    
    
        width = int(row['width'])
        height = int(row['height'])
        x1 = int(row['xmin'])
        x2 = int(row['xmax'] )
        y1 = int(row['ymin'])
        y2 = int(row['ymax'] )
        
        google_colab_file_path = 'C:/accar/Desktop/Faster_percevejo/train/'
        
        #nome=int(float(nome))
        #nome=format(nome, '07')
   
        fileName = os.path.join(google_colab_file_path, nome)
        
        className = str(row['class'])
        className = className.rstrip(".0")
        
        #Só tens que substituir aqui a classe que queres manter 
        if className==str('percevejo')  :
            f.write(fileName  + ',' + str(x1) + ',' + str(y1) + ',' + str(x2) + ',' + str(y2) + ',' + className + '\n')
    f.close()
# ########################
# #Valid
# ########################

valid_df = pd.read_csv('C:/accar/Desktop/Faster_percevejo/_annotations.csv')

with open("valid_annotation.txt","w+") as f:

    for idx, row in valid_df.iterrows():
        
        nome=str(row['filename'])
        #nome = nome.rstrip(".0")
        
        #path='train/'+str(nome) +'.jpg'
    
    
        width = int(row['width'])
        height = int(row['height'])
        x1 = int(row['xmin'])
        x2 = int(row['xmax'] )
        y1 = int(row['ymin'])
        y2 = int(row['ymax'] )
        
        google_colab_file_path = 'C:/accar/Desktop/Faster_percevejo/train/'
        
        #nome=int(float(nome))
        #nome=format(nome, '07')
   
        fileName = os.path.join(google_colab_file_path, nome)
        
        className = str(row['class'])
        className = className.rstrip(".0")
        
        #Só tens que substituir aqui a classe que queres manter 
        if className==str('percevejo')  :
            f.write(fileName + ','  + str(x1) + ',' + str(y1) + ',' + str(x2) + ',' + str(y2) + ',' + className + '\n')
    f.close()
    
########################
#TESTE
########################

test_df = pd.read_csv('C:/accar/Desktop/Faster_percevejo/test/_annotations.csv')
# # For training
with open("test_class.txt","w+") as f:

    for idx, row in test_df.iterrows():
        
        
        nome=str(row['filename'])
        
        
        width = int(row['width'])
        height = int(row['height'])
        x1 = int(row['xmin'])
        x2 = int(row['xmax'] )
        y1 = int(row['ymin'])
        y2 = int(row['ymax'] )
        
        google_colab_file_path =  'C:/accar/Desktop/Faster_percevejo/train/test/'
        #nome=int(float(nome))
        #nome=format(nome, '07')
        
        
        fileName = os.path.join(google_colab_file_path, nome)
 
        className = str(row['class'])
        className = className.rstrip(".0")
        #Só tens que substituir aqui a classe que queres manter 
        if className==str('percevejo')  :
            f.write(fileName + ','  + str(x1) + ',' + str(y1) + ',' + str(x2) + ',' + str(y2) + ',' + className + '\n')
    
    f.close()