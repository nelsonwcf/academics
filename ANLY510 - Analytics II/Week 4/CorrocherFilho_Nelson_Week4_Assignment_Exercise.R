# Setting up the environment
setwd("C:/Users/corrocherfilhonw/Dropbox/Harrisburg/ANLY510/Week4")
install.packages("caret")

# Loading the correct "cars" databaset
library("caret")
data(cars)

# Checking if the cars is the correct dataset
# Note: this dataset has different fields from the version in the documentation (www.amstat.org/publications/jse/v16n3/datasets.kuiper.html)
View(cars)

# Calculating the correlation matrix to eliminate highly correlated columns for the regression
carscor <- cor(cars)
carscor

# Making it easier to visualise
carscor.df <- data.frame(carscor)
View(carscor.df)
;
# Finding and removing linear combos (columns that are combinations of other columns)
findLinearCombos(cars)
carsl<-cars[,c(-15,-18)]

# Assigning a value to the seed. If we need to replicate the data partition, we can use the same value
set.seed(2817239)

# Partition the data into training and testing
carsl_sv<-createDataPartition(cars$Price,p=.75,list=FALSE)
carsl_train <- carsl[carsl_sv,]
carsl_test <- carsl[-carsl_sv,]

# Create the linear model using the training dataset
carsl_lm <- lm(carsl_train$Price ~ ., data = carsl_train) #Obs: . means all other variables
summary(carsl_lm)

# Saturn -> NA. Need to remove it to fix the Multicollinearity.
carsl_lm <- lm(carsl_train$Price ~ .-Saturn, data = carsl_train)

# Checking the residuals
summary(carsl_lm$residuals)
hist(carsl_lm$residuals) 

# Now we run the prediction using the model on the test data
carsl_p <- predict(carsl_lm  , carsl_test)
carsl_p.df <- data.frame(carsl_p)
View(carsl_p.df)

# Now comparing the predicted values to the real ones
summary(carsl$Price)
summary(carsl_train$Price) 
summary(carsl_test$Price) 
summary(carsl_p)

# Calculating and comparing the mean of the squares of the predictions minus the actuals
carsl_train$prediction <- predict(carsl_lm,carsl_train) 
carsl_test$prediction <- predict(carsl_lm,carsl_test) 
mean((carsl_train$prediction - carsl_train$Price)^2)
mean((carsl_test$prediction - carsl_test$Price)^2)