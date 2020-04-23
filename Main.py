import numpy as np
import random as rm

# 2x2 Matrix
A = np.array([[1, 2], [3, 4]])
A2 = np.array([[5, 6], [7, 8]])
# 3x3 Matrix
B = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# #################Needed for Markov Chain####################
# statespace
state = ["work", "sleep", "freetime"]
# possible sequences of events
transitionName = [["WW", "WS", "WF"],["SW","SS","SF"],["FW","FS","FF"]]
# Probabilities matrix (transition matrix) ~ each row [x,x,x] = 1
transitionMatrix = [[.2,.5,.3],[.0,.9,.1],[.3,.3,.4]]

def initializationCheck():
    if sum(transitionMatrix[0]) + sum(transitionMatrix[1]) + sum(transitionMatrix[1]) != 3:
        print("Invalid transition matrix")
        return -1
    else:
        pass

def what_will_I_do_today(days):
    # Choose the starting state
    activityToday = "work"
    activityList = [activityToday]
    i = 0
    prob = 1
    # while the number of days does not equal 0
    while i != days:
        # if the activity for today is work
        if activityToday == "work":
            # pick a random transitionName
            change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
            # if the transitionName is "WW"
            if change == "WW":
                prob = prob * .2
                activityList.append("work")
                pass
            # if the transitionName is "WS"
            elif change == "WS":
                prob = prob * .5
                activityToday = "sleep"
                activityList.append("sleep")
            # if the transitionName is "WF"
            else:
                prob = prob * .3
                activityToday = "freetime"
                activityList.append("freetime")
        # if the activity for today is sleep
        elif activityToday == "sleep":
            # pick a random transitionName
            change = np.random.choice(transitionName[1],replace=True,p=transitionMatrix[1])
            # if the transitionName is "SW"
            if change == "SW":
                prob = prob * .0
                activityList.append("work")
                pass
            # if the transitionName is "SS"
            elif change == "SS":
                prob = prob * .9
                activityToday = "sleep"
                activityList.append("sleep")
            # if the transitionName is "SF"
            else:
                prob = prob * .1
                activityToday = "freetime"
                activityList.append("freetime")

        # if the activity for today is freetime
        elif activityToday == "freetime":
            # pick a random transitionName
            change = np.random.choice(transitionName[2],replace=True,p=transitionMatrix[2])
            # if the transitionName is "FW"
            if change == "FW":
                prob = prob * .3
                activityList.append("freetime")
                pass
            # if the transitionName is "FS"
            elif change == "FS":
                prob = prob * .3
                activityToday = "sleep"
                activityList.append("sleep")
            # if the transitionName is "FF"
            else:
                prob = prob * .4
                activityToday = "work"
                activityList.append("work")
        i += 1
    return activityList


def markovChain():
    initializationCheck()
    what_will_I_do_today(3)     #3 is days
    # To save every activityList
    list_activity = []
    count = 0
    # `Range` starts from the first count up until but excluding the last count
    for iterations in range(1,10000):
            list_activity.append(what_will_I_do_today(2))
    # Check out all the `activityList` we collected
    #print(list_activity)
    # Iterate through the list to get a count of all activities ending in state:'v'
    for smaller_list in list_activity:
        if(smaller_list[2] == "freetime"):
            count += 1
    # Calculate the probability of starting from state:'sleep' and ending at state:'freetime'
    percentage = (count/10000) * 100
    print("The probability of starting at state:'sleep' and ending at state:'freetime'= " + str(percentage) + "%")



# takes th determinate of a 2x2 matrix
def det2x2(X):
    R1, R2 = X
    if len(X) and len(R1) and len(R2) != 2:
        print("ERROR: Invalid matrix configuration")
    else:
        R1, R2 = X
        a, b = R1
        c, d = R2
        determinate = (a * d) - (b * c)
        return (determinate)


# takes th determinate of a 3x3 matrix
def make2x2(a, b, c, d):
    F = np.array([[a, b], [c, d]])
    return F


def det3x3(X):
    if len(X) != 3:
        print("ERROR: Ivalid matrix configuration")
    else:
        R1, R2, R3 = X
        a, b, c = R1
        d, e, f = R2
        g, h, i = R3
        a1 = det2x2(make2x2(e, f, h, i))
        b1 = det2x2(make2x2(d, f, g, i))
        c1 = det2x2(make2x2(d, e, g, h))
        determinate = (a * (a1) - b * (b1) + c * (c1))
        return determinate


# for a 2x2 matrix
# regular formula is
# A^-1 = 1/det(A) * [[d, -b],[-c,a]]
def a_inverse2x2():
    pass

# what is being called



