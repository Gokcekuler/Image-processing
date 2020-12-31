import numpy as np
 
class Perceptron(object):
    """Implements a perceptron network"""
    def __init__(self, input_size, lr=1, epochs=10):
        self.W = np.zeros(input_size+1)
        self.epochs= epochs
        self.lr= lr
    def activation_fn(self, x):
        return 1 if x >= 0 else 0
    def predict(self, x):
        x = np.insert(x, 0, 1)
        z = self.W.T.dot(x)
        a = self.activation_fn(z)
        return a

    def fit(self, X, d):
        for _ in range(self.epochs):
           for i in range(d.shape[0]):
                y = self.predict(X[i])
                e = d[i] - y
                self.W = self.W + self.lr * e * np.insert(X[i], 0, 1  )

#mp= Perceptron(5)
#x=np.asarray([-10,-2,-30,4,-50])
#mp.predict(x)

X = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])
d = np.array([0, 0, 0, 1])
 
perceptron = Perceptron(input_size=2)
perceptron.fit(X, d)
print(perceptron.W)


    #a) init = constructor dır. lr öğrenme hızı epochs ise verilerin kaç kere çalıştırıldığıdır.
    # activation_fn= giriş 0 dan büyük eşitse 1 küçükse 0 döndürüyor. Sınıflandırma için kullanılıyor.
    # predict=girdilerden çıktı elde ediyoruz. İç çarpımı hesaplayıp aktivasyon fonksiyonunu kullanıyoruz.
    # fit = epochs sayısı kadar döngü kurup değeri güncelliyor

    # b) xor için yeteneği yoktur

    # c) imza için yükseklik ve  genişlik değerlerini m ve n alırsak ve bunları 100 olarak düşünürsek 40 imza için (100*100*3,40) lık bir matrisimiz olur. Yani d değeri için 40 farklı değerimiz olacaktır. 

    # d) çıkış değeri ve hesaplanan çıkış değeri arasındaki fark giriş ağırlık değerlerini güncellemede kullanılabilir. 






