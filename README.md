# Voice Enabled Facial Recognition System

A Voice Activated Facial Recognition Software using OpenFace (trained network) and dlib libraries [Machine Learning on OpenCV] , this system makes use of the HOG method to convert pictures to a readable black and white format and it stores a binary encoding of detectable faces (eyes, ears, nose encodings) and by training a deep convolutional neural network – generating 128 measurements for each detectedface, the algorithm is able to classify the closeness between the measurements of the stored face and detected face in order to accurately perform facial recognition on different faces and it distinguishes between them which can be
used for recognizing individuals and then logging in the recognized user’s data upon mention of the wake command (using speech recognition) as well as the
timestamp at which face was recognized on to a database – this software could be used in colleges for attendance logging in the cloud, which makes it easier for teachers.

The Project Has Not Been Deployed It. 

## To Do :
* Deploy Project with Useable UI designed with flask/Streamlit
* Develop API to log recognized user's data on database smoothly 
* Integrate mongoDB for storing user data
* ~~Integrate wake commands~~ 
* Add User Authentication With SQL
* Find Solution For better matching sequences
