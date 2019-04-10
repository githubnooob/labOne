import unittest
import time
import random
import matplotlib.pyplot as plt


# to run unit test, uncomment the line no 54 and 53
# extend unittest.Testcase in LabOne class
class LabOne():
    def linearSearch(self,array,num):
        for index in range(len(array)):
            if  num == array[index]:
                return index
        return -1

    def binarySearch(self,array,num):
        firstIndex = 0
        lastIndex = len(array)-1
        found = False
        while firstIndex<=lastIndex and not found:
            index = int((firstIndex+lastIndex)/2)
            if array[index]==num:
                found = True
                return  index
            else:
                if num < array[index]:
                    lastIndex = index-1
                else :
                    firstIndex = index+1

    def testAnswers(self):
            values = [1,23,4,56,7,89]
            indexLinear = self.linearSearch(values,89)
            self.assertEqual(indexLinear,5)
            indexBinary = self.binarySearch(values,89)
            self.assertEqual(indexBinary,5)


    def  plottingAssignmet(self):
        random_numbers = random.sample(range(10000),10000)
        sorted_number =sorted(random_numbers)
        time_taken = {}
        step_size = 1000
        for _ in range(int(len(sorted_number)/step_size)):
            start_time = time.clock()
            x=self.linearSearch(sorted_number,sorted_number[-1])
            end_time= time.clock()
            time_taken[len(sorted_number)] = end_time-start_time
            sorted_number = sorted_number[step_size:]
        return time_taken
l = LabOne()

#if __name__=="__main__:
#   unittest.main()

timeTakenDict = l.plottingAssignmet()
n = []
t = []
for key in sorted(timeTakenDict):
    n.append(key)
    t.append(timeTakenDict[key])

plt.plot(n,t)
plt.xticks(n)
plt.yticks(t)
plt.show()

# if __name__=="__main__":
#     unittest.main()



