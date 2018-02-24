# # # # # # # # # # # # # # # # # # # # # # # #
# Gale - Shapley Algorithm
# Christopher Kelly 
# Spring 2018       
# INPUT: Amount of Participants
# OUTPUT: A Stable-Matched Set of X-Y pairs
# EXAMPLE: ./gs-lab0.py 25
#

import numpy
num_participants = 10
# Even numbers only!
# This number represents suitors + girls. Half represents suits, half
# represents girls.

print("Number of participants:")
print(num_participants)

x_participants = {} # these will keep a record of everyone's id / interests
y_participants = {} # theres will keep a record of everyone's id / interests.

remaining_x_pool = {} # remaining suitors will go here.
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


# Propose function - needs work
def propose(x_id): # x_id and y_id represent their names/#'s/ids.
    # THE FIRST ELEMENT IS X_ID, NOT X'S PREFERENCE.

    
    # First check X's first preference.
    y_id = x_participants[x_id][2] # does not start at 0, 1 is X's id, so 2 is first interest.
    #print("X_PREFERENCE:")
    #print(y_id)

    # See if X's first preference is available.
    try:
        something = paired[y_id] # IF TAKEN ....
        # If X's first preference is paired elsewhere, see if Y would
        # prefer X over their current partner.
        for i in y_participants[y_id]: # iterate over Y's preferences
            if i == x_id: # if X comes up first, pair Y with X instead...
                remaining_x_pool.append(paired[y_id])
                # send Y's current partner back to the pool.
                paired[y_id] = x_participants[x_id] # pair X list with Y.
                remaining_x_pool.pop(0) # remove this suitor from the pool.
                print("X USURPS ANOTHER GUY!")
        return                
    # IF FREE/AVAILABLE...
    except:
        paired[y_id] = x_id # simple. Pair X and Y.
        remaining_x_pool.pop(0)# remove x from the pool.
        print("X PAIRS WITH UNMATCHED Y!")
        return

    

for i in range(0, int(num_participants/2)):
    x_participants[i] = makeParticipantXInterests( num_participants )
   # x_participants[i].insert(0,i) # add a label to make sure we keep track of the suitors.
    y_participants[i] = makeParticipantYInterests( num_participants )

    


# initialize remaining X participants into pool
index = 0 # first individual gets ID 0.
for x in x_participants:
    remaining_x_pool[index] = x_participants[x] #
    index += 1

print("X's (first value is x id, rest is their preferences in descending order)")
for x in remaining_x_pool:
    print(remaining_x_pool)

print("Y's, in order of descending preference for X's)")
for y in y_participants:
      print(y_participants[y])
    
#print(remaining_x_pool[2])

print("START PROPOSALS!")


while len(remaining_x_pool) > 0:
    for x in remaining_x_pool: # go through each suitor in the pool
        #print(x)
        propose(x)


print("HERE ARE THE MATCHES:")
for k, v in paired.items():
    print(k, v)
