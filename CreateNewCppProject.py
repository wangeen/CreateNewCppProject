#! /usr/bin/env python
import subprocess, os,  sys
import argparse

# sourceRoot = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))

def script(cmd):
    print cmd
    subprocess.call(cmd,  shell = True)

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--project", help="The project name.")
args = parser.parse_args()

##############################################################################################
def createCMakeFile():
    ## the following is cmake file contents
    content = '''project(myProject)
set(CMAKE_VERBOSE_MAKEFILE ON)
cmake_minimum_required(VERSION 2.8)

set(projectName "'''+args.project+'''")
include_directories(./interface)
include_directories(./include)

if(CMAKE_SIZEOF_VOID_P EQUAL 8)
    message("This is a 64 bit system")
else(CMAKE_SIZEOF_VOID_P EQUAL 8)
    message("This is a 32 bit system")
endif(CMAKE_SIZEOF_VOID_P EQUAL 8)

FILE(GLOB_RECURSE LIB_SRC_LIST src/*.cpp src/*.c src/*.cc)
FOREACH(src ${LIB_SRC_LIST})
	MESSAGE( Find: ${src} )
ENDFOREACH(src)

FILE(GLOB_RECURSE MAIN_SRC_LIST main/*.cpp main/*.c main/*.cc)
FOREACH(src ${MAIN_SRC_LIST})
	MESSAGE( Find: ${src} )
ENDFOREACH(src)

# add more ... ... 3rdParty library
# find_library(lib_boost_program_option NAMES boost_program_options PATHS
# ${libPath} NO_DEFAULT_PATH)
# add_library(${libName} SHARED ${libSrc})
# add_library(${libName} STATIC ${libSrc})

add_executable(${projectName} ${MAIN_SRC_LIST} ${LIB_SRC_LIST})

# add more ... ... add 3rdParty library
# target_link_libraries(${projectName} ${libName})

    '''
    handle = open("CMakeLists.txt", "w")
    handle.write(content)
    handle.close()
    pass

#################################################################################################
def createMainFile():
    content='''#include <iostream>
using namespace std;


int main(int ac,  char** av){
    cout  << "Hello World!" << endl;
    return 0;
}
    '''
    handle = open("main/main.cpp", "w")
    handle.write(content)
    handle.close()
    pass

################################################################################################
def createRunPyFile():
    content = '''#! /usr/bin/env python
import subprocess, os,  sys
import argparse

# sourceRoot = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))

def script(cmd):
    print cmd
    subprocess.call(cmd,  shell = True)

if __name__  == "__main__":
    os.chdir("build")
    script("rm -rf *")
    script("cmake ..")
    script("make -j4")
    script("./{0}")
    '''.format(args.project)
    handle = open("run.py", "w")
    handle.write(content)
    handle.close()
    script("chmod a+x run.py")
    pass


###############################################################################################
if __name__  == "__main__":
    print '''
        This script is used to create a new C/C++ project in working directory.
        Please refer --help for more detail.
    '''
    if args.project:
        projectName = args.project
        if os.path.exists(projectName) is True:
            sys.exit("[Error] The project with name {0} already exists.".format(projectName))
        # create project directory
        script("mkdir {0}".format(projectName))
        # create subdirectories
        os.chdir(projectName)
        script("mkdir build")
        script("mkdir src")
        script("mkdir main")
        script("mkdir interface")
        script("mkdir testcase")
        createCMakeFile()
        createMainFile()
        createRunPyFile()
        pass
