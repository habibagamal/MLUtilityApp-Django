# What is this?
This is a machine learning utility application that predicts whether a loan will default of not, based on user-input data that is filled through a form in a client application. 

# Archticture
Client-Server Architecture. 
The prediction runs on the server side and the GUI is on the client side. The client-server application is achieved using Django. 
The application is built using Python. 

# Model
The application is built using decision trees as the supervised learning model. We pre-trained the model, and the new predictions are made based on the tranining data. You can find the model in ./webapp/model.py
