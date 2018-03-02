## Init

setwd("C:/Users/corrocherfilhonw/Dropbox/Harrisburg/ANLY510");
library(cluster)
library(fpc)
library(ggplot2)

# Using mtcars data.frame
x <- mtcars[c("mpg","cyl","disp")]
x_k3 <- kmeans(x,centers=3, iter.max = 1000, algorithm = "Lloyd")

# Size of each cluster
x_k3$size

# Centers of each cluster
x_k3$centers

# Adding the clusters column to mtcars
x <- merge(mtcars,x_k3$cluster, by = 0)

# Calculating the averages of each cluster for disp, wt, and qsec
mean(subset(x, y == 1, select =c(disp))[,c("disp")])
mean(subset(x, y == 2, select =c(disp))[,c("disp")])
mean(subset(x, y == 3, select =c(disp))[,c("disp")])

mean(subset(x, y == 1, select =c(wt))[,c("wt")])
mean(subset(x, y == 2, select =c(wt))[,c("wt")])
mean(subset(x, y == 3, select =c(wt))[,c("wt")])

mean(subset(x, y == 1, select =c(qsec))[,c("qsec")])
mean(subset(x, y == 2, select =c(qsec))[,c("qsec")])
mean(subset(x, y == 3, select =c(qsec))[,c("qsec")])

# Describe each cluster in English
# A cluster is a way to group elements with certain similarities together. However, in the dataset mtcars each line
# is one different car model so clustering has limited usage in this dataset, this being difficult to describe each 
# cluster individually (again, because we selected variables just to test the tools and not to try to categorize something)
# One thing that could be said is that each cluster has cars that have similar disp, cyl and mpg. One possible use of the 
# clustering in this case would be to try to predict the four variables (since they are somewhat categorical variables) 
# in models not contained in the set by using disp, cyl and mpg. By changing the number of centers/clusters to the number 
# of categories.


## Part 2

# For this exercise I'm using a modified dataset from my company regarding types of project managers
# File attached.
pmset <- read.csv("Week 8/PMCData.csv")

# Some scatter plots
ggplot(pmset, aes(x=Budgeted_Cost, y=Yearly_Revenue)) + geom_point(shape = 3) + xlim(0,20000) + ylim(0,10000)
ggplot(pmset, aes(x=Yearly_Revenue, Current_Profit)) + geom_point(shape = 2) + xlim(0,20000) + ylim(-1,1)
ggplot(pmset, aes(x=Budgeted_Cost, Current_Profit)) + geom_point(shape = 10) + xlim(0,20000) + ylim(-1,1)
ggplot(pmset, aes(x=Budgeted_Cost, Customers)) + geom_point(shape = 7) + xlim(0,20000) + ylim(0,20)

# Running k-means. Since there are 5 classes, PMit, PM, SRPM, TSKM and Not PM, k = 5 is chosen
# First we prepare the data as kmeans don't like NAs.

pmset.sub <- pmset
pmset.sub <- subset(pmset.sub, !is.na(Budgeted_Cost))
pmset.sub <- subset(pmset.sub, !is.na(Yearly_Revenue))
pmset.sub <- subset(pmset.sub, !is.na(Current_Profit))
pmset.sub <- subset(pmset.sub, !is.na(Customers))

# Here we ran the algorithm kmeans
pmset_k5 <- kmeans(pmset.sub[,c(2,3,4,5)],centers=5, iter.max = 100, algorithm = "Lloyd")

# Size of each cluster
pmset_k5$size

# Centers of each cluster
pmset_k5$centers

# Comparing the cluster results to the categorical variable
table(pmset_k5$cluster,pmset.sub$Job)

## Part 3

# Each row represent one project manager.

# Columns are:
#   - Job: Which level the PM is (TSKM - Task Manager, PMit - Project Manager in Training, PM - Project Manager
#     SRPM - Senior Project Manager, Not PM - Internal Project PM)
#   - Budgeted_Cost: What is the total cost of projects that PMs are managing
#   - Yearly_Revenues: How much revenue the manager has generated in the current year
#   - Current_Profit: HOw profitable all projects the manager manage are (weighted)
#   - Customers: How many different customer a PM manage

# The data has been modified to hide the real number, for external use

# Each cluster was supposed to represent one Job class but as you could see on the results, it didn't match well.
# One explanation for that could be that the variables used for the classification don't explain the differences
# between seniority of PM well or there are significant differences between PMs from different segments, which was
# not accounted for. In truth, in many cases using real data the results ending up not working very well 
# and this is a good example of that. 
