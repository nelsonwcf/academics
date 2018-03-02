setwd("C:/Users/corrocherfilhonw/Dropbox/Harrisburg/ANLY530 - Machine Learning I/Online Class 2")

ex3data <- read.csv("Ch4Ex3.csv")

## Function to calculate the entropy of the set
entropy <- function(set) {
  ent <- 0
  for (elem in unique(set)) {
    ent <- ent + (t <- sum(set == elem) / length(set)) * (log2(t)) * (-1)
  }
  return (ent)    # Note: the return parameter must always be encased in parentesis
}

gini <- function(set) {
  gin <- 0
  for (elem in unique(set)) {
    gin <- gin + (sum(set == elem) / length(set)) ^ 2
  }
  gin <- 1 - gin
  return (gin)
}

binning <- function(contset, targetset) {
  df <- data.frame(contset = contset, targetset = targetset)
  df <- df[with(df, order(contset)),]
  f <- data.frame(greaterThan = double()) # Best way to initialize a data.frame - empty vector of a certain type
  
  for (i in 1:(length(contset) - 1)) {
    if (df$targetset[i] != df$targetset[i + 1])
      f <- rbind(f, data.frame(greaterThan = (df$contset[i] + df$contset[i+1]) / 2))
  }
  
  b <- data.frame(AGE = integer(), BINS = factor())
  
  counter <- length(f)
  for (i in (length(contset)):1) {
    if (counter > 1) {
      if (df$contset[i] > f$greaterThan[counter])
        b <- rbind(b, data.frame(AGE = df$contset[i], BINS = as.factor(paste(">=", f$greaterThan[counter]))))
      else {
        counter <- counter - 1
        b <- rbind(b, data.frame(AGE = df$contset[i], BINS = as.factor(paste(">=", f$greaterThan[counter]))))
      }
    } else {
      if (df$contset[i] > f$greaterThan[counter])
        b <- rbind(b, data.frame(AGE = df$contset[i], BINS = as.factor(paste(">=", f$greaterThan[counter]))))
      else
        b <- rbind(b, data.frame(AGE = df$contset[i], BINS = as.factor(paste("<", f$greaterThan[counter]))))
    }
  }
  b
}
entropy(ex3data$ANNUAL_INCOME)

gini(ex3data$ANNUAL_INCOME)

binning(ex3data$AGE, ex3data$ANNUAL_INCOME)