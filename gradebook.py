last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
#CheckPOint 1
subjects = [["Physics",98],["Calculus",97],["Poetry",85],["History",88]]
#CheckPOint 2 add  index to checkpoint 1 

#CheckPOint 3
gradebook = subjects 
#Checkpoint 4
print(gradebook)
#Checkpoint 5
subjects.append(["Computer Science", 100])

#CheckPOint 6
subjects.append (["Visual Arts",93])
#Checkpoint 7
gradebook[-1][-1] =98
gradebook.remove(["Poetry",85])
gradebook.append (["Poetry","Pass"])
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)