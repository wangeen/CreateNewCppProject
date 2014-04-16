CreateNewCppProject
===================

Python, CPP Project, CMake

This is a script for create a new CPP project with CMake to manage it.  
The following is a hierarchy tree for the project.  

> ProjectName  
   |__________run.py  
   |__________CMakeLists.txt  
   |__________src  
   |__________interface  
   |__________main  
   |           |___________main.cpp  
   |  
   |__________build  

- *run.py*:  script for build and test current project, also do some dirty jobs, such as commit SVN.  
- *CMakeLists.txt*: cmake file to manage current project.  
- *src: the directory for source code and common header files.  
- *interface*: if you want to create a library, some header files should be shared in this directory.  
- *main*: the directory for main.cpp, this can be changed if necessary.  
- *build*: temp folder, saving temp files for the project.  




