
import matplotlib.pyplot as plt

# Takes in [placeholder] filetype as input, passes an exponential moving average noise filter on the data and outputs a num-py graph 

# 1 Process information into arrays
x = [0.0, 1.0, 2.0, 3.0] # should be time
y = [1.0, 2.0, 3.0, 4.0]

def ema (x, y, a):
    # Takes in individual x i and y data poitns. Constant a determines how "aggressive" filter is
    return ( (a * x) + ( (1 - a) * y) ) # basically this: https://blog.mbedded.ninja/programming/signal-processing/digital-filters/exponential-moving-average-ema-filter/

# 2 Pass filter onto arrays and OVERRIDE old data. 



size = len(x)
alpha = 0.5

for i in range(size - 1):
    if i == 0:
        y[i] = ema(x[i], y[i], alpha)
    else:
        y[i] = ema(x[i], y[i - 1], alpha)

plt.plot(x, y)


    

