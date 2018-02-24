# # # # # # # # # # # # # # # # # # # # # # # #
# Gale - Shapley Algorithm
# Christopher Kelly 
# Spring 2018       
# INPUT: Amount of Participants
# OUTPUT: A Stable-Matched Set of X-Y pairs
# EXAMPLE: ./gs-lab0.py 25
#

import sys
import time
import numpy
num_participants = sys.argv[1]
# Even numbers only!
# This number represents suitors + girls. Half represents suits, half
# represents girls.

print("Number of participants:")
print(num_participants)

x_participants = {} # these will keep a record of everyone's id / interests
y_participants = {} # theres will keep a record of everyone's id / interests.

remaining_x_pool = {} # remaining suitors will go here.
paired = {} # complete pairs go here.

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
    y_id = x_participants[x_id][0]
    #print("X_PREFERENCE:")
    #print(y_id)

    # See if X's first preference is available.

    if y_id in paired: # IF TAKEN ....
        
        # If X's first preference is paired elsewhere, see if Y would
        # prefer X over their current partner.

        # IF Y Prefers this new X over their current partner, switch!
        for y in y_participants:
                
                remaining_x_pool[paired[y_id]] = x_participants[paired[y_id]] # send Y's current partner back to the pool.
                print(str(x_id) + " USURPS " + str(paired[y_id]))
                paired[y_id] = x_id # pair X list with Y.
                remaining_x_pool[x_id].pop(0)
                del remaining_x_pool[x_id] # remove from participant pool
                return
         
           
    else:  # IF FREE/AVAILABLE...
        paired[y_id] = x_id # simple. Pair X and Y.
        del remaining_x_pool[x_id]
        print(str(x_id) + " PAIRS WITH UNMATCHED " + str(y_id))
        print(remaining_x_pool)
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
print(remaining_x_pool)

print("Y's, in order of descending preference for X's)")
for y in y_participants:
      print(y_participants[y])
    
print("TESTING X:")
print(remaining_x_pool[0])
print(remaining_x_pool[1])
print(remaining_x_pool[2])
print(remaining_x_pool[3])
print(remaining_x_pool[4])
print("START PROPOSALS!")


start= time.time()

while len(remaining_x_pool) > 0:
    #print(next(iter(remaining_x_pool)))
    propose(next(iter(remaining_x_pool)))

print("HERE ARE THE MATCHES:")
for k, v in paired.items():
    print(k, v)

print(remaining_x_pool)
end = time.time()
print (str(end - start) + " seconds.")
