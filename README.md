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

### Configuration

Django by default creates a MySQL database. To finish configuring this part of the project, some settings are required. First, a database migration is requested so that some standard tables are created
```
python manage.py migrate 
```

#### File: settings.py

You can access all the project's settings in the file settings.py, including the settings for the database that was created

##### File: settings.py - Installed apps

In the installed files section you need to add all the applications that were included during the creation of the project. In this example, the registration application has been created, so at the end of the list the name will be added according to the name you created. It is also necessary to inform which framework is being used, in this case 'rest_framework' must be added to the end of the list too

### Creating the API 

#### File: models.py 

This file is responsible to map the main behaviors of the data, usually each model maps one database table. For each type of field used, a data type must be set. For this project the following data types were used:
```
cpf = models.IntegerField(primary_key=True, editable=False)
nome = models.CharField(max_length=255)
dataNascimento = models.DateField(auto_now_add=True)
estado = models.CharField(max_length=70)
cep = models.IntegerField()
```

