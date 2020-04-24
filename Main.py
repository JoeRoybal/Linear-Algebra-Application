import numpy as np
import random as rm

# 2x2 Matrix
A = np.array([[1, 2], [3, 4]])
A2 = np.array([[5, 6], [7, 8]])
# 3x3 Matrix
B = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# #################Needed for Markov Chain####################
# The statespace
states = ["Work", "Sleep", "Free Time"]

# Possible sequences of events
transitionName = [["WW", "WS", "WF"], ["SW", "SS", "SF"], ["FW", "FS", "FF"]]

# Probabilities matrix (transition matrix)
transitionMatrix = [[.2, .5, .3],
                    [.4, .5, .1],
                    [.3, .3, .4]]
# ############################################################

def initializationCheck():
    if sum(transitionMatrix[0]) + sum(transitionMatrix[1]) + sum(transitionMatrix[2]) != 3:
        print("Invalid transition matrix")
        return -1
    else:
        pass


def what_will_I_do_today(days):
    # Choose the starting state
    activityToday = "Sleep"
    # print("Start state: " + activityToday)
    activityList = [activityToday]
    i = 0
    prob = 1
    while i != days:
        if activityToday == "Work":
            change = np.random.choice(transitionName[0], replace=True, p=transitionMatrix[0])
            if change == "WW":
                prob = prob * 0.2
                activityList.append("Work")
                pass
            elif change == "WS":
                prob = prob * 0.5
                activityToday = "Sleep"
                activityList.append("Sleep")
            else:
                prob = prob * 0.3
                activityToday = "Free Time"
                activityList.append("Free Time")

        elif activityToday == "Sleep":
            change = np.random.choice(transitionName[1], replace=True, p=transitionMatrix[1])
            if change == "SW":
                prob = prob * 0.4
                activityToday = "Work"
                activityList.append("Work")
            elif change == "SS":
                prob = prob * 0.5
                activityList.append("Sleep")
                pass
            else:
                prob = prob * 0.1
                activityToday = "Free Time"
                activityList.append("Free Time")

        elif activityToday == "Free Time":
            change = np.random.choice(transitionName[2], replace=True, p=transitionMatrix[2])
            if change == "FW":
                prob = prob * 0.3
                activityToday = "Work"
                activityList.append("Work")
            elif change == "FS":
                prob = prob * 0.3
                activityToday = "Sleep"
                activityList.append("Sleep")
            else:
                prob = prob * 0.4
                activityList.append("Free Time")
                pass
        i += 1
    return activityList


def markovChain():
    # To save every activityList
    list_activity = []
    count = 0

    # `Range` starts from the first count up until but excluding the last count
    for iterations in range(1, 10000):
        list_activity.append(what_will_I_do_today(2))

    # Check out all the `activityList` we collected
    # print(list_activity)

    # Iterate through the list to get a count of all activities ending in state:'Free Time'
    for smaller_list in list_activity:
        if (smaller_list[2] == "Free Time"):
            count += 1

    # Calculate the probability of starting from state:'Sleep' and ending at state:'Free Time'
    percentage = (count / 10000) * 100
    print("The probability of starting at state:'Sleep' and ending at state:'Free Time'= " + str(percentage) + "%")


# takes the determinant of a 2x2 matrix
def det2x2(X):
    R1, R2 = X
    if len(X) and len(R1) and len(R2) != 2:
        print("ERROR: Invalid matrix configuration")
    else:
        R1, R2 = X
        print("Matrix =\n", X)
        print(" Row 1 =", R1, "\n", "Row 2 =", R2)
        a, b = R1
        c, d = R2
        print(" a =", a, ", b =", b, ", c =", c, ", d =", d)
        determinate = (a * d) - (b * c)
        print(" (a * d) - (b * c) = (", a, "*", d, ") - (", b, "*", c, ") =", determinate, "\n")
        return determinate


# converts 4 numbers into 2x2 matrix
def make2x2(a, b, c, d):
    F = np.array([[a, b], [c, d]])
    return F


# takes the determinant of a 3x3 matrix
def det3x3(X):
    R1, R2, R3 = X
    if len(X) and len(R1) and len(R2) and len(R3) != 3:
        print("ERROR: Invalid matrix configuration")
    else:
        R1, R2, R3 = X
        print("Matrix =\n", X)
        print("For the 3x3 matrix \n Row 1 =", R1, "\n", "Row 2 =", R2, "\n", "Row 3 =", R3)
        a, b, c = R1
        d, e, f = R2
        g, h, i = R3
        print(" a =", a, ", b =", b, ", c =", c, ", d =", d, " e =", e,
              ", f =", f, ", g =", g, " h =", h, ", i =", i, "\n")
        detA = print("For the 2x2 matrix a =", a), det2x2(make2x2(e, f, h, i))
        detB = print("For the 2x2 matrix b =", b), det2x2(make2x2(d, f, g, i))
        detC = print("For the 2x2 matrix c =", c), det2x2(make2x2(d, e, g, h))
        determinate = ((a * detA[1]) - (b * detB[1]) + (c * detC[1]))
        return print("(a * (detA) - b * (detB) + c * (detC)) = (", a, "* (", detA[1], ") -", b, "* ("
                     , detB[1], ") +", c, "* (", detC[1], ")=", determinate, "\n")


# for a 2x2 matrix
# regular formula is
# A^-1 = 1/det(A) * [[d, -b],[-c,a]]
def flipflop(X):
    R1, R2 = X
    if len(X) and len(R1) and len(R2) != 2:
        print("ERROR: Invalid matrix configuration")
    else:
        R1, R2 = X
        print("Matrix =\n", X, "\n")
        a, b = R1
        c, d = R2
        print("Matrix flip flopped =")
        X = make2x2(d, -b, -c, a)
        print(X, "\n")
        return X


def a_inverse2x2(X):
    R1, R2 = X
    if len(X) and len(R1) and len(R2) != 2:
        print("ERROR: Invalid matrix configuration")
    else:
        Y = flipflop(X)
        a_inverse = np.dot((1 / det2x2(X)), Y)
        # \n & \t are used for formatting
        print("A inverse = \n 1/det(A) *", Y[0], "\n", "\t\t   ", Y[1], "\n  =", a_inverse[0], "\n   ", a_inverse[1])
        return a_inverse


# Matrix Multiplication is Associative
def associative():
    pass


# what is being called
# what_will_I_do_today(2)
markovChain()
