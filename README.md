# Face-Recognition-for-CCTV-with-one-shot-learning
This a project for uploading the image of a person to the server and finding that person's image in the CCTV live feed.

This work is heavely based on the Python Face Recognition Library :

https://pypi.org/project/face_recognition/ && https://github.com/ageitgey/face_recognition

Instruction to Install :

Download and setup python3 and add to path.

To Install DLIB , First Install Microsoft Visual Studio Community and install CMAKE

Then Goto to the extracted project location using CMD or Shell and execute pip install -r requirements.txt

To just run the Face Recogntion Script , Run cctv.py

If you want to run the Face Recognition Script along with the Database and server (I've Used Laragon Here) just execute main_script.bat (Username and password of testing database is both "root")


To run the whole thing :

1:  Properly initiate the server connection in addtodb.php and addtodb.py
2: Start the server
3: run cctv.py and dbupdater.py parallely



