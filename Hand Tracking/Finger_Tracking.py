#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# Initializing the position as a (0,0) tuple, and Finger_Name as empty string. 
position_T,position_B,position_R,position_M,position_I= (0,0),(0,0),(0,0),(0,0),(0,0)
fingerName_T,fingerName_B,fingerName_R,fingerName_M,fingerName_I= ' ',' ',' ',' ',' '

# For webcam input:
cap = cv2.VideoCapture(0)
out = cv2.VideoWriter('output_1.mp4', -1, 20.0, (640,480))

# Initializing the Model:
with mp_hands.Hands(static_image_mode=False,model_complexity=1,min_detection_confidence=0.75,min_tracking_confidence=0.75,max_num_hands=2) as hands:
    
    while cap.isOpened():
        success, image = cap.read()
        #print('success',success)
        #print('image',image)
        width  = cap.get(3)  # float width of the displayed screen.
        height = cap.get(4)  # float height of the displayed screen.

        out.write(image)
        # To improve performance, optionally mark the image as not writeable topass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Get hand index to check label
                handIndex = results.multi_hand_landmarks.index(hand_landmarks)
                handLabel = results.multi_handedness[handIndex].classification[0].label
                
                # Set variable to keep landmarks positions (x and y)
                handLandmarks = []

                # Fill list with x and y positions of each landmark
                for landmarks in hand_landmarks.landmark:
                    handLandmarks.append([landmarks.x, landmarks.y])

                # Other fingers: TIP y position must be lower than PIP y position, as image origin is in the upper left corner.
                if handLandmarks[8][1] < handLandmarks[6][1]:     # Index finger
                    position_I=( int(handLandmarks[8][0]*width),int(handLandmarks[8][1]*height) ) # setting the position of Index finger 
                    fingerName_I ='I' # setting 'I' for Index finger
                    
                if handLandmarks[12][1] < handLandmarks[10][1]:   # Middle finger
                    position_M=( int(handLandmarks[12][0]*width),int(handLandmarks[12][1]*height) ) # setting the position of Middle finger
                    fingerName_M = 'M' # setting 'M' for Middle finger
                   
                if handLandmarks[16][1] < handLandmarks[14][1]:   # Ring finger
                    position_R=( int(handLandmarks[16][0]*width),int(handLandmarks[16][1]*height) ) # setting the position of Ring finger
                    fingerName_R = 'R' # setting 'R' for Ring finger
                    
                if handLandmarks[20][1] < handLandmarks[18][1]:   # Baby finger
                    position_B=( int(handLandmarks[20][0]*width),int(handLandmarks[20][1]*height) ) # setting the position of Baby finger
                    fingerName_B = 'B' # setting 'B' for Baby finger
                    
                if handLandmarks[4][1] < handLandmarks[3][1]:     # Thumb
                    position_T=( int(handLandmarks[4][0]*width),int(handLandmarks[4][1]*height) ) # setting the position of Thumb
                    fingerName_T = 'T' # setting 'T' for Thumb

                # Draw hand landmarks 
                mp_drawing.draw_landmarks(image, hand_landmarks,mp_hands.HAND_CONNECTIONS,mp_drawing_styles.get_default_hand_landmarks_style(), mp_drawing_styles.get_default_hand_connections_style())

            # Display finger name.
            cv2.putText(image, str(fingerName_I), position_I, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
            cv2.putText(image, str(fingerName_M), position_M, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
            cv2.putText(image, str(fingerName_R), position_R, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
            cv2.putText(image, str(fingerName_B), position_B, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
            cv2.putText(image, str(fingerName_T), position_T, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
            
            fingerName_T,fingerName_B,fingerName_R,fingerName_M,fingerName_I= ' ',' ',' ',' ',' ' # setting Finger_Name to empty string for next iteration.
            out.write(image)
        
        # Display image
        
        cv2.imshow('Finger_Tracking', image)
        #out.write(image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
out.release()
cv2.destroyAllWindows()        

