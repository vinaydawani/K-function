# Point pattern analysis with Ripley's K-function
Implementation of K-function in python for point pattern analysis. The algorithm tells us that whether points are clustered together and at what distance they start to seem like randomly distributed.
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/vinaydawani/K-function/master)

## Requirements
This program uses common analysis libraries like [matplotlib](https://matplotlib.org), [numpy](https://numpy.org), [GDAL](https://gdal.org/python/), etc.

## Usage
```
% python3 kfunction_main.py
```
#### optional args
* -sim \<value\>: Define the number of simulations.
```
% python3 kfunction_main.py -sim 10
```

## Result
Projected point data --
![point-data][points]

K-function Simulations --
![Kfunc-graph][kfunc]

[points]: Images/points.png
[kfunc]: Images/sim.png
