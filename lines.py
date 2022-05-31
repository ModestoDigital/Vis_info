import pandas as pd;
import matplotlib.pyplot as plt;

data = pd.read_csv("olist_order_items_dataset.csv", usecols=["price"])
ndata = data.groupby((data["price"]//5)*5).count()
ndata.plot(style='k.');
plt.ylabel("volume de vendas")
plt.xlabel("preço (R$)")
plt.yscale("log")
plt.xscale("log")
plt.title("Distribuição de vendas por preço")
plt.show();
#print(ndata)