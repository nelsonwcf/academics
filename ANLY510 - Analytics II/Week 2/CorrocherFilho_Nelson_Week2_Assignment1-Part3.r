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