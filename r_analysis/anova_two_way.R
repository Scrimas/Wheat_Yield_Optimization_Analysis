data <- read.csv("../data/wheat_yield_data.csv")

data$wheat_type <- as.factor(data$wheat_type)
data$fertilizer <- as.factor(data$fertilizer)

bartlett_result <- bartlett.test(yield ~ interaction(wheat_type, fertilizer), data=data)
print(bartlett_result)

model <- aov(yield ~ wheat_type * fertilizer, data = data)


print(summary(model))
