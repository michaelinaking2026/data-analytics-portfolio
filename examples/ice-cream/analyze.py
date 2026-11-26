"""Fit and evaluate a temperature-only sales model on a two-column CSV."""

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

FEATURE = "temperature_f"
TARGET = "sales_units"


def read_data(path):
    data = pd.read_csv(path)
    columns = [FEATURE, TARGET]
    missing = set(columns) - set(data.columns)
    if missing:
        raise ValueError(f"Missing columns: {', '.join(sorted(missing))}")
    data = data[columns].apply(pd.to_numeric, errors="coerce")
    if len(data) < 10 or not np.isfinite(data.to_numpy()).all():
        raise ValueError("Provide at least 10 rows with finite numeric values.")
    if data[FEATURE].nunique() < 2 or (data[TARGET] < 0).any():
        raise ValueError("Temperatures must vary and sales must be nonnegative.")
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", type=Path)
    parser.add_argument("--output", type=Path, default=Path("regression.png"))
    parser.add_argument("--title", default="Temperature and ice cream sales")
    args = parser.parse_args()

    try:
        data = read_data(args.csv)
    except (OSError, ValueError) as error:
        parser.error(str(error))

    x_train, x_test, y_train, y_test = train_test_split(
        data[[FEATURE]], data[TARGET], test_size=0.30, random_state=42
    )
    if x_train[FEATURE].nunique() < 2:
        parser.error("The training split must contain multiple temperatures.")

    model = LinearRegression().fit(x_train, y_train)
    baseline = DummyRegressor(strategy="mean").fit(x_train, y_train)
    predicted = model.predict(x_test)
    print(f"Training rows: {len(x_train)} | Test rows: {len(x_test)}")
    print(f"Baseline test MAE: {mean_absolute_error(y_test, baseline.predict(x_test)):.2f}")
    print(f"Regression test MAE: {mean_absolute_error(y_test, predicted):.2f}")
    if y_test.nunique() > 1:
        print(f"Regression test R²: {r2_score(y_test, predicted):.3f}")
    else:
        print("Regression test R²: undefined for a constant test outcome")
    print(f"Fitted slope: {model.coef_[0]:.2f} sales units per °F")

    line = x_train.sort_values(FEATURE)
    fig, ax = plt.subplots(figsize=(8, 4.5), layout="constrained")
    ax.scatter(x_train[FEATURE], y_train, color="#427d83", alpha=0.65, label="Training rows")
    ax.scatter(x_test[FEATURE], y_test, color="#c45b21", marker="D", label="Held-out rows")
    ax.plot(line[FEATURE], model.predict(line), color="#183353", linewidth=2, label="Fitted line")
    ax.set(title=args.title, xlabel="Temperature (°F)", ylabel="Ice cream sales (units)")
    ax.grid(alpha=0.2)
    ax.set_axisbelow(True)
    ax.legend()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    main()
