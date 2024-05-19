x_old = 0 # Başlangıç değeri; değeri önemli değil çünkü abs(x_new - x_old) > precision olduğu sürece döngü devam eder
x_new = 6 # Algoritma x=6'dan başlar, bu bizim başlangıç noktamız
gamma = 0.01 # Adım boyutu (öğrenme oranı), gradyan inişinde her adımda ne kadar hareket edileceğini belirler
precision = 0.00001 # İstenilen hassasiyet (döngünün durma kriteri), x_new ve x_old arasındaki fark bu değerden küçük olduğunda döngü durur

def df(x):
    y = 4 * x**3 - 9 * x**2 # Fonksiyonun türevini hesaplar
    return y

while abs(x_new - x_old) > precision:
    x_old = x_new # x_old'yi önceki x_new değeri olarak güncelleriz
    x_new += -gamma * df(x_old) # Yeni x değerini hesaplarız, negatif türev yönünde adım atarız

print("The local minimum occurs at ", +x_new) # Bulunan yerel minimumun x değerini yazdırır
