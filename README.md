#Spurious Regressions test simulation

In this project we try to test how the persistence of a time series can fool the regression to show Spurious Correlation.

The idea is to build the following $i$ AR1 process:

$$y_{i,t}=a+by_{i,t-1}+\epsilon_t$$

where $i$ is the number of AR1 process or simulations we want and t will be the lenght of each simulation.

We then choose the parameter $b$ depending on how persistent we want our time series to be.

- A $b$ between 0.3 and 0.8 give us a stationary Serie with low persistence.
- A $b$ between 0.95 and 0.99 give us a stationary Serie with high persistence.
- A $b=1$  give us a unit root process.

$a$ is a free to choose parameter depending on where we will like our simulation begin. (NOTE= in the case of unit root, it is important to be careful with this parameter)

With the normal standard errors and our parameters $a$ and $b$ we can then start to build the $y$ values for our A1 process.

The $i$ AR1 process should be each independent from one and other. So the idea is that a simple OLS regression between one half of the simulations and the other half should give us a estimator that is not statically significant.

In order to prove this idea we conduct a test.

We regress half of the simulation as dependent variables into the other half of simulations as independent variables. The OLS regression should look like:

$$y_{i}=c+kx_{i}+\epsilon_i$$

$k$ is the estimator and the program reports the proportion of times this coefficient is statically significant to a 5%.

For strong persistence process and unit root we get that the proportion for significance is very high detecting, thus, Spurious Correlation.
