# # # # # # # # # # # 
# Christopher Kelly #
# Spring 2018       #
# # # # # # # # # # #

import numpy
num_participants = 10
# Even numbers only!
# This number represents suitors + girls. Half represents suits, half
# represents girls.

print("Number of participants:")
print(num_participants)

x_participants = {}
y_participants = {}
paired = {}

index = 0


# Kneuth Shuffle
def kneuthShuffle( ls ):
    for i in range(len(ls)):
        j = numpy.random.randint(0,len(ls)-1) # generate a random j index swap
        ls[j], ls[i] = ls[i], ls[j] # swap between the 2 spots!
    return ls
        

                                    
# X can only be interested in the #'s representing the Y Participants,
# the upper half.
def makeParticipantXInterests( n ):
    interests = []
    for i in range(int(n/2), n):
        interests.append(i)

    interests = kneuthShuffle(interests)
    return interests

# Y can only be interested in the #'s representing the X Participants,
# the lower half.
def makeParticipantYInterests( n ):
    interests = []
    for i in range(0, int(n/2)):
        interests.append(i)

    interests = kneuthShuffle(interests)   
    return interests
    
for i in range(0, int(num_participants/2)):
    x_participants[i] = makeParticipantXInterests( num_participants )
    y_participants[i] = makeParticipantYInterests( num_participants )

    
print("X Participant 0:")
print(x_participants[0])
print("X Participant 1:")
print(x_participants[1])
print("X Participant 5:")
print(x_participants[4])

print("Y Participant 0:")
print(y_participants[0])
print("Y Participant 1:")
print(y_participants[1])
print("Y Participant 5:")
print(y_participants[4])
