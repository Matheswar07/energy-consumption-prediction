import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

data = pd.read_csv("data/energy_100_days_dataset.csv")

print("Original number of rows:", len(data))

data = data.dropna()

print("Number of usable rows:", len(data))


X = data[["Previous Day kWh", "Average Voltage V", "Average Current A"]]
y = data["Actual Energy kWh"]

split_index = int(len(X) * 0.80)

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

model = LinearRegression()

model.fit(X_train, y_train)

print("\nLinear Regression model trained successfully!")

y_pred = model.predict(X_test)

print("\nActual vs Predicted:")

for actual, predicted in zip(y_test, y_pred):
    print(f"Actual: {actual:.2f} kWh | Predicted: {predicted:.2f} kWh")

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100

print("\nModel Evaluation:")
print(f"MAE  : {mae:.2f} kWh")
print(f"RMSE : {rmse:.2f} kWh")
print(f"R²   : {r2:.4f}")
print(f"MAPE : {mape:.2f}%")

graphs_folder = Path("graphs")
graphs_folder.mkdir(exist_ok=True)

results_folder = Path("results")
results_folder.mkdir(exist_ok=True)

results = pd.DataFrame({
    "Day": data.loc[X_test.index, "Day"],
    "Actual Energy kWh": y_test,
    "Predicted Energy kWh": y_pred
})

results["Error kWh"] = (
    results["Actual Energy kWh"] -
    results["Predicted Energy kWh"]
)

results = results.sort_values("Day")

results.to_csv(
    results_folder / "prediction_results.csv",
    index=False
)

with open(results_folder / "model_metrics.txt", "w") as file:
    file.write("Linear Regression Model Evaluation\n")
    file.write("----------------------------------\n")
    file.write(f"Training samples: {len(X_train)}\n")
    file.write(f"Testing samples: {len(X_test)}\n")
    file.write(f"MAE: {mae:.2f} kWh\n")
    file.write(f"RMSE: {rmse:.2f} kWh\n")
    file.write(f"R2: {r2:.4f}\n")
    file.write(f"MAPE: {mape:.2f}%\n")

plt.figure(figsize=(10, 5))

plt.plot(
    results["Day"],
    results["Actual Energy kWh"],
    marker="o",
    label="Actual"
)

plt.plot(
    results["Day"],
    results["Predicted Energy kWh"],
    marker="s",
    label="Predicted"
)

plt.xlabel("Day")
plt.ylabel("Energy Consumption (kWh)")
plt.title("Actual vs Predicted Energy Consumption")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(
    graphs_folder / "actual_vs_predicted.png",
    dpi=300
)

plt.show()

plt.figure(figsize=(10, 5))

plt.bar(
    results["Day"],
    results["Error kWh"]
)

plt.axhline(0, linewidth=1)

plt.xlabel("Day")
plt.ylabel("Prediction Error (kWh)")
plt.title("Energy Prediction Error")
plt.grid(True)
plt.tight_layout()

plt.savefig(
    graphs_folder / "prediction_error.png",
    dpi=300
)

plt.show()

print("\nGraphs saved successfully in the graphs folder.")
print("Prediction results saved in the results folder.")

print("\nEstimated Electricity Bill")
print("Bill is calculated using project-defined tariff assumptions.")

while True:
    try:
        n = int(input(
            f"Enter number of days for bill calculation (1-{len(data)}): "
        ))

        if n < 1 or n > len(data):
            print(f"Please enter a number between 1 and {len(data)}.")
        else:
            break

    except ValueError:
        print("Please enter a valid whole number.")

selected_data = data.iloc[:n]

actual_units = selected_data["Actual Energy kWh"].sum()

predicted_data = selected_data.copy()

predicted_data["Predicted Energy kWh"] = model.predict(
    selected_data[
        [
            "Previous Day kWh",
            "Average Voltage V",
            "Average Current A"
        ]
    ]
)

predicted_units = predicted_data["Predicted Energy kWh"].sum()


def calculate_bill(units):
    bill = 0

    if units <= 100:
        return 0

    units -= 100

    if units > 0:
        slab = min(units, 100)
        bill += slab * 2.35
        units -= slab

    if units > 0:
        slab = min(units, 200)
        bill += slab * 4.70
        units -= slab

    if units > 0:
        bill += units * 6.30

    return bill


actual_bill = calculate_bill(actual_units)
predicted_bill = calculate_bill(predicted_units)

bill_difference = predicted_bill - actual_bill

print("\nElectricity Bill Estimation")
print("---------------------------")
print(f"Selected days           : {n}")
print(f"Actual consumption      : {actual_units:.2f} kWh")
print(f"Predicted consumption   : {predicted_units:.2f} kWh")
print(f"Actual estimated bill   : ₹{actual_bill:.2f}")
print(f"Predicted estimated bill: ₹{predicted_bill:.2f}")
print(f"Bill difference         : ₹{bill_difference:.2f}")
