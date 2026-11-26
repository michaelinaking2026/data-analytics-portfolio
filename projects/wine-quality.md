# Wine Quality and Chemistry

**CS 665 · Analytic Techniques · Fall 2023**  
**Michaelina King**

## Analysis question

How do the distributions of quality scores and measured properties differ across red and white Portuguese Vinho Verde wines?

## Workflow

- Imported the [Wine Quality dataset](https://www.kaggle.com/datasets/rajyellow46/wine-quality) into SAS.
- Used `PROC UNIVARIATE` to examine quality scores and `PROC SGSCATTER` to compare density, alcohol and acidity by score.
- Used `PROC SQL` to identify wines at the extremes of the residual sugar distribution and `PROC MEANS` to summarize numeric fields.

This adapted excerpt shows how the original SQL approach retrieves all wines tied for the highest measured residual sugar. It assumes the data have been imported as `WORK.WINE`.

```sas
proc sql;
    select Type, pH, Residual_Sugar
    from WORK.WINE
    where Residual_Sugar = (
        select max(Residual_Sugar)
        from WORK.WINE
    );
quit;
```

The plots and queries support exploratory comparisons. Establishing whether a chemical property predicts quality would require a defined model and held-out evaluation.

[Back to portfolio](../README.md)
