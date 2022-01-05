import os
import platform
import subprocess
import pyfiglet
from util.index import *

fig = pyfiglet 

# print compiler title
print(fig.figlet_format("pycomp", font='larry3d'))

# show compiler options

options = """
    Welcome To PyComp
    
    -r --run : run and compile java codes

    -l  --lagrange : run and compile the lagrange Interpolation Formular
    
    -h --help : get some useful informations about this compile
"""

print(options)

print("")
print("Enter some options from the info above")

dirname = os.getcwd()
child_dir = os.path.join(dirname)
parent_dir = os.path.normpath(child_dir)


def createJavaFile(filename, code="", extension="java"):
    # check if temp folder is available
    # cause that were all java files would be created

    newDir = f"{parent_dir}/temp"
    
    print("newDir", newDir)

    if os.path.isdir(parent_dir + "/temp") == False:
        # create new directory
        os.mkdir(newDir)
        print("directory created")

    # after making a new directory
    # create a file
    fileName = f"{filename}.{extension}"
    fileDir = os.path.join(newDir, fileName)
    
    # write data to that file
    
    f = open(fileDir, "w")
    f.write(code)
    f.close()
    
    print("")
    
    return { "fileDir": fileDir, "filename": fileName }

def compileJavaCode(filename, code = "", ext="java", cb=None):
    
    filedata = createJavaFile(filename, code, ext)
        
    # java = compilers["java"] this has been deprecated
    # javac = compilers["javac"] same as this. make sure you have java installed
    fileDir = filedata["fileDir"]
    fileName = filedata["filename"]
    
    command = f"cd {parent_dir}/temp && java {fileName}"
    
    output = {}
    
    compilerResult = subprocess.run(command, shell=True)
    
    output["output"] = compilerResult
    
    return output
 
def runCompile():
    # get the filename user wanna create
    print("")
    print("Provide the name of the file you wanna create without having extensions")
    filename = input()
    # get muli-line input from users
    userInputs = Input("Write some java codes here..")
    output = compileJavaCode(filename, userInputs, "java")
    print("")
    print("")
    print(output["output"])
    print("")
    print("")
    print("Continue or pres ctrl+c to quit")


def compileLagrange():
    dir = os.path.normpath(child_dir)
    lagDir = f"{dir}/util/Lagrange.java"

    # check if the lagrange directory exists.
    if os.path.exists(lagDir) == False:
        # print error messsage
        print("")
        print(f"Error running lagrangeInterpolation: cant locate Lagrange in {lagDir}")
    
    # check the os name and associate different commands to each os

    command = ""

    if platform.system() == "Linux":
        command = f"java {lagDir}"
    elif platform.system() == "Windows":
        command = f"cd {dir}/util && java Lagrange.java"
    else:
        command = f"java {lagDir}"

    # run the command using subprocess
    compilerResult = subprocess.run(command, shell=True)

    return compilerResult


def init():
    userOpt = input()

    if userOpt == "-h" or userOpt == "--help":
        return print(options)
        
    elif userOpt == "-r" or userOpt == "--run":
        return runCompile()
    elif userOpt == "-l" or userOpt == "--lagrange":
        compileLagrange()
        print("")
        return
    else:
        print("")
        print("Command you entered is invalid")
    
while True:
    init()
    
    