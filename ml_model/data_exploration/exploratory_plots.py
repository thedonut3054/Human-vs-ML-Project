import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from ml_model.data.fetch_data import get_data
 
data = get_data()
print(data.info())