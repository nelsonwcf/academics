vecpoisson <- rpois(100,5)
mean(vecpoisson)
set.seed(198911)
vecpoisson <- rpois(100,5)
mean(vecpoisson)
rep <- 50000
nexps <- 5
rate <- 0.1
set.seed(0)
system.time(x1 <- replicate(reps,sum(rexp(n = nexps, rate = rate))))
head(x1)
require(ggplot2)
ggplot(data.frame(x1), aes(x1)) + geom histogram(aes(y=..density..)) + stat functon(fun = function(x)dgamma(x, shape = nexps, scale = 1/rate), color = red, size=2)
hist(x1)

# data manipulation

