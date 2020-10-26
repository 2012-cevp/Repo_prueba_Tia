#Visualización con opencv y reconocimiento de caras 
import numpy as np 
import matplotlib.pyplot as plt
import cv2 

cascada_cara = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')

#Creando una función donde pasaremos una imagen 
def detectar_cara(imagen):
    imagen1 = imagen.copy()
    rectangulos = cascada_cara.detectMultiScale(imagen1)
    for (x,y,w,h) in rectangulos:
        cv2.rectangle(imagen1,(x,y),(x+w,y+h),(255,200,0),10)
        return imagen1
    
capturar = cv2.VideoCapture(0)

while True:
    res,video = capturar.read(0)
    video = detectar_cara(video)
    cv2.imshow('Detectar cara en video', video)
    tecla = cv2.waitKey(1)
    if tecla ==27: #Tecla esc
        break
capturar.release()
cv2.destroyAllWindows 