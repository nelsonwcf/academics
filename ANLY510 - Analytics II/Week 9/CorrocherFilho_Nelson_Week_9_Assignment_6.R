# Setting the environment
setwd("C:/Users/corrocherfilhonw/Dropbox/Harrisburg/ANLY510/Week 9")

# Part 1
nile.ts <- ts(Nile, start = 1, frequency = 10)
nile.hw1 <- HoltWinters(nile.ts, gamma = FALSE)
plot(nile.ts)
plot(nile.hw1)
nile.p <- predict(nile.hw1, n.ahead = 10)
ts.plot(nile.ts, nile.p)

# Part 2
ap <- ts(AirPassengers, start = 1, frequency = 12)
ap.hw <- HoltWinters(ap, beta = 1, alpha = 1)  ##
plot(ap.hw)

ap.hw <- HoltWinters(ap, beta = FALSE)  ## The time series will use exponential smoothing
plot(ap.hw)


ap.hw <- HoltWinters(ap, gamma = FALSE) ## The time series becomes shifted by one period
plot(ap.hw)


ap.hw <- HoltWinters(ap) ## Includes cycles and seasonal effects
plot(ap.hw)

# Plot 24 periods prediction
ap.p <- predict(ap.hw, n.ahead = 24)
ts.plot(ap, ap.p) 

# Part 3
tmp <- EuStockMarkets[,2] # Column SMI - Switzerland
stock.ts <- ts(tmp, start = 1, frequency = 260) # Frequency is complicated here because there is no cycle here
stock.hw <- HoltWinters(stock.ts)
plot(stock.hw)
stock.hw <- HoltWinters(stock.ts, beta = FALSE, gamma = FALSE) # No cycle, no seasonality
plot(stock.hw)
stock.p <- predict(stock.hw, n.ahead = 265)
ts.plot(stock.ts, stock.p) # Straight line, which may be explained by the fact there is no cycle or seasonality, so it can't be predicted

