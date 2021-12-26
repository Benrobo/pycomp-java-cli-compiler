import os
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
    
    -h --help : get some useful informations about this compile
"""

print(options)

print("")
print("Enter some options from the info above")

dirname = os.getcwd()
child_dir = os.path.join(dirname)
parent_dir = os.path.normpath(child_dir)


# get java compilers

def getJavaCompiler():
    data = os.listdir(parent_dir + "/executable")
    return {"java": data[0], "javac": data[1]}

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
    
    compilers = getJavaCompiler()
    filedata = createJavaFile(filename, code, ext)
        
    java = compilers["java"]
    javac = compilers["javac"]
    fileDir = filedata["fileDir"]
    fileName = filedata["filename"]
    
    command = f"cd {parent_dir}/temp && {java} {fileName}"
    
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
    print(output["output"])
    print("")
    print("Continue or pres ctrl+c to quit")

def init():
    userOpt = input()

    if userOpt == "-h" or userOpt == "--heplp":
        return print(options)
        
    elif userOpt == "-r" or userOpt == "--run":
        return runCompile()
    
while True:
    init()