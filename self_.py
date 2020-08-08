import numpy as np
import time

# least amount of energy (distance and speed)

# probablistic spontaneous connection between n clusters

# eat other clusters

container = []

alpha = 'abcdefghijklmnopqrstuvwxyz'

while len(container) < 4:
    if len(container) != len(container)+1:
        identity = ''
        identity = alpha[np.random.randint(0,len(alpha))] + str(np.random.randint(0,100000001))
        container.append({
            identity:[
                np.random.randint(-100000000,100000001),
                np.random.randint(-100000000,100000001),
                np.random.randint(-100000000,100000001)
            ]
        })
        if len(container) == 1:
            pass
        else:
            optimized_map = []
            action = []
            poss = [e for e in range(len(container))]
            # print(container)
            for i in (range(len(container))):
                include = [w for w in poss if w != i]
                for q in range(len(include)+1):
                    if i != q:
                        t1 = (container[i].values()[0][0] - container[q].values()[0][0]) ** 2 
                        t2 = (container[i].values()[0][1] - container[q].values()[0][1]) ** 2 
                        t3 = (container[i].values()[0][2] - container[q].values()[0][2]) ** 2 
                        cal = np.sqrt(t1+t2+t3)
                        optimized_map.append({container[i].keys()[0]:[container[q].keys()[0],cal]})
            for s in range(len(optimized_map)):
                print(optimized_map[s].keys()[0],optimized_map[s].values()[0][0],
                    optimized_map[s].values()[0][1])
            print("")
            same = []
            for d in range(len(optimized_map)):
                lock = [x for x in range(len(optimized_map)) if x != d]
                sames = [j for h in same for j in h.keys()]
                for a in range(len(lock)):
                    if optimized_map[d].keys()[0] in sames:
                        same[sames.index(optimized_map[d].keys()[0])][1].append({optimized_map[d].values()[0][0]:optimized_map[d].values()[0][1]}]})
                    else:
                        if optimized_map[d].keys()[0] == optimized_map[a].keys()[0]:
                            same.append({optimized_map[d].keys()[0]:[{optimized_map[d].values()[0][0]:optimized_map[d].values()[0][1]}]})