# Temperature and Ice Cream Sales

**CS 633 · Data Mining · Spring 2024**  
**Collaborators:** Carolin Hoering and Michaelina King

## Business question

Can temperature help explain changes in ice cream sales and inform stocking decisions?

## Analysis

- Used a [Kaggle temperature and ice cream sales dataset](https://www.kaggle.com/datasets/raphaelmanayon/temperature-and-ice-cream-sales) and referenced a [published regression notebook](https://www.kaggle.com/code/nishnaparia/temperatures-v-s-ice-cream-profits-regression) for the baseline workflow.
- Fit simple linear regression with a 70/30 train/test split and plotted observed values against fitted values.
- Explored season and city groupings. The season label was derived from temperature, so those groupings cannot establish an independent calendar-season effect.

## What the analysis showed

The coursework reported a positive fitted slope of about 1.19 outcome units per recorded temperature unit. The report alternates between sales and profit terminology, so the coefficient should be read in the source outcome's recorded units. An observational fit alone does not establish the effect of temperature on profit. For inventory planning, I would validate against dated sales records and compare performance on later periods.

[Run the companion Python demo](../examples/ice-cream/README.md). It demonstrates the workflow with simulated data.

[Back to portfolio](../README.md)
