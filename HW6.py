mport numpy as np
import matplotlib.pyplot as plt


import numpy as np

# set seed
np.random.seed(42)
# Function to compute the Mean Squared Error
def mean_squared_error(y, y_pred):
    return np.mean((y - y_pred) ** 2)

# Function to compute gradients
def compute_gradients(X, y, a, b, c):
    N = len(y)
    y_pred = a * X**2 + b * X + c
    da = (-2/N) * np.sum(X**2 * (y - y_pred))
    db = (-2/N) * np.sum(X * (y - y_pred))
    dc = (-2/N) * np.sum(y - y_pred)
    return da, db, dc

# Gradient Descent Function
def gradient_descent(X, y, a, b, c, learning_rate, iterations):
    for _ in range(iterations):
        da, db, dc = compute_gradients(X, y, a, b, c)
        a -= learning_rate * da
        b -= learning_rate * db
        c -= learning_rate * dc
    return a, b, c

# Example data
x = np.linspace(-1, 1, 100)
y = 1.5*x*x + 0.2 + 0.2*np.random.randn(100)
plt.scatter(x, y)
plt.plot(x, 1.5*x*x + 0.2, 'r-', lw=3)
plt.show()
# Initial parameters
a, b, c = 0, 0, 0
learning_rate = 0.1
iterations = 1000

# Perform Gradient Descent
a, b, c = gradient_descent(x, y, a, b, c, learning_rate, iterations)

print(f"The fitted quadratic curve is: y = {a:.2f}x^2 + {b:.2f}x + {c:.2f}")

# Plot the fitted curve
plt.scatter(x, y)
plt.plot(x, a*x*x + b*x + c, 'r-', lw=3,label='fitted curve')
plt.plot(x, 1.5*x*x + 0.2, 'g-', lw=3,label='original curve')
plt.show()
