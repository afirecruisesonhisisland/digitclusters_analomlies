import numpy as np
import time

# least amount of energy (distance)

# join other clusters

container = []

alpha = 'abcdefghijklmnopqrstuvwxyz'

while len(container) < 3:
    if len(container) != len(container)+1:
        identity = ''
        identity = alpha[np.random.randint(0,len(alpha))] + str(np.random.randint(0,100000001))
        # time.sleep(5)
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
            host = []
            poss = [e for e in range(len(container))]
            for i in (range(len(container))):
                include = [w for w in poss if w != i]
                for q in range(len(include)+1):
                    host = [j for t in optimized_map for j in t.keys()]
                    if i != q:
                        t1 = (container[i].values()[0][0] - container[q].values()[0][0]) ** 2 
                        t2 = (container[i].values()[0][1] - container[q].values()[0][1]) ** 2 
                        t3 = (container[i].values()[0][2] - container[q].values()[0][2]) ** 2 
                        cal = np.sqrt(t1+t2+t3)
                        if container[i].keys()[0] in host:
                            optimized_map[host.index(container[i].keys()[0])].values()[0].append(
                                [container[q].keys()[0],cal]
                            )
                        else:
                            optimized_map.append({container[i].keys()[0]:[[container[q].keys()[0],cal]]})
            destination = []
            for s in range(len(optimized_map)):
                for h in optimized_map[s].values():
                    all_selection = []
                    for f in range(len(h)):
                        all_selection.append(h[f][1])
                    location = all_selection.index(min(all_selection))
                    final = h[location]
                    destination.append(final)
            all_keys = [n for q in optimized_map for n in q.keys()]
            for v in range(len(all_keys)):
                for p in range(len(destination)):
                    if v == p:
                        optimized_map[p][all_keys[v]] = destination[p]
            print("good")
            for z in range(len(optimized_map)):
                for o, p in optimized_map[z].items():
                    print(o, p)
            print("bad")
            
