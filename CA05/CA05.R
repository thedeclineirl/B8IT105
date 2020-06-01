# ##################################################### #
# Student Name:   Thomas Higgins
# Student Number: 10544739
# Course title:   Programming for Big Data         
# Course ID:      B8IT105
# Assignment:     CA05
# 
# Created:        2020-05-11
# Editted:        2020-06-01
# ##################################################### #

# install packages if not already installed
if (!require('lubridate')) install.packages('lubridate')
if (!require('ggplot2')) install.packages('ggplot2')

# load libraries
library(lubridate)
library(ggplot2)


setwd("C:/Users/GBKXN/OneDrive - Bayer/Code/github/B8IT105/CA05")
# import data
data<-read.csv("london_merged.csv")

# examine data
head(data)
tail(data)
summary(data)
str(data)

# check for missing data
table(is.na(data))

#examine the range of the cnt column 
min(data$cnt)
max(data$cnt)
mean(data$cnt)
sd(data$cnt)


# data reorganisation

# convert the date to a number
data$Date <- as.numeric(substr(gsub("-", "", data$timestamp), 1, 9))

# numeric categorical data for correlation
data$Year <- lubridate::year(data$timestamp)
data$Hour <- lubridate::hour(data$timestamp)
data$Day <- lubridate::day(data$timestamp)
data$wDay <- lubridate::wday(data$timestamp)
data$Month <- lubridate::month(data$timestamp)
str(data)

# check for errors/unexpected before dropping unneeded columns
unique(data$Year)  # expected 2015:2017
unique(data$Month) # expected 1:12
unique(data$Day)   # expected 1:31
unique(data$wDay)  # expected 1:7
unique(data$Hour)  # expected 0:23

# drop the original timestamp
data$timestamp <- NULL
str(data)

# create plots 
options(repr.plot.width=15, repr.plot.height=6)

hist(data$cnt, col=3, main="Histogram of London Bike Rentals")

scatter.smooth(data$hum,data$cnt, col=5, main="Effect of Humidity on Bike Rentals")

scatter.smooth(data$wDay,data$cnt, col=3, main="Bike Rentals by weekday")

scatter.smooth(data$Year,data$cnt, col=12, main="Bike Rentals by Year")

ggplot(data,aes(x=Month,y=cnt,fill=Year))+geom_col()+ggtitle("Bike rental by Month & Year")+xlab("Month")+ylab("count")
