## Django Project 

This project is a creation of a simple template for django application. Contains GET and POST methods for API and the structure can be applied to other contexts.

### Installation

1. Virtual environment
   1. First a virtual environment must be created for the installation of the other packages that will be needed for the application. For this project the Intellij Community IDE will be used. 

2. Django Installation 
   1. To install the django framework it is necessary to use the command below
```
pip install django djangorestframework
```

3. Now the packages related to the API will be created inside the project folder, so be careful to type the following command inside the correct directory. This step is very important 
   1. Note: library can be renamed to a setup
```
django-admin startproject library .
```

4. The next step is to install the application inside the created folder, one API can have many applications, in this case, it is going to be called Registration, since it will simulate a data registration 
```
django-admin startapp registration
```

At this point it is possible to start the application using the command
```
python manage.py runserver
```


