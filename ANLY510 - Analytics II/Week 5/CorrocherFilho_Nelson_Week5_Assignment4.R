setwd("D:/Dropbox/Harrisburg/ANLY510/Week5")
library(arules)
data <- paste("# this is some test data",
              "item1, item2",
              "item1",
              "item2, item3",
              sep="\n")
cat(data)
write(data, file = "demo_basket")
tr <- read.transactions("demo_basket", format="basket", sep=",", skip = 1)
inspect(tr)

data("Groceries")
head(Groceries)
str(Groceries)
rules <- apriori(data = Groceries, parameter = list(supp = 0.01, conf = 0.08), appearance = list(default = "lhs", rhs = "whole milk"), control = list(verbose = FALSE))
rules <- sort(rules, decreasing = TRUE, by =  "confidence")
inspect(rules[1:5])

# Assigment 4
# Part 1
grd <- read.transactions("http://fimi.ua.ac.be/data/retail.dat", format="basket")
itemFrequencyPlot(grd,support=.1) #run with support .2, .3, & .5
itemFrequencyPlot(grd,support=.2)
itemFrequencyPlot(grd,support=.3)
itemFrequencyPlot(grd,support=.5)
summary(grd)
inspect(grd[1:20])
grdar <- apriori(grd,parameter=list(supp=.05,conf=.5)) 
inspect(grdar) 

# Part 2
rules <- apriori(data = grd, parameter = list(supp = 0.05, conf = 0.20), control = list(verbose = FALSE))
inspect(rules)
