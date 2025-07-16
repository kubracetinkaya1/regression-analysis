import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from catboost import CatBoostRegressor
from sklearn.model_selection import GridSearchCV, cross_val_predict, KFold
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import warnings
warnings.filterwarnings("ignore")

# 1. Excel dosyasını oku (2. satır başlık olacak şekilde)
df = pd.read_excel("File.xlsx", header=1)

# 2. İlk (boş) sütunu kaldır
df = df.iloc[:, 1:]

# 3. X ve y ayır
X = df.drop("K", axis=1)
y = df["K"]

# 4. CatBoost modeli ve GridSearch parametreleri
model = CatBoostRegressor(verbose=0)
param_grid = {
    "depth": [4, 6, 8],
    "learning_rate": [0.01, 0.05, 0.1],
    "iterations": [100, 200]
}

cv = KFold(n_splits=10, shuffle=True, random_state=42)
grid = GridSearchCV(model, param_grid, cv=cv, scoring="r2", n_jobs=-1)
grid.fit(X, y)
best_model = grid.best_estimator_

# 5. 10-kat çapraz doğrulama tahminleri
y_pred = cross_val_predict(best_model, X, y, cv=cv)
 



# 6. Metrikleri hesapla
r2 = r2_score(y, y_pred)
mae = mean_absolute_error(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))

# 7. Sonuçları DataFrame olarak oluştur
results_df = pd.DataFrame({
    "Gerçek K Değeri": y,
    "Tahmin Edilen K": y_pred,
    "Fark": y - y_pred
})
results_df.to_excel("k_degerleri_tahmin.xlsx", index=False)

# 8. En iyi parametreleri ve metrikleri yazdır
print("🔧 En iyi hiperparametreler:", grid.best_params_)
print(f"📊 R²: {r2:.4f}, MAE: {mae:.4f}, RMSE: {rmse:.4f}")

# 9. Korelasyon Isı Haritası
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Korelasyon Matrisi (Heatmap)")
plt.tight_layout()
plt.savefig("heatmap.jpg")
plt.close()

# 10. Scatterplot Matrix
sns.pairplot(df)
plt.savefig("scatterplot_matrix.jpg")
plt.close()

# 11. Pairplot (reg çizgili)
sns.pairplot(df, kind="scatter")
plt.savefig("pairplot_reg.jpg")
plt.close()

# 12. Özellik Önem Grafiği
importances = best_model.get_feature_importance()
feature_names = X.columns

plt.figure(figsize=(8,6))
sns.barplot(x=importances, y=feature_names)
plt.title("Özellik Önem Grafiği (Feature Importance)")
plt.xlabel("Önem Skoru")
plt.ylabel("Özellikler")
plt.tight_layout()
plt.savefig("feature_importance.jpg")
plt.close()
