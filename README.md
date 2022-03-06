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
- [Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Github](https://github.com/)
- [Git Cheat Sheat](https://education.github.com/git-cheat-sheet-education.pdf)
- [Markdown Cheat Sheat](https://www.markdownguide.org/cheat-sheet/)

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
3. Set your editor 'git config --global core.editor "code --wait' This specifies the use of vscode.  You can use other editors like VIM!
4. To check your settings you can do the following 'git config --global -e' This will open the configuration settings using your default editor


### Definitions
1. Git - Git is an open source program for tracking changes in text files
2. Repository - The repository tracks all changes made to files in your project, building a history over time.
3. Project -  Project is the folder in which the actual content(files) lives
4. Remote - A common repository that all team members use to exchange their changes
5. Local -  For where you keep your copy of a Git repository on your computer



### Key Git Commands to Know for Today
1. 'git help' Lists all of the git commands
2. 'git status' Shows the status of files in the working directory
3. 'git add [file]' Adds a file to your next commmit (stage)
4. 'git commit -m "Message"' Commits your staged content as a new commit snapshot
5. 'git push' Sends local commits to the remote repository branch
6. 'git pull' Fetches and merges remote commits to local repository
7. 'git clone' Retrieves an entire repository from a hosted location
8. 'git init' Initializes a git repository from an existing directory
9. 'git diff' Tells you the difference of what is changed but not staged


# Simple Git Project
We are going to start with an existing project already in Git.  When accessing an existing project you have two options
1. Cloning the project or repository [Git Clone Diagram](lesson-material/clone.jpg)
2. Forking the project or repository [Git Fork Diagram](lesson-material/fork.jpg)

For this lesson we are going to clone an existing project.  I have created a public project here:
[Git-Introduction](https://github.com/827561ghb/Git-Introduction)
1. Open the link and select the code byutton.  You have the option of copying a link to clone the repository.  Copy the link.
[Git project screenshot](lesson-material/git-project-screenshot.jpg)
2. Create a directory in your documents folder called projects.  Using the command line change to the projects directory.
2. Next in the command line type the following: 'git clone https://github.com/827561ghb/Git-Introduction.git'
3. What happens?  Try typing 'ls' in the command line.  What do you see?

When you clone a repository you copy or clone the repository to your local git repository.   Take a look around.  You can also view the files in Windows file explorer!

## A few standard files (best practice) for all projects
1. README.MD - This file provides a description of what the project is, how to use or install it.  It also typically provides the software license.  It is typically written using markdown language.  But this is not required.  Markdown language allows you to easily display the README within a webpage.  Take a look at the README.md file in this project.  what do you see?  Now go here: [Github project](https://github.com/827561ghb/Git-Introduction) Notice that this README is displayed.
2. .gitIgnore - This file automatically tells git to ignore certain files associated with a software language and typical temporary files.  You can add to this file by editing it
3. docs/ - This directory is where you can write or place automatically generated documentation files.  They can html or MD files.
4. LICENSE - This license tells others what type of license is associated with this project.

## Adding a Document 
Now let us try editing a document
1. We are going to collaboratively work on the project. First we want to create a list of team member names. Who wants to create a new file in the project root directory called 'teamlist.txt'?  Open this file and add the first names of all the team members. What are the names that we should add?
2. Now save and close the document
3. Next we want to add the member list to our project.  
4. Type 'git status'  What do you see?
5. Because 'teamlist.txt' is a new file, git shows it as untracked.  We need to explicitly add it to the repository.  Do this by typing 'git add teamlist.txt'
6. Now type 'git status'  What changed?
7. Now we want to commit this to the repository.  The file has only been staged at this point.  Type 'git commit -m "message describing the changes"'
8. Someone else try and type 'git pull'.  Did you see any changes?  Why not?
9. We need to push the changes to the remote repository for others to see the changes.  Type 'git push'.  You will be asked to login because you are making changes to the remote repository or project.  In this case the project is owned by the user 827561ghb.
10. Now everyone should be able to pull the changes by typing 'git pull'.  What did you see?

## Editing a Python File
Next we will try editing a Python file separately and merging the changes.  Git has the ability to check changes within a file and update the local changes
1. First make sure you do a 'git pull'  This will bring any changes from the remote repository to your local repository on your computer
2. Break up into four teams
3. Each team will complete a small function to print the team member list in a specific order.  Let's assign what a function to each team.
4. Work on your function with your team
5. When complete save and close the file.
6. Run the python code by typing 'python HelloTeam.py'.  After testing your function and confirming it works, what are the steps you need to take to update your repository with the changes?  What steps do you need to take to update the master remote repository with your changes?  Do a 'git status' to see the status according to git of your files. Try committing your changes now.
7. Wait for everyone to finish
8. Merging changes.  Now let's try merging your team's changes so that you can have the most up to date code.
9. You can first do a 'git diff' or 'git diff HelloTeam.py'  What did you see?
10. Try doing a 'git pull'.  What happened?
11. Now run your 'HelloTeam.py'  What do you see? 

Congratulations, if everything went as planned, you just merged changes from multiple software developers.  On top of that all of the version are kept and tracked in git.  So if you ever needed to go back or undo a change, you can do that.

To look at the changes, try 'git log'.  This will list all the commits from all of the developers.




# Best Practices
## What files should you include and not include in a repository?
1. Include source code files
2. Do not include tmp files, or configuration files that are unique to you.  These files will then be changed by everyuser
3. Do not include large data files.  Git is not designed for large data files
4. Do include documentation files



# Other Useful Things to Know
1. The .gitIgnore file.  This file is in the base directory of your repository.  It tells git what files to ignore so that they are not listed in git status. This is useful to ignore configuration files, tmp files, large binary files, etc.
2. It is always good practice to push your changes to the shared repository after a coding session and when you are happy with your code.  This allows others to build off of what you wrote
3. You should always leave an informative comment when pushing.  This allows you and others to understand what the changes were
4. Not addressed today is how to use git inside of visual studio
5. Git supports the idea of branches.  We may want to think about using different branches to keep our development, test, and competition code separated.  By default, each project starts with a master branch.  One way to use branches is to keep new untested code separated from the competition or production code and only add that code when it is fully tested and mature.  In this way you can help track and avoid any errors or bugs while also allowing to new things out.  Git helps you automatically track and maintain these separate versions!
6. Moving files or removing files.  Since git is tracking all files you cannot just delete them in the file system.  You should always do a 'git rm [file]' or 'git mv [existing] [new]' for files being tracked by git.  Otherwise they will not be removed or moved in the repository, just your local working directory


# Designing our First Lego Repository
Break up into teams.  Your task is to think about how you should design your Lego repository.  Look at your code that you developed for previous competitions.  

Questions
1. What code do you currently have?  Who can walk through the software from the last lego competition? 
2. Are common functions or behaviors that you reuse?
3. What code stays the same? What code changes?
4. Where do you keep your documents?  Presentation material?  
5. Are there any competition specific files or documents?
6. What were any challenges you faced as a team when developing code for the competition?  How do we think git can help?















