import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Veri yükle
df = pd.read_csv('C:/Users/oguzhan/Downloads/datas/electric_vehicles.csv')

# Gerekli sütunları al, eksikleri çıkar
df_clean = df[['brand', 'battery_capacity_kWh', 'range_km']].dropna()

# Performans metriği: menzil / batarya kapasitesi
df_clean['range_per_kWh'] = df_clean['range_km'] / df_clean['battery_capacity_kWh']

# Marka bazında ortalama performans
brand_perf = df_clean.groupby('brand')['range_per_kWh'].mean().reset_index()

# En yüksek performanslı markayı bul
best_idx = brand_perf['range_per_kWh'].idxmax()
best_brand = brand_perf.loc[best_idx, 'brand']
best_value = brand_perf.loc[best_idx, 'range_per_kWh']

# Grafik için renk paleti: tüm barlar mavi, en iyi marka turuncu
colors = ['orange' if i == best_idx else 'dodgerblue' for i in range(len(brand_perf))]

# Barplot çizimi
plt.figure(figsize=(14,8))
sns.barplot(x='range_per_kWh', y='brand', data=brand_perf.sort_values('range_per_kWh', ascending=False),
            palette=colors)

plt.title('Marka Bazında Ortalama Menzil / Batarya Kapasitesi (km/kWh)', fontsize=16)
plt.xlabel('Ortalama km/kWh')
plt.ylabel('Marka')

# En iyi markayı grafik üzerine not olarak ekle
plt.text(best_value + 0.1, best_idx, f"En iyi: {best_brand} ({best_value:.2f} km/kWh)",
         color='black', weight='bold', fontsize=12, va='center')

plt.grid(axis='x')
plt.tight_layout()
plt.show()
