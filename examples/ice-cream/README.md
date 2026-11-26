# Ice Cream Sales Regression Demo

This runnable companion to the [coursework case study](../../projects/ice-cream-sales.md) uses 48 simulated observations. Each row contains a temperature in Fahrenheit and a simulated count of ice cream sales. The demo compares a temperature-only linear regression against a baseline that predicts the training-set mean.

## Run locally

From this folder, use Python 3.10 or later in a virtual environment.

```bash
python -m pip install -r requirements.txt
python analyze.py sample.csv --output regression.png --title "Temperature and ice cream sales (simulated data)"
```

| Held-out metric | Result |
| --- | ---: |
| Mean baseline MAE | 21.27 sales units |
| Linear regression MAE | 8.59 sales units |
| Linear regression R² | 0.740 |

The script trains on 33 rows and evaluates on 15 held-out rows. A lower mean absolute error (MAE) indicates a smaller average prediction error. The simulated sales were generated with a positive temperature effect plus random noise, so these results illustrate the evaluation workflow. For real sales forecast evaluation, split by date and compare against relevant seasonal baselines.

To use another CSV, provide numeric `temperature_f` and `sales_units` columns and at least 10 rows. Sales must be nonnegative and temperatures must vary.

[Back to portfolio](../../README.md)
