import face_recognition
import cv2
import numpy as np
import os
import pathlib
import dlib
import sys
#dlib.DLIB_USE_CUDA = True

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)


dir = os.path.join(os.getcwd(),'faces')
list = os.listdir(dir)
prevlen = len(list)




i = 0

video_capture = cv2.VideoCapture(0)

known_face_encodings = []
known_face_names = []




imgpath = os.path.join(os.getcwd(),'faces')

#print(imgpath)

for filename in os.listdir(imgpath) :
    #print(os.path.join(imgpath , filename))
    impath = os.path.join(imgpath , filename)
    image = face_recognition.load_image_file(impath)
    image_encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings.append(image_encoding)
    #print(known_face_encodings)
    temppath = filename
    tmp = os.path.splitext(temppath)
    #print(tmp)
    #print(tmp[0])
    known_face_names.append(tmp[0])
    #print(known_face_names)
    

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            print(matches)
            print(name)
            #if len(matches) != 0 :
            #    print ("Hi Jyo , Test Success")                
            #else :
            #    print("cant find jyo :(")

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            print("face dist :",face_distances)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)
            print("face name : ",face_names)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    #print("name again:",face_names)

########################################## Image Generator

    if len(face_names) != 0 :
        print("save to folder face")
        for face in face_names :
            path = os.getcwd()
            newpath = os.path.join(path,"detected",face)
            if not os.path.exists(newpath) :
                print("Creating path for ",face)
                os.mkdir(newpath)
            name = face + str(i) + ".jpg"
            i += 1
            facepath = os.path.join(newpath , name)
            print(" face path is : ",facepath)
            while os.path.isfile(facepath):
                i *= 1000
                break 

            cv2.imwrite(facepath , frame )
            

            
            

            print("path is :",newpath)

    
    dir = os.path.join(os.getcwd(),'faces')
    list = os.listdir(dir)
    curlen = len(list)
    if not prevlen == curlen :
        prevlen = curlen
        print("New files detected .... Restarting Script") 
        os.execv(sys.executable, ['python'] + sys.argv)
        

    #cv2.imwrite("testsuccess.jpg", frame)
    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()