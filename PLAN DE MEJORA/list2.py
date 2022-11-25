
l = [0, 1, 2, 3]
m = [ 1, 4]
n = [m * l for s in m
            for v in l
             if v > 1]
print(n)