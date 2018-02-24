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

x_participants = {} # these will keep a record of everyone's id / interests
y_participants = {} # theres will keep a record of everyone's id / interests.

remaining_x_pool = [] # remaining suitors will go here.
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


# Propose function
def propose(x_id): # x_id and y_id represent their names/#'s/ids.
    # THE FIRST ELEMENT IS X_ID, NOT X'S PREFERENCE.

    
    # First check X's first preference.
    y_id = x_participants[x_id][1]
    print("X_PREFERENCE:")
    print(y_id)

    # See if X's first preference is available.
    try:
        if paired[y_id]: # IF TAKEN ....
            # If X's first preference is paired elsewhere, see if Y would
            # prefer X over their current partner.
            for i in y_participants[y_id]: # iterate over Y's preferences
                if i == x_id: # if X comes up first, pair Y with X instead...
                    remaining_x_pool.append(paired[y_id])
                    # send Y's current partner back to the pool.
                    
                    paired[y_id] = x_participants[x_id] # pair X list with Y.
                    remaining_x_pool.pop(0) # remove this suitor from the pool.
                    
                    
        else: # IF FREE/AVAILABLE...
            paired[y_id] = x_id # simple. Pair X and Y.
            remaining_x_pool.pop(0)# remove x from the pool.
    except:
        pass
    

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

print("START PROPOSALS!")

# initialize remaining X participants into pool
index = 0 # first individual gets ID 0.
for x in x_participants:
    x_participants[x].insert(0,index) # add a label to make sure we keep track of the suitors.
    remaining_x_pool.append(x) # add this suitor to the pool.
    index += 1  # increase this counter, so we keep everyone labeled.

for x in remaining_x_pool: # go through each suitor in the pool
    print("proposing")
    print(x)
    propose(x)
    
