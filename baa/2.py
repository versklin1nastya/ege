print('w z x y F')
for w in 0,1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                F = ((not z) and y and x and (not w)) or ((not z) and y and (not x) and (not w)) or (z and y and x and (not w))
                if F == 1:
                    print(w, z, x, y, F)