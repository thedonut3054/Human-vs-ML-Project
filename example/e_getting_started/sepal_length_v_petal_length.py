import os
from example.e_data.fetch_data import load_iris_data
import matplotlib.pyplot as plt
import seaborn as sns

df, target_name = load_iris_data()

os.makedirs("plots", exist_ok=True)

plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df,
    x='sepal length',
    y='petal length',
    hue=target_name,
    style=target_name,
    s=90
)

plt.title('Iris Species: Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Iris Species')
plt.grid(True)
plt.savefig('example/e_getting_started/plots/sepal_length_v_petal_length.png', dpi=150)
plt.close()