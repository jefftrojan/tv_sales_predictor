# -*- coding: utf-8 -*-


# A library for programmatic plot generation.
import matplotlib.pyplot as plt
# A library for data manipulation and analysis.
import pandas as pd
# LinearRegression from sklearn.
from sklearn.linear_model import LinearRegression

"""Import the unit tests defined for this notebook."""

import w2_unittest


path = "Data/tvmarketing.csv"

### START CODE HERE ### (~ 1 line of code)
adv = pd.read_csv(path)#None.None(None)
### END CODE HERE ###

# Print some part of the dataset.
print(adv.head())

"""##### __Expected Output__

```Python
	TV	Sales
0	230.1	22.1
1	44.5	10.4
2	17.2	9.3
3	151.5	18.5
4	180.8	12.9
```
"""

w2_unittest.test_load_data(adv)

"""`pandas` has a function to make plots from the DataFrame fields. By default, matplotlib is used at the backend. Let's use it here:"""

adv.plot(x='TV', y='Sales', kind='scatter', c='black')

"""You can use this dataset to solve a simple problem with linear regression: given a TV marketing budget, predict sales.

<a name='2'></a>
## 2 - Linear Regression in Python with `NumPy` and `Scikit-Learn`

Save the required field of the DataFrame into variables `X` and `Y`:
"""

X = adv['TV'].values# To Do
Y = adv['Sales'].values# To Do

"""<a name='2.1'></a>
### 2.1 - Linear Regression with `NumPy`

You can use the function `np.polyfit(x, y, deg)` to fit a polynomial of degree `deg` to points $(x, y)$, minimising the sum of squared errors. You can read more in the [documentation](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html). Taking `deg = 1` you can obtain the slope `m` and the intercept `b` of the linear regression line:
"""

import numpy as np
m_numpy, b_numpy = np.polyfit(X, Y, deg=1)# 

print(f"Linear regression with NumPy. Slope: {m_numpy}. Intercept: {b_numpy}")

"""*Note*: [`NumPy` documentation](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html) suggests the [`Polynomial.fit` class method](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.fit.html#numpy.polynomial.polynomial.Polynomial.fit) as recommended for new code as it is more stable numerically. But in this simple example, you can stick to the `np.polyfit` function for simplicity.

<a name='ex02'></a>
### Exercise 2

Make predictions substituting the obtained slope and intercept coefficients into the equation $Y = mX + b$, given an array of $X$ values.
"""

# This is organised as a function only for grading purposes.
def pred_numpy(m, b, X):

    # TO DO: Insert code here
    Y = m * X + b
    return Y

X_pred = np.array([50, 120, 280])
Y_pred_numpy = pred_numpy(m_numpy, b_numpy, X_pred)

print(f"TV marketing expenses:\n{X_pred}")
print(f"Predictions of sales using NumPy linear regression:\n{Y_pred_numpy}")

"""##### __Expected Output__

```Python
TV marketing expenses:
[ 50 120 280]
Predictions of sales using NumPy linear regression:
[ 9.40942557 12.7369904  20.34285287]
```
"""

w2_unittest.test_pred_numpy(pred_numpy)

"""<a name='2.2'></a>
### 2.2 - Linear Regression with `Scikit-Learn`

`Scikit-Learn` is an open-source machine learning library that supports supervised and unsupervised learning. It also provides various tools for model fitting, data preprocessing, model selection, model evaluation, and many other utilities. `Scikit-learn` provides dozens of built-in machine learning algorithms and models, called **estimators**. Each estimator can be fitted to some data using its `fit` method. Full documentation can be found [here](https://scikit-learn.org/stable/).

Create an estimator object for a linear regression model:
"""

lr_sklearn = LinearRegression()# To do

"""The estimator can learn from data calling the `fit` function. However, trying to run the following code you will get an error, as the data needs to be reshaped into 2D array:"""

print(f"Shape of X array: {X.shape}")
print(f"Shape of Y array: {Y.shape}")

try:
    lr_sklearn.fit(X, Y)
except ValueError as err:
    print(err)

"""You can increase the dimension of the array by one with `reshape` function, or there is another another way to do it:"""

X_sklearn = X[:, np.newaxis]
Y_sklearn = Y[:, np.newaxis]

print(f"Shape of new X array: {X_sklearn.shape}")
print(f"Shape of new Y array: {Y_sklearn.shape}")

"""You have already loaded your dataset into X_sklearn and Y_sklearn
Step 1: Split the data into training and testing sets use train_test_split from sklearn
The test size shoukd be 20% of the data
"""

from sklearn.model_selection import train_test_split


# Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X_sklearn, Y_sklearn, test_size=0.2)

# Check the shapes of the resulting arrays
print(f"Shape of X_train array: {X_train.shape}")
print(f"Shape of X_test array: {X_test.shape}")
print(f"Shape of Y_train array: {Y_train.shape}")
print(f"Shape of Y_test array: {Y_test.shape}")

"""Step 2: Fit the linear regression model to the training data

"""

# Fit the model to the training data
lr_sklearn.fit(X_train, Y_train)

"""
 Step 3: Make predictions using the fitted model on the testing data
"""

# Make predictions on the testing data
Y_pred = lr_sklearn.predict(X_test)#use test data from X from step 1 above)

""" Step 4: Calculate the RMSE
Using sklearn.metrics - mean_squared_error
"""

#Insert your code
from sklearn.metrics import mean_squared_error

# Calculate the mean squared error
mse = mean_squared_error(Y_test, Y_pred)

# Calculate the root mean squared error (RMSE)
rmse = np.sqrt(mse)

print("Root Mean Square Error:", rmse)

"""TO DO Create an estimator object for Random Forest and Desision Trees and compare RSMES:"""

from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error


# Create Linear Regression, Random Forest, and Decision Trees models
lr_model = LinearRegression()
rf_model = RandomForestRegressor()
dt_model = DecisionTreeRegressor()

# Fit the models to the training data
lr_model.fit(X_train, Y_train)
rf_model.fit(X_train, Y_train)
dt_model.fit(X_train, Y_train)

# Make predictions on the testing data
Y_pred_lr = lr_model.predict(X_test)
Y_pred_rf = rf_model.predict(X_test)
Y_pred_dt = dt_model.predict(X_test)

# Calculate the RMSE for each model
rmse_lr = np.sqrt(mean_squared_error(Y_test, Y_pred_lr))
rmse_rf = np.sqrt(mean_squared_error(Y_test, Y_pred_rf))
rmse_dt = np.sqrt(mean_squared_error(Y_test, Y_pred_dt))

# Create a dictionary to store the RMSEs for each model
model_rank = {
    'Linear Regression': rmse_lr,
    'Random Forest': rmse_rf,
    'Decision Trees': rmse_dt
}

# Sort the models based on their RMSEs (ascending order)
sorted_model_rank = {k: v for k, v in sorted(model_rank.items(), key=lambda item: item[1])}

print("Rank of models from the best to the worst performing and associated RMSEs:")
for model, rmse in sorted_model_rank.items():
    print(f"{model}: {rmse}")

"""The estimator can learn from data calling the `fit` function for RandomForest and Decision Trees

Compare the RSME for the three different models and rank them according to performance i.e Print out Model Rank and Associated RSME
"""



"""<a name='ex03'></a>
### Exercise 3

Fit the linear regression model passing `X_sklearn` and `Y_sklearn` arrays into the function `lr_sklearn.fit`.
"""

### START CODE HERE ### (~ 1 line of code)
lr_sklearn.fit(X_sklearn, Y_sklearn)
### END CODE HERE ###

# Obtain the slope and intercept
m_sklearn = lr_sklearn.coef_
b_sklearn = lr_sklearn.intercept_

print(f"Linear regression using Scikit-Learn. Slope: {m_sklearn}. Intercept: {b_sklearn}")

"""##### __Expected Output__

```Python
Linear regression using Scikit-Learn. Slope: [[0.04753664]]. Intercept: [7.03259355]
```
"""

w2_unittest.test_sklearn_fit(lr_sklearn)

"""Note that you have got the same result as with the `NumPy` function `polyfit`. Now, to make predictions it is convenient to use `Scikit-Learn` function `predict`.

<a name='ex04'></a>
### Exercise 4


Increase the dimension of the $X$ array using the function `np.newaxis` (see an example above) and pass the result to the `lr_sklearn.predict` function to make predictions.
"""

# This is organised as a function only for grading purposes.
def pred_sklearn(X, lr_sklearn):
    # Increase the dimension of X array
    X_2D = X[:, np.newaxis]

    # Make predictions
    Y = lr_sklearn.predict(X_2D)

    return Y

Y_pred_sklearn = pred_sklearn(X_pred, lr_sklearn)

print(f"TV marketing expenses:\n{X_pred}")
print(f"Predictions of sales using Scikit_Learn linear regression:\n{Y_pred_sklearn.T}")

"""##### __Expected Output__

```Python
TV marketing expenses:
[ 50 120 280]
Predictions of sales using Scikit_Learn linear regression:
[[ 9.40942557 12.7369904  20.34285287]]
```
"""

w2_unittest.test_sklearn_predict(pred_sklearn, lr_sklearn)

"""You can plot the linear regression line and the predictions by running the following code. The regression line is red and the predicted points are blue."""

fig, ax = plt.subplots(1,1,figsize=(8,5))
ax.plot(X, Y, 'o', color='black')
ax.set_xlabel('TV')
ax.set_ylabel('Sales')

ax.plot(X, m_sklearn[0][0]*X+b_sklearn[0], color='red')
ax.plot(X_pred, Y_pred_sklearn, 'o', color='blue')

"""<a name='3'></a>
## 3 - Linear Regression using Gradient Descent

Functions to fit the models automatically are convenient to use, but for an in-depth understanding of the model and the maths behind it is good to implement an algorithm by yourself. Let's try to find linear regression coefficients $m$ and $b$, by minimising the difference between original values $y^{(i)}$ and predicted values $\hat{y}^{(i)}$ with the **loss function** $L\left(w, b\right)  = \frac{1}{2}\left(\hat{y}^{(i)} - y^{(i)}\right)^2$ for each of the training examples. Division by $2$ is taken just for scaling purposes, you will see the reason below, calculating partial derivatives.

To compare the resulting vector of the predictions $\hat{Y}$ with the vector $Y$ of original values $y^{(i)}$, you can take an average of the loss function values for each of the training examples:

$$E\left(m, b\right) = \frac{1}{2n}\sum_{i=1}^{n} \left(\hat{y}^{(i)} - y^{(i)}\right)^2 =
\frac{1}{2n}\sum_{i=1}^{n} \left(mx^{(i)}+b - y^{(i)}\right)^2,\tag{1}$$

where $n$ is a number of data points. This function is called the sum of squares **cost function**. To use gradient descent algorithm, calculate partial derivatives as:

\begin{align}
\frac{\partial E }{ \partial m } &=
\frac{1}{n}\sum_{i=1}^{n} \left(mx^{(i)}+b - y^{(i)}\right)x^{(i)},\\
\frac{\partial E }{ \partial b } &=
\frac{1}{n}\sum_{i=1}^{n} \left(mx^{(i)}+b - y^{(i)}\right),
\tag{2}\end{align}

and update the parameters iteratively using the expressions

\begin{align}
m &= m - \alpha \frac{\partial E }{ \partial m },\\
b &= b - \alpha \frac{\partial E }{ \partial b },
\tag{3}\end{align}

where $\alpha$ is the learning rate.

Original arrays `X` and `Y` have different units. To make gradient descent algorithm efficient, you need to bring them to the same units. A common approach to it is called **normalization**: substract the mean value of the array from each of the elements in the array and divide them by standard deviation (a statistical measure of the amount of dispersion of a set of values). If you are not familiar with mean and standard deviation, do not worry about this for now - this is covered in the next Course of Specialization.

Normalization is not compulsory - gradient descent would work without it. But due to different units of `X` and `Y`, the cost function will be much steeper. Then you would need to take a significantly smaller learning rate $\alpha$, and the algorithm will require thousands of iterations to converge instead of a few dozens. Normalization helps to increase the efficiency of the gradient descent algorithm.

Normalization is implemented in the following code:
"""

X_norm = (X - np.mean(X))/np.std(X)
Y_norm = (Y - np.mean(Y))/np.std(Y)

"""Define cost function according to the equation $(1)$:"""

def E(m, b, X, Y):
    n = len(X)
    predictions = m * X + b  # Predicted values
    error = predictions - Y  # Error between predicted and actual values
    cost = np.sum(error ** 2) / (2 * n)  # Sum of squares cost function
    return cost

"""<a name='ex05'></a>
### Exercise 5


Define functions `dEdm` and `dEdb` to calculate partial derivatives according to the equations $(2)$. This can be done using vector form of the input data `X` and `Y`.
"""

def dEdm(m, b, X, Y):
    # Calculate the predicted values
    predictions = m * X + b

    # Calculate the error between predicted and actual values
    error = predictions - Y

    # Calculate the partial derivative of the cost function with respect to m
    res = np.mean(error * X)

    return res

def dEdb(m, b, X, Y):
    # Calculate the predicted values
    predictions = m * X + b

    # Calculate the error between predicted and actual values
    error = predictions - Y

    # Calculate the partial derivative of the cost function with respect to b
    res = np.mean(error)

    return res

print(dEdm(0, 0, X_norm, Y_norm))
print(dEdb(0, 0, X_norm, Y_norm))
print(dEdm(1, 5, X_norm, Y_norm))
print(dEdb(1, 5, X_norm, Y_norm))

"""##### __Expected Output__

```Python
-0.7822244248616067
5.098005351200641e-16
0.21777557513839355
5.000000000000002
```
"""

w2_unittest.test_partial_derivatives(dEdm, dEdb, X_norm, Y_norm)

"""<a name='ex06'></a>
### Exercise 6


Implement gradient descent using expressions $(3)$:
\begin{align}
m &= m - \alpha \frac{\partial E }{ \partial m },\\
b &= b - \alpha \frac{\partial E }{ \partial b },
\end{align}

where $\alpha$ is the `learning_rate`.
"""

def gradient_descent(dEdm, dEdb, m, b, X, Y, learning_rate=0.001, num_iterations=1000, print_cost=False):
    for iteration in range(num_iterations):
        # Calculate the gradients using the provided functions
        grad_m = dEdm(m, b, X, Y)
        grad_b = dEdb(m, b, X, Y)

        # Update m and b using the gradients and learning rate
        m_new = m - learning_rate * grad_m
        b_new = b - learning_rate * grad_b

        # Update m and b for the next iteration
        m = m_new
        b = b_new

        if print_cost and iteration % 100 == 0:
            cost = E(m, b, X, Y)
            print(f"Cost after iteration {iteration}: {cost}")

    return m, b

print(gradient_descent(dEdm, dEdb, 0, 0, X_norm, Y_norm))
print(gradient_descent(dEdm, dEdb, 1, 5, X_norm, Y_norm, learning_rate = 0.01, num_iterations = 10))

"""##### __Expected Output__

```Python
(0.49460408269589495, -3.489285249624889e-16)
(0.9791767513915026, 4.521910375044022)
```
"""

w2_unittest.test_gradient_descent(gradient_descent, dEdm, dEdb, X_norm, Y_norm)

"""Now run the gradient descent method starting from the initial point $\left(m_0, b_0\right)=\left(0, 0\right)$."""

m_initial = 0; b_initial = 0; num_iterations = 30; learning_rate = 1.2
m_gd, b_gd = gradient_descent(dEdm, dEdb, m_initial, b_initial,
                              X_norm, Y_norm, learning_rate, num_iterations, print_cost=True)

print(f"Gradient descent result: m_min, b_min = {m_gd}, {b_gd}")

"""Remember, that the initial datasets were normalized. To make the predictions, you need to normalize `X_pred` array, calculate `Y_pred` with the linear regression coefficients `m_gd`, `b_gd` and then **denormalize** the result (perform the reverse process of normalization):"""

X_pred = np.array([50, 120, 280])
# Use the same mean and standard deviation of the original training array X
X_pred_norm = (X_pred - np.mean(X))/np.std(X)
Y_pred_gd_norm = m_gd * X_pred_norm + b_gd
# Use the same mean and standard deviation of the original training array Y
Y_pred_gd = Y_pred_gd_norm * np.std(Y) + np.mean(Y)

print(f"TV marketing expenses:\n{X_pred}")
print(f"Predictions of sales using Scikit_Learn linear regression:\n{Y_pred_sklearn.T}")
print(f"Predictions of sales using Gradient Descent:\n{Y_pred_gd}")


#What imports do we need for Fast api
import asyncio
import uvicorn
from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException, status, Path
from pydantic import BaseModel, Field

import uvicorn
from fastapi import FastAPI, Query, status
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Define a class to represent the request body
class PredictionRequest(BaseModel):
    X: List[float]

# Define endpoint for linear regression prediction
@app.post("/predict")
def predict_sales(request: PredictionRequest):
    # Extract input data from request
    X = request.X

    # Convert input data to numpy array and reshape it
    X_array = np.array(X).reshape(-1, 1)

    # Make predictions using the best model (lr_model)
    Y_pred = lr_model.predict(X_array)

    return {"predictions": Y_pred.tolist()}


async def main():
    config = uvicorn.Config(app)
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())

