#Load and print the team members in different forms

#Complete the following functions below


def buildTeam(filename):
    """
    Builds an array of team members from file

    Returns: array of strings
    """

    myTeam = []
    with open(filename) as my_file:
        for line in my_file:
            myTeam.append(line.strip())
    return myTeam


#Function 1
def printLongestToShortest(_members):
    print(_members)      
    


#Function 2
def printShortesToLongest(_members):
    _members.sort()
    print(_members) 

#Function 3
def printAscendingAlphabetical(_members):
    _members.sort(key=lambda x: x[-1])
    print(_members) 

#Function 4
def printDescendingAlphabetical(_members):
    print(_members)      


print("Hello Team")


#teamMembers = buildTeam()
teamMembers = buildTeam('teamlist.txt')
print("The Team")
print(teamMembers)
print("-----")

print("Printing Team Members from Longest Name to Shortest")
printLongestToShortest(teamMembers)
print("-----")


print("Printing Team Members from Shortest Name to Longest")
printShortesToLongest(teamMembers)
print("-----")


print("Printing Team Members from A-Z ")
printAscendingAlphabetical(teamMembers)
print("-----")


print("Printing Team Members from Z-A")
printDescendingAlphabetical(teamMembers)
print("-----")


