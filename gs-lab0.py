import numpy
num_participants = 10
# Even numbers only!

print("Number of participants:")
print(num_participants)

x_participants = {}
y_participants = {}
paired = {}

index = 0
# Kneuth Shuffle
def kneuthShuffle( ls ):
    #copy = ls
    index = 0
    temp = 0
    
    for i in ls:
        index += 1
        shuffle_or_no = numpy.random.randint(0,2)
        print("shuffleorno:")
        print(shuffle_or_no)
        if (shuffle_or_no >= 1) and (index != len(ls)-1) :
            rand = numpy.random.randint(index,len(ls)-1)
            print("rand:")
            print(rand)
            temp = i
            i = rand
            ls[rand] = temp          
        else:
            continue
    print("COPY:")
    print(ls)
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
