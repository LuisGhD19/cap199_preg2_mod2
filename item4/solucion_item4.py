# Solución ítem 4
import matplotlib.pyplot as plt

# Crear figura con 3 subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle('Boxplots de variables numéricas', fontsize=16, fontweight='bold')

# ===============================
# Boxplot: age
# ===============================
axes[0].boxplot(df['age'], vert=True)
axes[0].set_title('Age')
axes[0].set_ylabel('Valor')
axes[0].grid(alpha=0.3)

# ===============================
# Boxplot: bmi
# ===============================
axes[1].boxplot(df['bmi'], vert=True)
axes[1].set_title('BMI')
axes[1].grid(alpha=0.3)

# ===============================
# Boxplot: cholesterol_level
# ===============================
axes[2].boxplot(df['cholesterol_level'], vert=True)
axes[2].set_title('Cholesterol Level')
axes[2].grid(alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.92])
plt.show()
