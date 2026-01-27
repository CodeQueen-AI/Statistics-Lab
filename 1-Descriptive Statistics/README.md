# 📊 **Descriptive Statistics**

Descriptive Statistics helps us describe data in a short and meaningful way

Instead of listing every value individually, we summarize data using **key measures** like **Mean**, **Median** and **Mode**


## 🔹 **Measures of Central Tendency**

Tell us **where the center of data lies**

### 1️⃣ Mean (Average)

* **Formula:**
  [
  \text{Mean (μ)} = \frac{\text{Sum of all values}}{\text{Number of values}}
  ]

* **Note:** Affected by extreme values (outliers)

**Example:**
Marks = 45, 70, 90, 60
Mean = (45 + 70 + 90 + 60) ÷ 4 = **66.25**

> “The average score of the class is 66.25”



### **2️⃣ Median (Middle Value)**

* Middle value when data is **sorted in ascending order**
* **Note:** Not affected by extreme values
* **Use:** Skewed data like income or house prices

**Example:**
Marks = 45, 70, 90, 60
Ascending: 45, 60, 70, 90
Median = (60 + 70) ÷ 2 = **65**

> “Half of the students scored below 65 and half above 65”



### **3️⃣ Mode (Most Frequent Value)**

* Number that **appears most frequently**

**Example:**
Marks = 45, 70, 70, 90, 60
Mode = **70**

> “70 is the most common score”



### **Comparison Table**

| Measure | What it shows | Example |
| ------- | ------------- | ------- |
| Mean    | Average       | 66.25   |
| Median  | Middle value  | 65      |
| Mode    | Most frequent | 70      |



### **When to use**

* **Mean** → data is normal
* **Median** → data has extreme values
* **Mode** → to find most common value



## 🔹 **Measures of Dispersion**

Tell us how much data spreads out


### 1️⃣ Variance

* **Definition:** Measures how far values are from the mean

* **Formula (Population):**
  [
  \text{Variance (σ²)} = \frac{\sum (x - \bar{x})^2}{N}
  ]

* **Symbols:**

  * x = each value
  * (\bar{x}) = mean
  * N = total values
  * Σ = sum

**Example:**
Data = 40, 50, 60
Mean = 50
Variance = ((40−50)² + (50−50)² + (60−50)²) ÷ 3 = **66.67**

> “Average squared distance from mean = 66.67”


### 2️⃣ Standard Deviation (SD)

* **Definition:** Square root of variance

* **Shows spread in original units**

* **Formula:**
  [
  \text{SD} = \sqrt{\text{Variance}} = \sqrt{\frac{\sum (x - \bar{x})^2}{N}}
  ]

**Example:**
Variance = 66.67
SD = √66.67 ≈ **8.16**

> “Most marks are within ±8.16 of the mean (50)”



### **Summary Table**

| Measure            | Formula                                 |
| ------------------ | --------------------------------------- |
| Variance           | (\frac{\sum (x - \bar{x})^2}{N})        |
| Standard Deviation | (\sqrt{\frac{\sum (x - \bar{x})^2}{N}}) |



### **Shortcut to remember**

* Variance = squared spread
* SD = spread in original units



### ✅ **Quick Notes**

**Descriptive Statistics** = **Center + Spread**

* **Center (Measures of Central Tendency):** Mean, Median, Mode
* **Spread (Measures of Dispersion):** Variance, SD

**Not included in Descriptive Statistics:**
Prediction, future estimation, machine learning → These belong to **Inferential Statistics / Data Science**

