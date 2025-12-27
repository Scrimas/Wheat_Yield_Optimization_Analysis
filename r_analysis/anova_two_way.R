# Wheat Yield Analysis
# Context: Bio-statistics L3
# Objective: Determine the effect of Wheat Type and Fertilizer on Yield.

# 1. Data Loading
data <- read.csv("../data/wheat_yield_data.csv")

data$wheat_type <- as.factor(data$wheat_type)
data$fertilizer <- as.factor(data$fertilizer)

# 2. Assumption Checks (Pre-conditions) 
# A. Normality of residuals (Shapiro-Wilk per group)
shapiro_by_group <- tapply(data$yield, 
                           interaction(data$wheat_type, data$fertilizer), 
                           shapiro.test)
print(shapiro_by_group)

# B. Homogeneity of Variances (Bartlett's Test)
# H0: Variances are equal across groups.
bartlett_res <- bartlett.test(yield ~ interaction(wheat_type, fertilizer), data=data)
print(bartlett_res)
# p-value = 0.1034 (> 0.05) -> H0 Accepted .

# 3. Two-Way ANOVA 
# Model: yield ~ wheat + fertilizer + wheat:fertilizer
model <- aov(yield ~ wheat_type * fertilizer, data = data)

# 4. Results & Interpretation
print(summary(model))

# Key Findings from PDF :
# - Wheat Effect: Significant (***)
# - Fertilizer Effect: Significant (***)
# - Interaction: Significant (***) -> The effect of fertilizer depends on the wheat type.
