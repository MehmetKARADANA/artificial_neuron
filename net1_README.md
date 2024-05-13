Matematiksel olarak bir yapay sinir ağını (YSA) eğitirken kullanılan hesaplamalar, özellikle bir AND mantık kapısı için, oldukça basit bir yapıya sahiptir. Bu işlemi adım adım matematiksel olarak açıklayacağım. Aşağıdaki örnek, tek bir nöron kullanarak AND işlemi gerçekleştirmek için gereken adımları içerir:

1.Sigmoid Aktivasyon Fonksiyonu ve Türevi:
𝜎(𝑥)=1/(1+𝑒−𝑥)
𝜎′(𝑥)=𝜎(𝑥)⋅(1−𝜎(𝑥))
2.Başlangıç Değerleri:
Ağırlıklar: 𝑤1=−0.8,𝑤2=0.5
Bias: 𝑏=−0.2
3.Eğitim Verileri ve Beklenen Çıktılar:
(𝑥1,𝑥2)=(1,0),𝑦=0
(𝑥1,𝑥2)=(0,1),𝑦=0
(𝑥1,𝑥2)=(0,0),𝑦=0
(𝑥1,𝑥2)=(1,1),𝑦=1
4.Eğitim Süreci (Bir iterasyon için):
Her girdi için:
İleri Yayılım:
𝑧=𝑤1𝑥1+𝑤2𝑥2+𝑏
𝑦^=𝜎(𝑧)
Hata ve Maliyet Fonksiyonu:
error=𝑦−𝑦^
Geri Yayılım ve Ağırlık Güncellemesi:
Δ𝑤=𝛼⋅error⋅𝜎′(𝑧)⋅𝑥
𝑤=𝑤+Δ𝑤
Δ𝑏=𝛼⋅error⋅𝜎′(𝑧)
𝑏=𝑏+Δ𝑏
Örneğin, ilk veri seti için hesaplamaları yapalım (𝑥1=1,𝑥2=0,𝑦=0):
İleri Yayılım:
𝑧=(−0.8⋅1)+(0.5⋅0)−0.2=−1
𝑦^=11+𝑒−(−1)≈0.2689
Hata:
error=0−0.2689=−0.2689
Geri Yayılım ve Ağırlık Güncellemesi:
𝜎′(𝑧)=0.2689⋅(1−0.2689)≈0.1966
Δ𝑤1=1⋅(−0.2689)⋅0.1966≈−0.0529
𝑤1=−0.8−0.0529=−0.8529
Δ𝑏=(−0.2689)⋅0.1966≈−0.0529
𝑏=−0.2−0.0529=−0.2529
