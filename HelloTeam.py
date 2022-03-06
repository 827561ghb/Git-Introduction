#Load and print the team members in different forms

print("Hello Team")


#teamMembers = buildTeam()
teamMembers = buildTeam('teamlist.txt')
print("The Team")
print(team_members)
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




#Complete the following functions below

def buildTeam(filename)
    myTeam = []
    with open(filename) as my_file:
    for line in my_file:
        myTeam.append(line)
    return myTeam


def buildTeam()
    """
    Builds an array of team members

    Returns: array of strings
    """

    team_members = []
    team_members.append('Lee')
    return team_members


#Function 1
def printLongestToShortest(_members):
    print(_members)      
    


#Function 2
def printShortesToLongest(_members):
    print(_members)      



#Function 3
def printAscendingAlphabetical(_members):
    print(_members)      


#Function 4
def printDescendingAlphabetical(_members):
    print(_members)      


