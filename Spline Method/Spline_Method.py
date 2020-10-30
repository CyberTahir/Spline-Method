import matplotlib.pyplot as plot
import math

pi = math.pi
X = [0, pi/14, 3*pi/14, 5*pi/14, 9*pi/14, 13*pi/14, pi]
dx = 0.01

c = [0, 0, 0, 0, 0, 0, 0]
d = [0, 0, 0, 0, 0, 0, 0]

plot.axis([0, pi, 0.9, 3])
plot.title('onyameee :з')

def draw(f, x0, x1, h):
    x = x0
    x_axis = []
    y_axis = []

    while x <= x1:
        x_axis.append(x)
        y_axis.append(f(x))

        x += h
    else:
        x_axis.append(x1)
        y_axis.append(f(x1))

    plot.plot(x_axis, y_axis)

def get_cube_spline(f, i):
    h = X[i] - X[i - 1]
    f1 = f(X[i - 1])
    f2 = f(X[i])

    def g(x):
        x2 = X[i] - x
        x3 = x - X[i - 1]

        return (d[i - 1] * x2 ** 3 + d[i] * x3 ** 3) / (6 * h) + (f1 - d[i - 1] * h * h / 6) * x2 / h + (f2 - d[i] * h * h / 6) * x3 / h
    
    return g

def func(x):
    return math.sin(x) * math.sqrt(x) + 1

if __name__ == '__main__':

    for i in range(1, 6):
        a = (X[i] - X[i - 1]) / 6
        b = (X[i - 1] - X[i + 1]) / 3
        c[i] = (X[i + 1] - X[i]) / 6
        d[i] = (func(X[i + 1]) - func(X[i])) / (X[i + 1] - X[i]) - (func(X[i]) - func(X[i - 1])) / (X[i] - X[i - 1])

        b -= a * c[i - 1]

        c[i] /= b
        d[i] = (a * d[i - 1] - d[i]) / b

    for i in range(5, -1, -1):
        d[i] += d[i + 1] * c[i]


    draw(func, 0, X[-1], dx)

    for i in range(1, len(X)):
        spline = get_cube_spline(func, i)
        draw(spline, X[i - 1], X[i], dx)

    plot.show()