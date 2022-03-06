# Git-Introduction

# Welcome
Welcome to a Git introduction and tutorial.  In this lesson you will learn:
1. What is Git and what is software version control is
2. Why Git is an important tool for software development
3. The basics of using Git 
4. What is Github
5. Using Git in your first software development project

# References
- [Git for Windows](https://gitforwindows.org/)
- [Installing Git] (https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Github](https://github.com/)

# Prerequisites
1. Windows, Mac, or Linux computer
2. Github account

## What is Git & Software Version Control
- [Git Explainer video](https://www.youtube.com/watch?v=8JJ101D3knE)

### Introduction Video Questions & Discussion
1. What can you do with a software version control system?
2. What is the difference between a centralized vs distributed system?
2. What is a repository?



### Using GIT
How can you use GIT? 
1. Command Line, 
2. Integrated Development Environment (IDE)
3. raphical User Interfaces (GUI)

Today we will focus on using the command line. 
In the windows search box type 'powershell'


### Configuring GIT

1. Set your username 'git config --global user.name "Your Name"'
2. Set your email 'git config --global user.email youremail@email.com'
3. Set your editor 'git config --global core.editor "code --wait' This specifies the use of vscode
4. To check your settings you can do the following 'git config --global -e' This will open the configuration settings using your default editor


### Definitions
1. Repository
2. 


### Common Git Commands
1. git - 


# Simple Git Project
We are going to start with an existing project already in Git.  When accessing an existing project you have two options
1. Cloning the project or repository
2. Forking the project or repository 

For this lesson we are going to clone an existing project.  I have created a public project here:
[Git-Introduction](https://github.com/827561ghb/Git-Introduction)
1. Open the link and select the code byutton.  You have the option of copying a link to clone the repository.  Copy the link.
[Git project screenshot](lesson-material/git-project-screenshot.jpg)
2. Create a directory in your documents folder called projects.  Using the command line change to the projects directory.
2. Next in the command line type the following: 'git clone https://github.com/827561ghb/Git-Introduction.git'
3. What happens?  Try typing 'ls' in the command line.  What do you see?

When you clone a repository you copy or clone the repository to your local git repository?   Take a look around.  You can also view the files in Windows file explorer!

##Editing a Document 
Now let us try editing a document
1. Open and edit the file HelloTeam.py
##

#Best Practices
##What files should you include and not include in a repository?
1. Include source code files
2. Do not include tmp files, or configuration files that are unique to you.  These files will then be changed by everyuser
3. Do not include large data files.  Git is not designed for large data files
4. Do include documentation files



#Other Useful Things to Know
1. The .gitIgnore file.  This file is in the base directory of your repository.  It tells git what files to ignore so that they are not listed in git status. This is useful to ignore configuration files, tmp files, large binary files, etc.
2. It is always good practice to push your changes to the shared repository after a coding session and when you are happy with your code.  This allows others to build off of what you wrote
3. You should always leave an informative comment when pushing.  This allows you and others to understand what the changes were














