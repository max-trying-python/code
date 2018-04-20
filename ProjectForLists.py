# read the people
peopleF = open("peoples.csv")

people = peopleF.read().strip().split("\n")
peopleList = []
LAST = 0
FIRST = 1

# loop through people and split the list on , (this is a comma seperated values list)
for person in people:
    person = person.split(",")
    peopleList.append(person)


def wishMerryFestivus():
    for person in peopleList:
        # prints (example) John Smith, I wish you a merry festivus!
        print("{} {}, I wish you a merry festivus!".format(person[FIRST], person[LAST]))


def alphabeticalNames():
    # this is a function that returns the first element of a list. useful for sorting by the nth element of a list.
    def firstElem(list):
        return list[0]

    # sort the list by the first element (index 0), the last name
    sortedList = sorted(peopleList, key=firstElem)
    print(sortedList)
    for person in sortedList:
        # print the name
        print("{} {}".format(person[FIRST], person[LAST]))


def tellLikes():
    for person in peopleList:
        if person[4] == "hiking":
            #like hiking?
            print("i like hiking too")

        if person[4] == "tofu":
            #like tofu?
            print("bacon is better")


wishMerryFestivus()
print("\n")
alphabeticalNames()
print("\n")
