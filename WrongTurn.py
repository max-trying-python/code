namesFile = open("Epitaph.txt")

# split the file into lines
names = namesFile.read().strip().split("\n")

# split lines into lists
names = list(map(lambda line: line.split(", "), names))

# only save the name and age
names = list(map(lambda line: [line[0], int(line[2]) - int(line[1])], names))

# sort the list by the age (the second element in each list) with the highest age first
oldest = sorted(names, key=lambda line: line[1], reverse=True)[0]

# print oldest person's name and age
print("{} died at age {}.".format(oldest[0], oldest[1]))
