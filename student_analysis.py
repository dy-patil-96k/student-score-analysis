import numpy as np
#1..
score = np.array([[85,92,78],[76,88,95],[90,80,82],[68,75,70],[94,86,91]])

# #2..
# student_no=int(input('enter the student number to find the average score:'))-1
# print ('the avarage score of student{}is'.format(student_no))
# print(np.average(score[student_no]))

#3
#avarage scpre of all students in math
print('avarage score of all students in math is : ',np.mean(score[:,0]))

#4..
# print('highest score in math is : ',np.max(score[:,0]))
# print('highest score in science is : ',np.max(score[:,1]))
# print('highest score in english is : ',np.max(score[:,2]))