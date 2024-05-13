import numpy as np

#ileri beslemede transfer fonksiyonu olarak 
def sigmoid(net):
    return 1/(1+np.exp(-net))

#geri yayılımda 
#f türev nete karşılık geliyor formülde
#ağırlıkların ilk değeri rastgele atılır
#başlangıç değerleri önemli

#transfer öğrenme: daha önce öğrenmiş bir ağdan bilgisinin transfer etme
#buradakş bilgi ağırlıklar aslında öğrenmeyi ağırlıklar temsil ediyor.

#aktivasyon fonksiyonu
def sigmoid_derivate(net):
    return sigmoid(net)*(1-sigmoid(net))

epochs=1000
learning_rate=1

inputs=np.array([[0,0],[0,1],[1,0],[1,1]])
outputs=np.array([0,0,0,1])

weights=np.array([0.1,0.3])
bias=-0.9

#bir epoch döngüsü veri setinin aç kere tekrarlancağı bilgisi
#veri setinin kendi içerisindeki gözlemlerin döngüsü 
#input giriş bilgisi,label:gercek_cikis gercek değer
#bir nörondaki ilk bilgi toplam bilgisini elde etmek/net bilgisi
#dot dediğimiz toplam semblolünün karşılığı 
#vektörel çarpım/skalar çarpım? ikisi arasındaki fark ne? burada matris çarpımı yapıyoruz .dot ile
#hatanın karesinni alırsak mutlak hataya göre farkı ne olur

for epoch in range(epochs):
    toplam_hata=0
    for input, gercek_cikis in zip(inputs,outputs):

        #ileri besleme
        net=np.dot(input,weights)+bias
        ag_cikis=sigmoid(net)

        #hata hesabı 
        hata=gercek_cikis-ag_cikis #anlık hata
        toplam_hata+=hata**2

        #geri yayılım
        delta=learning_rate*hata*sigmoid_derivate(net)
        delta_w=delta*input

        #weights+=delta_W
        bias+=delta

print(f'{epoch}-Epoch: {toplam_hata}')

#model çıktısı
print("Testing trained model an AND inputs:")
for input in inputs:
    final_output=sigmoid(np.dot(input,weights)+bias)
    print(f"Input: {input} Output: {final_output}")

    
