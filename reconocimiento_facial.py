from cv2 import cv2
import face_recognition as fr

# Cargar Imagenes

foto_control = fr.load_image_file('FotoA.jpeg')
foto_prueba = fr.load_image_file('FotoB.jpg')

foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)