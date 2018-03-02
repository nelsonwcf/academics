---
title: "Assignment 7"
author: "Nelson Corrocher"
date: "January 16, 2017"
output: html_document
always_allow_html: yes
---
  
  
````{r setup, include=FALSE, message = FALSE}
setwd("C:/Users/corrocherfilhonw/Dropbox/Harrisburg/ANLY510/Week 10")
knitr::opts_chunk$set(echo = TRUE)
options(digits = 2)
is.installed <- function(mypkg) {
  is.element(mypkg, installed.packages()[, 1])
}

if(!is.installed("survival")) {
  install.packages("survival")
}

if(!is.installed("coin")) {
  install.packages("coin")
}

library("survival")
library("coin")
data(glioma)
```