import os,subprocess,platform,sys
import argparse
from getpass import getuser


parser=argparse.ArgumentParser()
parser.add_argument("-p",help="Give the name of your project.")
parser.add_argument("-a",help="Give the name of our app.")
parser.add_argument("-t",help="For creating multiple templates specify them by having space in between or you can just type n,no,N,No.")
args=parser.parse_args()
def start(nameProject,nameApp,ADD_TEMPLATES=None):

    """This function is responsible for completing all basic things in a Django Project"""
    USR=getuser()
    SYS=platform.system()

    #Target_Directory and Project_Directory according to your operating system
    #I can simply build Django Project in Current Directory but I just like to work on the project while it is on Desktop.
    if SYS=="Linux":
       Target_Directory=f"/home/{USR}/Desktop"    

    elif SYS=="Windows":
       Target_Directory=f"C:\\Users\\Public\\{USR}\\Desktop"

    else:
        print("Your os is not supported.\nYou have to manually write the Target Directory\nFor example, /home/user123/Desktop or cwd for currentdirector")
        Target_Directory=input("TargetDirectory")
        if Target_Directory=="cwd":
            Target_Directory=os.getcwd()

    
    Common=["python3","manage.py"]
    Start_Django=["django-admin","startproject",nameProject]
    Start_App=["python3","manage.py","startapp",nameApp]
    dirs=["media","assets","static","templates"]
    Run_Migrations=Common+["makemigrations"]
    Migrate=Common+["migrate"]
    Settings_data=  ["MEDIA_ROOT = os.path.join(BASE_DIR,'media')\n","MEDIA_URL = '/media/'\n","STATIC_ROOT =  os.path.join(BASE_DIR,'assets')\n","STATIC_URL = '/static/'\n","STATICFILES_DIRS = [ BASE_DIR / 'static']"]
    if ADD_TEMPLATES!=None:
       template=["index.html","about.html"]+ADD_TEMPLATES
    else:
        template=["index.html","about.html"]
    PATH_to_Settings=f"{nameProject}/settings.py"
    PATH_to_Urls=f"{nameProject}/urls.py"
    PATH_to_Views=f"{nameApp}/views.py"
    
    if os.getcwd()!=Target_Directory:
         os.chdir(Target_Directory)#Change director to target location

    List_Dirs=os.listdir()

    if nameProject in List_Dirs:
        print("Folder is already present!!")
        sys.exit()

    #Code  for starting Django Project

    subprocess.run(Start_Django)
    os.chdir(nameProject)

    #This below  code is for starting an app and running migrations

    subprocess.run(Start_App)
    subprocess.run(Run_Migrations)
    subprocess.run(Migrate)

    #Below code is for making basic directories and for creating and updating basic as well as given templates

    for i in dirs:
        os.mkdir(i)
   
    f=open("templates/base.html","w")
    f.write("<html>\n<head><title>{%block title%}{%endblock%}</title>\n</head>\n<body>\n{%block body%}{%endblock%}\n</body>\n</html>")
    f.close()
    for i in template:
        if i!="index.html":
            with open(f"templates/{i}",'a') as f:
                f.write("""{%extends 'base.html%'}\n{%block title%}{%endblock%}\n{%block body}{%endblock%}""")
        else:
            with open("templates/index.html","w") as f:
                f.write("""{%extends 'base.html'%}\n{%block title%}Home{%endblock%}\n{%block body%}<p>This is an Index page</p>{%endblock%}""")

    #Below code is for updating settings.py

    with open(PATH_to_Settings,'r') as f:
        data=f.readlines()
    data[14]="import os\n\n"
    data[56]="        'DIRS': [ BASE_DIR / 'templates'],\n"
    data[39]=f"    '{nameApp}' ]"
    data[122]+="#Below are Added Later\n"
    
    for i in Settings_data:
        data.append(i)
    
    with open(PATH_to_Settings,'w') as f:
        f.writelines(data)
    
    #This code is for updating urls.py
    with open(PATH_to_Urls,"r") as p:
        urldata=p.readlines()
    urldata[17]=f"from django.conf.urls.static import static\nfrom django.conf import settings\nfrom {nameApp} import views\n"
    urldata[20]=f"    path('',views.index,name='index')]\n"   
    urldata.append("\nurlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)")
    
    with open(PATH_to_Urls,"w") as f:
        f.writelines(urldata)
    
    #Code for updating views.py
    
    with open(PATH_to_Views,"a") as f:
        f.write("def index(request):\n    return render(request,'index.html')")


    #Message after all the things worked well
    print("Success")
    
if __name__=="__main__":
    
    print("Your Django project will be built on Desktop Folder.")
    if args.a and args.p:
        nameProject=args.p
        nameApp=args.a
        if args.t:
           ADD_templates=[args.t]
        else:
           ADD_templates=None
    else:
        nameProject=input("Specify a unique name for the project: ")
        nameApp=input("Name of the app built in this project:")
        print("Base.html and About.html will be made automatically. You can give additional templates by inputting them with space in between or You can press enter to skip this part.")
        ADD_templates=input("Templates: ").split(" ")
        if  ADD_templates[0]=="":
            ADD_templates=None

    start(nameProject,nameApp,ADD_TEMPLATES=ADD_templates)
