# logic behind
#generte random numbers between 1and 6 four times
#count number of 6 gen in the 4 tosses
#repeat the four tosses for many times eg 1000
#our desired probability = total 6 achieved/total no of trials
#
###############
#Analytical solution
print (float(1-((5/6)**4)) )

#####
#Solution through simulation with python
import random

rand_numbers_generated = []
for i in range(1,1001):
    for num in range(1,5):
        rand_numbers_generated.append(random.randint(1, 6))
        num +=1
    i+=1
num_of_six = rand_numbers_generated.count(6)
prob = num_of_six/1000

print("Our desired probability is "+str(prob))

   
