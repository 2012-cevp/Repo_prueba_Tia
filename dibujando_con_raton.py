import numpy as np 
import cv2

#Definimos la funcion con la cual dibujaremos con el raton
#Aquí le decimos que dibujara un circulo dentro de los parametros que le hemos dado
def dibujar(event,x,y,etiquetas, parametros):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(imagen,(x,y),50, color=(200,100,255))
        
#Conectando imagen con la funcion
#Le ponemos primero el nombre de la ventana
cv2.namedWindow(winname='Imagen_dibujada_con_raton')
#Aquí le decimos que cuando el mouse pase por encima de la imagen entonces llamara a la funcion dibujar
cv2.setMouseCallback('Imagen_dibujada_con_raton',dibujar)
    
#Mostrando la imagen donde dibujaremos
imagen = np.ones((500,300,3), np.int8)

while True:
    #Creamos el nombre de la imagen y luego con el waitKey agregamos los milisegundos que espera y que cuando presione
    #La tecla 27 del codigo ASCII(ESC) se cerrara la ventana
    cv2.imshow('Imagen_dibujada_con_raton',imagen)
    if cv2.waitKey(5) & 0XFF == 27:
        break
    
cv2.destroyAllWindows()