# Regression Analysis - CatBoost Regresyon

Bu proje, CatBoost regresyon algoritması kullanarak verilen veri setinde hedef sütunun tahmin edilmesini amaçlamaktadır. Modelin hiperparametreleri Grid Search algoritmasıyla optimize edilmiş ve sonuçlar 10 kat çapraz doğrulama yöntemi ile değerlendirilmiştir.

---

## İçerik

- Python kodu ile model eğitimi ve tahminler  
- Grid Search sonucu bulunan en iyi hiperparametreler tablosu  
- Gerçek ve tahmin edilen değerlerin karşılaştırıldığı Excel dosyası (fark sütunu dahil)  
- Hesaplanan performans metrikleri: **R², MAE, RMSE**  
- Korelasyon matrisi (Heatmap) görseli  
- Scatterplot Matrix (Dağılım Grafikleri) görseli  
- Seaborn ile oluşturulan çift grafikler (Pairs Plot)  
- Özellik önem derecesi grafiği  

---

## Kullanılan Teknolojiler ve Kütüphaneler

- Python 3.x  
- CatBoost  
- scikit-learn  
- pandas  
- numpy  
- matplotlib  
- seaborn  
- openpyxl (Excel dosyası işlemleri için)  

---

## Kurulum ve Çalıştırma

1. Projeyi klonlayın veya zip dosyasını açın.

2. Sanal ortam oluşturmanızı öneririm:

   ```bash
   python -m venv venv
   Linux / Mac:  
   source venv/bin/activate
   Windows:  
   venv\Scripts\activate
   
 3.Gerekli kütüphaneleri yükleyin:

   ```bash
   pip install -r requirements.txt  
  ```
4. Python dosyasını çalıştırarak modeli eğitin ve sonuçları inceleyin.

 ##  Notlar

Veri seti ve rapor dosyaları proje klasöründe mevcuttur.

Model performansını artırmak için farklı hiperparametreler denenebilir.

Görseller proje çıktıları arasında yer almaktadır.


