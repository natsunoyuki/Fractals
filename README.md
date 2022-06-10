# Fractals
`Fractals` is a python package for generating and visualizing fractals.

# List of Fractals Available
* Cantor box.
* Barnsley fern.
* Julia set.
* Mandelbrot set.
* Sierpinski carpet.
* Sierpinski triangle.
* Weierstrauss fractal.

# Installation
```
pip install git+https://github.com/natsunoyuki/Fractals
```

# Usage
```
import fractals

barnsley_fern = fractals.BarnsleyFern(run = True)
barnsley_fern.plot()
```

# To-do
Refactor the code - most of the classes have functionalities which can be reduced into a common parent class.

