# DjangoProjectStarter

## Introduction
This script automates the task of making a DjangoProject. A Django project involves a variety of tasks such as, Doing Template Inheritance in all templates, Applying migrations, Creating static files folder, Updating settings.py (with static root, StaticFiles_Dir, templates, media root and many more), Adding templates, Creating different directories, Updating urls and Importing important modules, so I made this script to automate this task.

## Usage
This script can be executed in two ways:

### 1.Using arguments
    You can use arguments to specify different variables in this script.For example:
     
    If you run  ``` python DjangoProjectStarter.py -h ``` .It will give a list of all arguments to use with this script. These are:
    
    -p  For specifying name of the project
    -a  For specifying name of the app 
    -t  For adding templates
    
    
### 2.By Input
    
    You can just directly run the script like ```python DjangoProjectStarter.py ``` , and it will ask the above variables(name of the project , app and templates) in the form of user input.
    For Instance;
    ```
    Specify a unique name for the project:<project name>
    Name of the app built in this project:<app name>
    Base.html and About.html will be made automatically. You can give additional templates by inputting them with space in between or ou can write no or n
    Templates:<templates names>
    
    ```
    After that script will be run normally.

## Conclusion
   This Project was made by me because I used to spend most of the time doing same repetitve tasks while working on Django Projects, so I decided to automate this process.
    
