## Face-Recognition-for-CCTV-with-one-shot-learning
This project works by uploading the image of a person to the server and finding that person's image in the CCTV live feed.

### Instruction to Install :

1. Download and setup python3 and add to path. <br/>
1. To Install DLIB , First Install Microsoft Visual Studio Community and install CMAKE <br/>
1. Then Goto to the extracted project location using CMD or Shell and execute pip install -r requirements.txt <br/>
1. To just run the Face Recogntion Script , Run cctv.py <br/>

If you want to run the Face Recognition Script along with the Database and server (I've Used Laragon Here) just execute main_script.bat (Username and password of testing database is both "root")


### To execute the program :

1.  Initiate the server connection using addtodb.php and addtodb.py. <br/>
1. Start the server <br/>
1. run cctv.py and dbupdater.py parallely <br/>

#### Thanks to :
https://github.com/ageitgey/face_recognition

