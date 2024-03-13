# code fait à partir du code de Murtaza's Workshop - Robotics and AI 
import cv2
import mediapipe as mp
import time
import ClassHandTrackingModule as htm
import math
#from djitellopy import Tello

def main():
    #Initialisation de la résolution de l'écran et des variables
    wCam, hCam = 1280, 720
    print(f"Résolution de la de l'écran : {wCam}x{hCam}")
    length = 0
    
    #Initialisation du détecteur de mains
    detector = htm.handDetector(detectionCon=0)
    cTime = 0
    pTime = 0
    
    #Initialisation de la capture vidéo
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
    
    color = (0, 255, 0)
    x3= 640
    y3 = 360
    # Connexion au drone Tello
    #tello = Tello()
    #tello.connect()

    #tello.takeoff()
    
    while True:
        #Lecture de la vidéo et détection des mains
        success, img = cap.read()
        img = detector.findHands(img)
        landmark_list = detector.findPosition(img, draw=False)

        if len(landmark_list):
         
            #Extraction des points clés pour calculer la longueur entre le pouce et l'index
           # x1, y1 = landmark_list[8][1], landmark_list[8][2] #L'index
            x2, y2 = landmark_list[9][1], landmark_list[9][2] #Millieu du majeur
           # x3, y3 = landmark_list[20][1], landmark_list[20][2] #L'auriculaire
          
            cx, cy = (wCam - x2) , (hCam - y2)
            vx = -(50 - ((cx / 1280) * 100)) 
            vy = -(50 - ((cy / 720) * 100)) 
            length = math.hypot(x2 - x3, y2 - y3)

            #Dessine des points et la ligne entre le pouce et l'index
            #cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x3, y3), 5, color, cv2.FILLED)
            cv2.line(img, (x3, y3), (x2, y2), (255, 0, 0), 2)
            #cv2.circle(img, (x3, y3), 10, (255, 0, 255), cv2.FILLED)
            
            #tello.send_rc_control(int(vx), int(vy), 0, 0)  # Avancer/Reculer
            #tello.send_rc_control(int(vx), 0, 0, 0)  # Aller à gauche/droite
            #print(landmark_list[9]) #landmark_list[8], landmark_list[20]
            #print(length)
            #print(cx,cy)
            #print(vx,vy)
            
        #Calcul du FPS
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        #Retournement de l'image
        flipped = cv2.flip(img, 2)

        #Changement de taille d'écriture FPS
        cv2.putText(flipped, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 100), 2)

        #Affichage de l'image
        cv2.imshow("image", flipped)

         
        #Quitter la boucle si la touche 'q' est enfoncé
        if cv2.waitKey(1) & 0xFF == ord('q'):
            #tello.land()
            break

    #Sortie de la programmation
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
