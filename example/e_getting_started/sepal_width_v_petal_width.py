import os
from example.e_data.fetch_data import load_iris_data
import matplotlib.pyplot as plt
import seaborn as sns

df, target_name = load_iris_data()

os.makedirs("plots", exist_ok=True)

plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df,
    x='sepal width',
    y='petal width',
    hue=target_name,
    style=target_name,
    s=90
)

plt.title('Iris Species: Sepal Width vs Petal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Petal Width (cm)')
plt.legend(title='Iris Species')
plt.grid(True)
plt.savefig('example/e_getting_started/plots/sepal_width_v_petal_width.png', dpi=150)
plt.close()