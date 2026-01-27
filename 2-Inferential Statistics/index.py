# Probability
def probability(fav, total):
    return fav / total

favorable = 1
total = 6

prob = probability(favorable, total)
print('probability : ', prob)
print('Probability in % :' , prob*100, '%')

# Sample Space
sample_space = [1, 2, 3, 4, 5, 6] 
print("Sample Space:", sample_space)

# Event
event = [2, 4, 6]
print('Event :', event)

# Joint Probability
def join_probability(event_A, event_B, total_outcomes):
    join_event = list(set(event_A) & set(event_B))
    return len(join_event) / total_outcomes

event_A = [2, 4, 6]
event_B = [4, 5, 6]
total_outcomes = 6

prob = join_probability(event_A, event_B, total_outcomes)
print('Join Probability: ', prob)

# Mutually Exclusive Probability
event_A = [1, 2]
event_B = [5, 6]
total_outcomes = 6

def probability(fav , total):
    return len(fav) / total

mutual_prob = probability(event_A, total_outcomes) + probability(event_B, total_outcomes)
print("Mutually Exclusive Probability (A or B):", mutual_prob)