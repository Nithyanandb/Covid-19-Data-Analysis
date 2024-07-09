import pandas as pd
import seaborn as sns
import matplotlib as plt
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv(r"C:\Users\nithy\Documents\GitHub\Covid-19-Data-Analysis\Dataset.csv")
def print_box(text):
    length = len(text)
    print("+" + "-" * (length - 7) + "+")
    print("| " + text + " |")
    print("+" + "-" * (length - 7) + "+")
print_box("\033[34mDataset\033[0m")
print(data)


print_box("\033[34mStatistics for Date, State, Regions, Confirmed Cases, Deaths, and Recoveries\033[0m")
print(data.count())


affected = data.groupby('Region')['Confirmed'].sum().sort_values(ascending=False).head(10)
print_box("\033[34mConfirmed\033[0m")
print(affected)



died = data.groupby('Region')['Deaths'].sum().sort_values(ascending=False).head(10)
print_box("\033[34mDIED\033[0m")
print(died)

recovery = data.groupby('Region')['Recovered'].sum().sort_values(ascending=False).head(10)
print_box("\033[34mRecovered\033[0m")
print(recovery)

heatmap_data = pd.DataFrame({
    'Affected': affected,
    'Died': died,
    'Recovered': recovery
}).fillna(0)

x = np.arange(heatmap_data.shape[1])
wave = np.sin(x / 2) * 100
heatmap_data = heatmap_data + wave


plt.figure(figsize=(14, 8))
sns.heatmap(heatmap_data, annot=True, cmap='coolwarm', fmt='.0f', cbar_kws={'label': 'Count'})
plt.title('Top 10 Regions: COVID-19 Confirmed, Deaths, and Recovered by Region', fontsize=18, fontweight='bold', color='darkblue')
plt.xlabel('Region', fontsize=12, fontweight='bold')
plt.ylabel('Category', fontsize=12, fontweight='bold')

plt.xticks(rotation=45, fontsize=12, fontweight='bold')

plt.yticks(rotation=0, fontsize=12, fontweight='bold')


cbar = plt.gca().collections[0].colorbar
cbar.ax.tick_params(labelsize=12)

plt.show()

print(data[data.Confirmed < 15].head(10))


print_box("\033[34mMaximum No of Confirmed Case\033[0m")
max_confirmed = data.groupby('Region')['Confirmed'].sum().sort_values(ascending=False).head(10)
print(max_confirmed)
print_box("\033[34mMaximum No of Deaths\033[0m")
max_deaths = data.groupby('Region').Deaths.sum().sort_values(ascending=False).head(20)
print(max_deaths)

print_box("\033[34mMaximum No of Recvered\033[0m")
max_Rec= data.groupby('Region').Recovered.sum().sort_values(ascending=False).head(20)
print(max_Rec)


print_box("Confirmed, Recovered and Dealths Cases were Reported from India till 29 April 2020")
repoindia  = data[data.Region =='India']
print(repoindia)

print_box("Confirmed, Recovered and Dealths Cases were Reported in US ")
repoUs  = data[data.Region =='US']
print(repoUs)