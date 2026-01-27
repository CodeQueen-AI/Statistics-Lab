# Probability
def probability(fav, total):
    return fav / total

favorable = 1
total = 6

prob = probability(favorable, total)
print('probability : ', prob)
print('Probability in % :' , prob*100, '%')