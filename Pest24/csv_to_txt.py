# # -*- coding: utf-8 -*-
# """
# Created on Thu Dec  9 11:19:56 2021

# @author: accar
# """


import os
import pandas as pd

import cv2

########################
#TREINO
########################

train_df = pd.read_csv('C:/Users/accar/Desktop/train2/train/_annotations.csv')

with open("train_annotation.txt","w+") as f:

    for idx, row in train_df.iterrows():
        
        nome=str(row['filename'])
        
    
    
        width = int(row['width'])
        height = int(row['height'])
        x1 = int(row['xmin'])
        x2 = int(row['xmax'] )
        y1 = int(row['ymin'])
        y2 = int(row['ymax'] )
        
        google_colab_file_path = 'drive/My Drive/Faster/train/'
        
   
        fileName = os.path.join(google_colab_file_path, nome)
        
        className = str(row['class'])
        
        
        f.write(fileName  + ',' + str(x1) + ',' + str(y1) + ',' + str(x2) + ',' + str(y2) + ',' + className + '\n')
    f.close()
# # ########################
# # #Valid
# # ########################

valid_df = pd.read_csv('C:/Dissertacao/Resultados/Pest24/Faster/valid/_annotations.csv')

with open("valid_annotation.txt","w+") as f:

    for idx, row in valid_df.iterrows():
        
        nome=str(row['filename'])
        
    
    
        width = int(row['width'])
        height = int(row['height'])
        x1 = int(row['xmin'])
        x2 = int(row['xmax'] )
        y1 = int(row['ymin'])
        y2 = int(row['ymax'] )
        
        google_colab_file_path = 'drive/My Drive/Faster/train/'
        
   
        fileName = os.path.join(google_colab_file_path, nome)
        
        className = str(row['class'])
        
        
        f.write(fileName + ','  + str(x1) + ',' + str(y1) + ',' + str(x2) + ',' + str(y2) + ',' + className + '\n')
    f.close()
    
#######################
#TESTE
#######################

test_df = pd.read_csv('C:/Dissertacao/Resultados/Pest24/Faster/TEST_annotations.csv')
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
        
        google_colab_file_path =  'drive/My Drive/Faster/test/'
        
        
        
        fileName = os.path.join(google_colab_file_path, nome)
 
        className = str(row['class'])
        
        
        f.write(fileName + ','  + str(x1) + ',' + str(y1) + ',' + str(x2) + ',' + str(y2) + ',' + className + '\n')
    
    f.close()