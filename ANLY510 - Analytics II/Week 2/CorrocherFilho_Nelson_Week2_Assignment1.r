#setwd("C:/Users/Nelson Corrocher/R/ANLY510/Week2") # Home computer folder
setwd("C:/Users/corrocherfilhonw/Dropbox/Harrisburg/ANLY510/Week2") # Job computer folder

# Part 1

# Creates a vector with 577 "1"s and 323 "0"s
# "1"s represents positive vote intention and "0"s the negative
sampleVector <- c(rep(1, times = 577),rep(0, times = 900 - 577))

sizeSample <- 900 #Sample Size
meanSample <- mean(sampleVector) #mean of sample
standardDeviationSample <- sd(sampleVector) # sd of sample
standardErrorSample <- standardDeviationSample / sqrt(sizeSample) # se of sample

# 95% Confidence Interval = 1.96
left <- (meanSample - 1.96 * standardErrorSample) * sizeSample
right <- (meanSample + 1.96 * standardErrorSample) * sizeSample

left
right

# Part 2A
# Comparing population mean to the sample mean (one-sample t-Test) 
# Hipothesis
# H0: xmean = 90;
# Ha: xmean > 90 (one tailed);

# Variables
pmean <- 90
xmean <- 86.35
xsd <- 23.90
xn <- 250

t <- ((xmean - pmean) / xsd) * sqrt(xn); # t -> value of the one-sample t-test
df <- xn - 1; # df -> degrees of freedom
a <- 0.05 # a -> confidence interval

# This is the critical value from the t-student table
tv <- qt(a,df,lower.tail = FALSE) 

t
tv

#In part A (250 customers surveyed), since t < tv, we can't reject the null hipothesis.

# Part 2B
# Comparing population mean to the sample mean (one-sample t-Test) 
# Hipothesis
# H0: xmean = 90;
# Ha: xmean > 90 (one tailed);

# Variables
pmean <- 90
xmean <- 88.53
xsd <- 18.29
xn <- 500

t <- ((xmean - pmean) / xsd) * sqrt(xn); # t -> value of the one-sample t-test
df <- xn - 1; # df -> degrees of freedom
a <- 0.05 # a -> confidence interval

# This is the critical value from the t-student table
tv <- qt(a,df,lower.tail = FALSE) 

t
tv

#Again, since t < tv, we can't reject the null hipothesis.

#Part 3
USArrests_Coasts <- read.csv("USArrests_Coasts.csv")

head(USArrests_Coasts)

# Are East Coast states more violent than others?
oneway.test(Murder ~ East.Coast, USArrests_Coasts, var.equal = TRUE)
oneway.test(Assault ~ East.Coast, USArrests_Coasts, var.equal = TRUE)
oneway.test(Rape ~ East.Coast, USArrests_Coasts, var.equal = FALSE)

#None of he cases the p-value was below 0.05, so none of the null hipothesis that the mean is equal can be rejected.
#Obs: In the third test, Rape, F suggests that the variance may not be the same so I changed var.equal to FALSE.
#Even so, the p-value still remains above 0.05. 