import pandas as pd;
import matplotlib.pyplot as plt;

series = pd.read_csv("olist_orders_dataset.csv",usecols = ["order_purchase_timestamp"], parse_dates=["order_purchase_timestamp"]);
series.groupby([(series.order_purchase_timestamp.dt.year),(series.order_purchase_timestamp.dt.month)]).count().plot(kind="bar")

plt.title("Volume de compras no site da Olist  2016-2018")
plt.ylabel("Volume de Compras")
plt.xlabel("Meses")
plt.show()