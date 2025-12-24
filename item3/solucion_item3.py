# Solución ítem 3
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(20, 12))
fig.suptitle('Cancer', fontsize=16, fontweight='bold')

# ===============================
# Histograma: edad
# ===============================
axes[0, 0].hist(df['age'], bins=6, color='skyblue', edgecolor='black')
axes[0, 0].set_title('Distribucion de la edad')
axes[0, 0].set_xlabel('Edad')
axes[0, 0].set_ylabel('Frecuencia')
axes[0, 0].grid(alpha=0.3)

# ===============================
# Pie chart: genero
# ===============================
gender_counts = df['gender'].value_counts()

axes[0, 1].pie(
    gender_counts,
    labels=gender_counts.index,
    autopct='%1.1f%%',
    startangle=90
)
axes[0, 1].set_title('Distribucion del genero')

# ===============================
# Barras: pais
# ===============================
country_counts = df['country'].value_counts()

axes[1, 0].bar(
    country_counts.index,
    country_counts.values,
    color='lightcoral'
)
axes[1, 0].set_title('Pacientes por pais')
axes[1, 0].set_ylabel('Numero de pacientes')
axes[1, 0].tick_params(axis='x', rotation=90)

# ===============================
# Barras: etapa del cancer
# ===============================
stage_counts = df['cancer_stage'].value_counts()

axes[1, 1].bar(
    stage_counts.index,
    stage_counts.values,
    color='lightgreen'
)
axes[1, 1].set_title('Distribucion de la etapa del cancer')
axes[1, 1].set_ylabel('Numero de observaciones')

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
