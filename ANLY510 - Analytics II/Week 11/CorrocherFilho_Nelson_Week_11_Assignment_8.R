## Init
setwd("~/Dropbox/Harrisburg/ANLY510/Week 11")
# install.packages(c("rpart","rpart.plot","RColorBrewer","rattle"))
library(rpart)
library(rpart.plot)
library(RColorBrewer)
library(rattle)
set.seed(1)

## Example

train <- read.csv("train.csv")
test <- read.csv("test.csv")
str(train) # Notice that there is no Survived variable in test because this is the variable to be predicted
tree <- rpart(Survived ~ Pclass + Sex + Age, data = train, method = "class")
fancyRpartPlot(tree)
pred <- predict(tree,test,type="class")
pred
pruned <- prune(tree, cp = 0.01)
pruned

## Part 1

# Data downloaded from https://www.kaggle.com/uciml/student-alcohol-consumption
# Definition for the fields are also in that page

d1=read.table("student-mat.csv",sep=";",header=TRUE)
d2=read.table("student-por.csv",sep=";",header=TRUE)
d3=merge(d1,d2,by=c("school","sex","age","address","famsize","Pstatus","Medu","Fedu","Mjob","Fjob","reason","nursery","internet"))
print(nrow(d3)) # 382 students

# Sampling
index <- sample(1:nrow(d3), size = 2/3*nrow(d3))
train <- d3[index,]
test <- d3[-index,]

tree <- rpart(Dalc.x ~ romantic.x + goout.x + sex, data = d3, method = "class")
fancyRpartPlot(tree)
pred <- predict(tree,test,type="class")
pred

tree <- rpart(Dalc.x ~ age + Pstatus + failures.x, data = d3, method = "class")
fancyRpartPlot(tree)
pred <- predict(tree,test,type="class")
pred

## Part 2

# Comparing the results using a regular linear model
linm <- lm(Dalc.x ~ romantic.x + goout.x + sex, data = d3)
summary(linm)


linm <- lm(Dalc.x ~ age + Pstatus + failures.x, data = d3)
summary(linm)

# Neither of the selected variables seems to explain well the reason for students to become heavy drinkers
# in neither of the methods. Based on the results, seems like both functions treat heavy drinkers somewhat
# like outliers.
