#Q1
install.packages('MASS')
library(MASS)
data(Boston)

head(Boston)

summary(Boston)

str(Boston)

help(Boston)

?Boston

mean(Boston$rm)
sd(Boston$rm)

aggregate(d[, 3:4], list(Boston$chas), mean)


#Q2
attach(mtcars)
str(mtcars)
help(mtcars)
mtcars[complete.cases(mtcars)]
str(mtcars)
str(mtcars2)
mtcars

boxplot(wt ~ cyl, col=c("red","orange","yellow"),
        main
        
        )

library(ggplot2)
ggplot2(mtcars)


