import numpy as np

apple_stock = [38.38222885, 34.55907822, 36.03437042, 35.95417023, 36.63956451, 37.26177216, 37.38086700, 37.01386261, 36.45728683, 37.20344162, 37.65793991, 37.88154221, 38.11487198, 37.25934601, 37.41003036, 37.11351776, 38.34333038, 37.98849106, 37.59475327, 40.16376877, 40.45300674, 40.47245026, 41.62205887, 42.33419800, 42.34877777, 41.54671860, 41.59553528, 41.35632706, 41.71270752, 41.53939438, 41.69073868, 41.59797287, 41.72246552, 41.99096680, 41.75419617, 42.22041702, 42.52796555, 42.55237579, 42.68418503, 42.26435089, 42.70859909, 42.92338943, 42.84527588, 42.59875488, 42.10569000, 42.20576477, 43.66787338, 44.15849686, 44.35376358, 44.84682083, 45.43020248, 45.89398193, 45.53028870, 45.92815399, 47.61970139, 46.63357544, 46.06971741, 45.59374619, 46.00382233, 46.06484222, 46.36507416, 46.67995834, 47.35852432, 47.68317032, 47.76615143, 48.08591461, 48.84260559, 48.69614792, 48.96952438, 48.56189346, 48.54235840, 48.63023376, 48.63512039, 49.58219528, 49.76038361, 49.92391968, 50.64399338, 50.56588364, 50.10699081, 49.86777878, 49.94344711]
print("Type of apple_stock")
print(type(apple_stock))

apple = np.array(apple_stock)
print("Type of apple")
print(type(apple))

strategy = np.zeros(np.size(apple))
q = int(np.size(apple))
t_avg = np.copy(apple)
for x in range(q-3):
	avg = np.average(apple[x:x+3])
	if avg > apple[x+3]:
		strategy[x+3] = 1
	elif avg == apple[x+3]:
		strategy[x+3] = 0
	else:
		strategy[x+3] = -1
	t_avg[x+3] = avg
#print(t_avg)
print("The strategy array")
print(strategy)
profit = 0
for x in range(len(strategy)):
	if strategy[x] == 1:
		profit -= apple[x]
	elif strategy[x] == -1:
		profit += apple[x]

print("Pure profit in USD:", profit)

shares = np.sum(strategy)
shares += 100
print("Number of final shares:", shares)
prof_with_stx = (shares*apple[-1] + profit + 10000) - (100*apple[0] + 10000)
print("Profit along with remaining stocks accounted for:", prof_with_stx)