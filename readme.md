## CAT N DOG IMAGE CLASSIFIER
Pengenalan Gambar Kucing dan Anjing menggunakan Convolution Neural Network (CNN) Classifier

### Step 1: Dataset
Dataset dapat diunduh pada link berikut https://www.kaggle.com/c/dogs-vs-cats/data
Ekstrak dataset dan buat struktur direktorinya seperti berikut
```
 _model
|_screenshoot
|_test_data
|_test_set
  |_cat
  |_dog
|_training_set
  |_cat
  |_dog
|_testing.py
|_training.py
```
### Step 2: Menyiapkan program
Program ini membutuhkan beberapa module sebagai berikut
```
1. Python 3.6
2. Open CV
3. Tensorflow
4. Keras
5. Matplotlib
```
### Step 3: Training data
Untuk melakukan training data gunakan file ```training.py```. Training tersebut akan menghasilkan file ```model.json``` dan ```model.h5``` yang nantinya akan digunakan sebagai model pada klasifikasi gambar.

### Step 4: Testing data
Untuk melakukan testing data letakkan gambar yang akan di test di folder ```test_data``` kemudian jalankan file ```testing.py```.
