# Facial-Recognition

Requirements for this application:
==================================
1. Webcam(embedded/external) on your machine.
2. OpenCV(cv2) module installed on your Python Idle.

Steps for executing this application:
=====================================
1. Create two folders with names 'dataset' and 'trainner'
2. Execute the dataset.py file keeping the face to be recognized in front of webcam. It will ask for an Id.
Enter an id and remember it. This will create samples of the face with the given Id.
3. Execute the trainner.py. This will create a .yml file in the trainner folder.
4. As per the Id you gave in step 2 make changes in the FaceRecognize.py file. e.g: Id-1 was for Aakash.
5. Now execute the file. The output screen should recognize the face
