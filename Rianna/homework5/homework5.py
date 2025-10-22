# 3.1 vocabulary review

# 1. git is the all-encompassing environment that manages code files and sharing while github is the website made by git that enforces collaboration for script writing.
# 2. the terminal is the software where commands can be written while the command line is where they're actually written and executed.
# 3. local repository is stored on the device itself while a remote repository is stored elsehwere to be shared.
# 4. version control is the practice of tracking and managing changes to files.
# 5. the staging area is what you enter when trying to make changes or save files.
# 6. git add is when you enter the staging area.
# 7. git commit is when you actually begin to save the changes to the file in a staging area.
# 8. git push is when you save the changes made in git commit.
# 9. git status is to check the status of your file in the staging area.
# 10. git pull is used to fetch content from a remote repository to update the local repository.
# 11. pwd is the command to tell you what path your directory is in.
# 12. ls lists all of the files inside of your current working directory.
# 13. cd lets you change the directory you're in.
# 14. nano is a text editor to open files directly in the terminal.
# 15. touch creates a new file.
# 16. mv moves the file to another directory that you choose.
# 17. removes a file from the directory
# 18. cat is used to read & display text files.

# 3.2 directory tree

# cwd
# cd brianna_repo
# mv homework.py homework
# cd homework
# cat homework.py
# git pull, git commit, git push
# brianna's updates were rejected beause she was in the wrong repository and committing out of order.
# c/Users/Brianna/~/Recent/

# 3.3 drawing my own directory tree 

# 4 homework 3 review

def checkDataType(n):
    return print(type(n))

# 4.2 conditionals
def evenOrOdd(int):
    if int % 2 == 0:
        print("even")
    else:
        print("odd")

# 5 loops
def sumWithLoop(numbers):
    i = 0
    for number in numbers:
        i = i + number
    return i

# 6.1 lists
def duplicateList(list):
    new_list = []
    for item in list:
        new_list.append(item)
        new_list.append(item)
    return new_list

# 6.2 debugging

# there should be parantheses and a colon!

def square(num):
    return (num * num)

# 7.2 my favorite function!
print(duplicateList(["i", "like", "cheese"]))
