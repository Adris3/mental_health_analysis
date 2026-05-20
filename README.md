# Mental Health & Social Media Usage Analysis

Data: https://www.kaggle.com/datasets/sharmajicoder/gen-z-social-media-usage-dataset

## Project Overview
Comprehensive statistical analysis of the relationship between social media consumption patterns and mental health outcomes. This project demonstrates advanced data analysis techniques including exploratory data analysis (EDA), statistical hypothesis testing, and trend analysis on a 1M-row dataset.

## Problem Statement
Understanding how social media usage impacts mental health is increasingly important. This analysis investigates key factors affecting mental health scores across demographics, usage patterns, and addiction levels using rigorous statistical methods.

## Dataset
- **Size**: 1,000,000 records
- **Features**: 13 variables including age, gender, country, daily usage hours, platform, purpose, addiction level, and mental health scores
- **Data Quality**: Pre-cleaned dataset with consistent encoding

## Methodology

### 1. Exploratory Data Analysis (EDA)
- Distribution analysis of key metrics (mental health, usage hours, age)
- Demographic breakdowns by gender, country, and purpose
- Correlation matrix analysis to identify relationships

### 2. Statistical Testing
Validated EDA findings using hypothesis tests:
- **T-Tests**: Night usage impact on mental health (effect size: Cohen's d)
- **ANOVA**: Group comparisons across categorical variables (gender, purpose, addiction level)
- **Correlation Significance**: Pearson correlation testing with p-value thresholds

### 3. Trend Analysis
Generated visualizations and reports for:
- Mental health by daily usage intensity
- Mental health across countries (top 10)
- Mental health by addiction level
- Mental health by age group

## Key Findings
- **Daily Usage Impact**: Mental health scores decrease significantly with higher daily usage (Low: 8.02 → High: 4.12)
- **Addiction Relationship**: Strong negative correlation between addiction level and mental health
- **Statistical Significance**: All major factors showed p < 0.05, confirming non-random relationships
- **Demographics**: Mental health patterns vary across countries and age groups

## Technologies & Tools
- **Python 3**: Data processing and analysis
- **Pandas**: Data manipulation and aggregation
- **NumPy**: Numerical computations
- **Matplotlib & Seaborn**: Data visualization
- **SciPy**: Statistical testing (ANOVA, t-tests, correlation analysis)
- **Jupyter Notebooks**: Interactive analysis and documentation

## Project Structure
