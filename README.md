# Getting Started with django REST API with react
Technology used for this project:<br/>
React.js is a front-end JavaScript library used to build interactive user interfaces for applications.<br/>
Django is a Python open-source backend framework that is built solely on a model-template-view architecture.<br/>

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






