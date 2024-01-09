import cv2
import face_recognition

#load the first image
image1 = cv2.imread(r'C:\Users\edwar\OneDrive\Pictures\facerecognition\manwithtablet.jpg')

#load the second image
image2 = cv2.imread(r'C:\Users\edwar\OneDrive\Pictures\facerecognition\groupofpeople.jpg')

#find face encodings using face_recognition
face_encoding1 = face_recognition.face_encodings(image1)[0]
face_encoding2 = face_recognition.face_encodings(image2)[0]

#compare face encodings
results = face_recognition.compare_faces([face_encoding1], face_encoding2)

if results[0]:
    print("The face from Image 1 is present in Image 2.")
else:
    print("The face from Image 1 is not present in Image 2.")

#display the images
cv2.imshow('People - Image 1', image1)
cv2.imshow('People - Image 2', image2)

cv2.waitKey(0)
cv2.destroyAllWindows()
