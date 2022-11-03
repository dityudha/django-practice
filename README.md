# Getting Started with django REST API with react
Technology used for this project:<br/>
**React.js** is a front-end JavaScript library used to build interactive user interfaces for applications.<br/>
**Django** is a Python open-source backend framework that is built solely on a model-template-view architecture.<br/>
**MySQL** is a relational database management system (RDBMS) developed by Oracle that is based on structured query language (SQL).<br/>
**XAMPP** has the ability to serve web pages on the World Wide Web.<br/>

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app)

## Available Scripts

In the project directory, you can run:

### Create django virtual environment

Go to django-rest-api directory and run this command:<br/>
**python -m venv (virtual env name)**

Go to the env directory, and run this command **"env\Scripts\activate"**.<br/>
After running this command, you should see the name of the virtual environment enclosed in brackets.

### Install Library 

Inside virtual environment directory run this command to install library:<br/>
**python -m pip install django djangorestframework django-cors-headers mysqlclient**

### Create local MySQL Database

Create local database with XAMPP named "djangodb", or whatever you want that must same with file settings.py on mysite directory.<br/>

### Migrate Database

Inside virtual environment directory run this command<br/>
**py manage.py migrate**


### Start Django

Inside virtual environment directory run this command<br/>
**py manage.py runserver**

### Apps Preview

![1](https://user-images.githubusercontent.com/33762836/199698611-bc43867f-905b-4daf-8232-f598a9120e1a.PNG)<br/>
![2](https://user-images.githubusercontent.com/33762836/199698622-af617942-11ad-4ea1-8a3d-59296bf4502f.PNG)<br/>
![3](https://user-images.githubusercontent.com/33762836/199698626-b72ed529-7c70-488f-8fe9-8093cad8bfcd.PNG)<br/>

### MySQL Database Preview

![4](https://user-images.githubusercontent.com/33762836/199698632-36eae861-b922-4137-aa04-5e56141a2719.PNG)<br/>
![5](https://user-images.githubusercontent.com/33762836/199698635-726473df-38eb-4c8d-801a-2aef9d36b36b.PNG)<br/>







