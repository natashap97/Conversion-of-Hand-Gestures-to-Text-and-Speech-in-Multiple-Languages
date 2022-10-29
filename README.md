# Conversion-of-Hand-Gestures-to-Text-and-Speech-in-Multiple-Languages
INSTALLATION OF SOFTWARE AND PACKAGES:

1.In order to install all the packages first install Pythonv3.6.5
2.Install pip v19.1
3.Install all packages with command: pip3 install -r requirments.txt
4.Install the latest version of Django

PREPROCESSING OF AN IMAGE:

In order to preprocess the image run the follwing command in the Alphabet directory:
python3 feature_extract.py

TRAINING OF MODEL:

In order to train the alphabet model(A-Z) run the following command in the Alphabet directory:
python3 cnn_model.py

In order to train the Colloquial model(4 gestures) run the following command in the Alphabet directory:
python3 cnn_model.py

FRONT END:

To run the front end website and predict gestures go to the directory /Alphabets/myproject and run the following command:
python3 manage.py runserver
An IP adress will be generated. Paste that address on your browser and predict gestures both in real time and dynamic time.
