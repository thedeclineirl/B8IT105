# ##################################################### #
# Student Name:   Thomas Higgins
# Student Number: 10544739
# Course title:   Programming for Big Data         
# Course ID:      B8IT105
# Assignment:     CA05
# 
# Created:        2020-05-11
# Editted:        2020-05-31
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


mean(data$cnt)
sd(data$cnt)

# data reorganising



# to keep the actual date I'm going to make the data into number
data$Date <- as.numeric(substr(gsub("-", "", data$timestamp), 1, 9))
# numeric categorical data for correlation
data$Year <- lubridate::year(data$timestamp)
data$Hour <- lubridate::hour(data$timestamp)
data$Day <- lubridate::day(data$timestamp)
data$wDay <- lubridate::wday(data$timestamp)
data$Month <- lubridate::month(data$timestamp)
str(data)

# check for errors before ddropping uneeded columns
unique(data$Year)
unique(data$Month)
unique(data$Day)
unique(data$wDay)
unique(data$Hour)

# drop the original timestamp
data$timestamp <- NULL
str(data)


# Plots using R standard library 
options(repr.plot.width=15, repr.plot.height=6)

hist(data$cnt, col=3, main="Histogram of London Bike Rentals")

scatter.smooth(data$hum,data$cnt, col=5, main="Effect of Humidity on Bike Rentals")

scatter.smooth(data$wDay,data$cnt, col=3, main="Bike Rentals by weekday")

scatter.smooth(data$Year,data$cnt, col=12, main="Bike Rentals by Year")

plot(data$wDay, data$cnt, col = rep(data$Year), pch = 19)
legend("topleft", legend = unique(data$Year), col = unique(data$Year), pch = 19, bty = "n")


# Plots using ggplot2

ggplot(data,aes(x=cnt,fill=cnt)) + geom_area(fill="Red")

ggplot(data)
?ggplot2

#To figure out if the temperature is in fahrenheit or celsius
#I know it's London, they use celsius, but it never hurts to confirm
ggplot(data, aes(x=data$Month, y=data$t1),col(3)) + geom_boxplot(fill="blue") + 
  ggtitle("Temperature over Months") + ylab("Temperature (units ?)") + xlab("Month")

# table of 
table(data$Month, data$season)



ggplot(data, aes(x=season, y=cnt)) + geom_area(fill="slateblue") + 
  ggtitle("Temperature over Months") + ylab("Temperature (units ?)") + xlab("Month")

boxplot(data$cnt, main="cnt", col="2")
boxplot(data$t1, main="T1", col="3")
boxplot(data$t2, main="T2", col="4")
boxplot(data$t1,data$t2,main='T1 vs T2',col = 'orange')
?boxplot
        
