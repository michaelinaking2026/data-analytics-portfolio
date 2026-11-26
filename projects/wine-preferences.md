# Wine Preference Analysis

**CS 703 · Applied Data Science Capstone · Spring 2024**  
**Michaelina King**

## Business question

How could a wine retailer use product, price and rating information to improve assortment decisions and plan more relevant recommendations?

## Data preparation

- Combined separate red, white, rosé and sparkling wine listings while preserving wine type.
- Standardized column names, location labels and numeric formats. Used wine name, year and winery to check for duplicates.
- Examined distributions for price, rating and number of ratings. Created price bands, rating bands and wine age.

## Modeling and evaluation

The report documented classification approaches, including decision trees, random forest and gradient boosting, along with evaluation and monitoring plans. Ratings indicate how reviewers scored listed wines. Individual purchase histories would be needed to evaluate personalized recommendations or measure changes in sales and retention.

A useful validation step is to exclude the original rating when predicting a category derived from that rating. A split that groups repeated listings by wine would also reduce the chance of near-duplicate records appearing on both sides of the evaluation. The original input CSVs were unavailable for this portfolio, so the published case study covers the workflow without reporting model scores.

[Back to portfolio](../README.md)
