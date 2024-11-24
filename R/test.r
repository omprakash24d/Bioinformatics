# # ?mean
# # help(mean)
# # example(mean)
# # example(probability)
# # example(boxplot)
# objects()
# x <- c(10.4, 5.6, 3.1, 6.4, 21.7);
# mean(x)
# mode(x)
# y <- c(12,23,43)
# sin(23)
# cos(54)
# sin(30)+cos(90)
# sort(x)
# sort(y)
# max(y)
# order(x)
# sort.list(x)
# pmax(x)
# pmin(y)
# x
# pmax(x)
# z=x+y
# z
# q=x/y

# sqrt(-17+0i)
# seq(7101, 7160, 1)
# seq(7101, 7160, 2)
# s <- seq(7101, 7160, 2)
# s
# sum(s)
# mean(s)
# max(s)
# min(s)
# max_min=(max(s)+min(s))
# max_min
# 7159+7101
#  temp <- x > 13
# temp
# x
# z <- c(1:3,NA); ind <- is.na(z)
# ind
# # ?Quotes
# labs <- paste(c("X","Y"), 1:5, sep=":")
# labs
# # Your playlist
# x <- c("Song1", "Song2", NA, "Song4", "Song5")

# # Rule: Only play non-missing songs (not NA)
# y <- x[!is.na(x)]
# print(y)  # Output: "Song1" "Song2" "Song4" "Song5"
# attr(x, "dim") <- c(10,10)
# cd <- c(10,10) 
# cd
# winter
#  state <- c("tas", "sa", "qld", "nsw", "nsw", "nt", "wa", "wa",
#  "qld", "vic", "nsw", "vic", "qld", "qld", "sa", "tas",
#  "sa", "nt", "wa", "vic", "qld", "nsw", "nsw", "wa",
#  "sa", "act", "nsw", "vic", "vic", "act")
# state
# stages <- c("Vegetative", "Fruiting", "Flowering", "Seedling")
# stagesf <- factor(stages)
# print(stagesf)
# stagesf_ordered <- ordered(stages, levels = c("Seedling", "Vegetative", "Flowering", "Fruiting"))
# print(stagesf_ordered)
# a <- c(3,4,2)
# a
# dim <- c(3, 5, 100)
# din
# dim
# z <- 1:1500
# z
# dim(z) <- c(3, 5, 100)
# z
# z[2, 3, 10]
# z[2, , ]
# z[, , 10]
# gene_data <- array(runif(1500), dim = c(3, 5, 100))
# gene_data
# gene_data[1, 3, 50]
# gene_data[2, , 30]
# gene_data[3, 4, ]
# # example(boxplot)
# # example(scatteredplot)
# # ?scatteredplot
# # example(ScatterPlot)
# # example(hist)
# # x <- array(1:20, dim=c(4,5))
# # x
#  Xb <- matrix(0, n, b)
# i <- array(c(1, 2, 3, 3, 2, 1), dim = c(3, 2))
# i
# x[i]
# x
# Z <- array(0, c(3, 4, 2))
# Z
# A <- array(1:24, dim = c(3, 4, 2))
# B <- array(24:1, dim = c(3, 4, 2))
# C <- array(0, dim = c(3, 4, 2))

# D <- 2 * A * B + C + 1
 Lst <- list(name="Fred", wife="Mary", no.children=3,
 child.ages=c(4,7,9))
Lst
a <-c(1:20) 
a
b <- c(40:90)
b
boxplot(a,b)
hist(a,b)
?hist
t.test(a,b)
var.test(a,b)
t.test(a, b, var.equal=TRUE)
random_integers <- sample(1:100, 5)
random_integers
random_integers1 <- sample(7:100, 5)
hist(random_integers,random_integers1)
boxplot(random_integers,random_integers1)
library()
 help.start()
x <- rnorm(50)
x
y <- rnorm(x)
y
plot(x,y)
hist(x,y)
boxplot(x,y)
ls()

