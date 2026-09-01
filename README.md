\# Household Energy Consumption Prediction



This project is a machine learning based system that predicts household electricity consumption using daily energy consumption data.



The main idea of this project is to use previous energy consumption, average voltage, and average current to predict the energy consumed on a particular day. The project also includes a simple electricity bill calculator that compares the bill based on actual and predicted consumption.



\## About the Project



Electricity consumption can vary from day to day depending on the usage of electrical appliances and other factors.



In this project, I used household electricity consumption data and applied Linear Regression to predict daily energy consumption. The predicted values are then compared with the actual values to check how well the model performs.



Along with prediction, the program can also calculate an estimated electricity bill for a selected number of days.



\## Dataset



The dataset used in this project is based on household electricity consumption data.



The dataset used for the project contains the following information:



\- Day

\- Previous Day Energy Consumption (kWh)

\- Average Voltage (V)

\- Average Current (A)

\- Actual Energy Consumption (kWh)



The dataset contains 100 days of data.



The first day does not have a previous-day consumption value, so that row is removed before training the model. This leaves 99 usable records for the prediction model.



\## Machine Learning Model



I used \*\*Linear Regression\*\* for this project.



The model uses three input features:



\- Previous Day Energy Consumption

\- Average Voltage

\- Average Current



The model predicts:



\- Actual Energy Consumption (kWh)



The available data is divided into training and testing data:



\- 80% for training

\- 20% for testing



After training, the model predicts the energy consumption for the test data and the results are compared with the actual values.



\## Model Performance



The model is evaluated using four common regression metrics:



\- Mean Absolute Error (MAE)

\- Root Mean Squared Error (RMSE)

\- R² Score

\- Mean Absolute Percentage Error (MAPE)



The current results are:



| Metric | Result |

|---|---:|

| MAE | 0.23 kWh |

| RMSE | 0.29 kWh |

| R² Score | 0.9996 |

| MAPE | 0.61% |



These values are based on the current dataset and model implementation.



\## Graphs



The project generates two graphs to understand the model predictions.



\### Actual vs Predicted Energy Consumption



This graph shows the difference between the actual energy consumption and the energy predicted by the model.



!\[Actual vs Predicted](graphs/actual\_vs\_predicted.png)



\### Prediction Error



This graph shows the prediction error for the test data.



!\[Prediction Error](graphs/prediction\_error.png)



\## Electricity Bill Calculator



I also added an electricity bill calculation feature to the program.



After the prediction is completed, the user can enter the number of days for which the bill needs to be estimated.



For example:



\- 10 days

\- 30 days

\- 60 days

\- 90 days



The program then calculates:



\- Total actual energy consumption

\- Total predicted energy consumption

\- Estimated bill from actual consumption

\- Estimated bill from predicted consumption

\- Difference between the two bills



The bill calculation uses the tariff rates defined for this project.



\## Example



For a selected period of 30 days, the current program produced:



\- Actual consumption: 1203.38 kWh

\- Predicted consumption: 1204.74 kWh

\- Actual estimated bill: ₹6236.32

\- Predicted estimated bill: ₹6244.86

\- Difference: ₹8.54



The values may change if the dataset or model is changed.



\## Project Structure



```text

energy-consumption-prediction/

│

├── code/

│   └── energy\_prediction.py

│

├── data/

│   └── energy\_100\_days\_dataset.csv

│

├── graphs/

│   ├── actual\_vs\_predicted.png

│   └── prediction\_error.png

│

├── results/

│   ├── model\_metrics.txt

│   └── prediction\_results.csv

│

└── README.md



