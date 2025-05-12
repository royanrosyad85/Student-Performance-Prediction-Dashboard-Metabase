# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut merupakan sebuah perguruan tinggi yang telah berdiri sejak tahun 2000 dan telah meluluskan banyak mahasiswa berprestasi. Namun, institusi ini menghadapi tantangan serius berupa tingginya tingkat mahasiswa yang tidak menyelesaikan studi (dropout). Masalah ini berdampak pada citra institusi serta kualitas pendidikan yang diberikan. Untuk mengatasi hal tersebut, Jaya Jaya Institut berupaya mendeteksi mahasiswa yang berpotensi dropout sejak dini, sehingga dapat diberikan bantuan atau intervensi yang lebih efektif dan tepat sasaran.

Dengan semakin ketatnya persaingan di dunia pendidikan tinggi dan kebutuhan mahasiswa yang semakin beragam, Jaya Jaya Institut perlu memanfaatkan teknologi berbasis data untuk mengatasi permasalahan ini. Melalui penerapan analitik data dan machine learning, diharapkan institusi dapat mengenali mahasiswa berisiko dropout lebih awal dan memberikan dukungan yang diperlukan agar mereka dapat menyelesaikan pendidikan dengan baik.

### Permasalahan Bisnis

1. **Tingkat Dropout yang Tinggi**  
   Jaya Jaya Institut mengalami permasalahan dengan banyaknya mahasiswa yang tidak menyelesaikan studi, sehingga mempengaruhi reputasi dan persentase kelulusan.

2. **Sulitnya Deteksi Dini Mahasiswa Berisiko**  
   Institusi mengalami kesulitan dalam mengidentifikasi mahasiswa yang berpotensi dropout secara cepat, sehingga intervensi sering terlambat dilakukan.

3. **Belum Tersedianya Sistem Dukungan Berbasis Data**  
   Tidak terdapat sistem yang memanfaatkan data untuk memberikan intervensi atau dukungan secara efisien kepada mahasiswa yang membutuhkan.

4. **Pemanfaatan Data yang Kurang Optimal**  
   Data yang tersedia belum digunakan secara maksimal untuk memprediksi dan mencegah risiko dropout, sehingga pengambilan keputusan dan kebijakan belum sepenuhnya berbasis data.

### Cakupan Proyek

- **Dashboard Analitik**: Mengembangkan dashboard interaktif untuk menampilkan performa mahasiswa dan mengidentifikasi pola-pola yang berkaitan dengan risiko dropout. Dashboard ini menyajikan informasi statistik seperti tingkat kelulusan, kehadiran, dan nilai akademik mahasiswa.

- **Pengembangan Model Machine Learning**: Membuat model prediksi status mahasiswa (Dropout atau Graduate) menggunakan algoritma Gradient Boosting Classifier, sehingga pihak manajemen dapat mengambil keputusan intervensi yang lebih tepat.

- **Pembuatan Aplikasi Streamlit**: Merancang aplikasi berbasis Streamlit yang memungkinkan dosen atau manajemen memasukkan data mahasiswa secara langsung dan memperoleh prediksi status serta insight performa mahasiswa. Aplikasi ini memudahkan akses terhadap hasil analisis dan prediksi yang telah dikembangkan.

- **Rekomendasi Intervensi dan Kebijakan**: Memberikan saran tindakan dan kebijakan berdasarkan hasil analisis dan prediksi model, seperti peningkatan program pendampingan atau mentoring, serta pemanfaatan data untuk mendukung pengambilan keputusan yang lebih efektif dalam meningkatkan tingkat kelulusan dan kepuasan mahasiswa.

### Persiapan

**Sumber Data**  
Dataset yang digunakan dalam proyek ini tersedia di [tautan berikut](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv).

#### Setup Environment  
Berikut langkah-langkah untuk menyiapkan environment serta menjalankan dashboard Streamlit:

##### 1. Membuat Virtual Environment dengan Conda
Mulailah dengan membuat environment baru menggunakan Conda:

```bash
conda create --name streamlit-venv python=3.10
```

Aktifkan environment yang telah dibuat:

```bash
conda activate streamlit-venv
```

##### 2. Instalasi Dependencies dari `requirements.txt`
Pastikan Anda memiliki file `requirements.txt` yang berisi seluruh library yang diperlukan.  
Untuk menginstal semua dependensi, jalankan perintah berikut:

```bash
pip install -r requirements.txt
```

##### 3. Menjalankan Streamlit Dashboard
Setelah semua dependensi terpasang, jalankan aplikasi Streamlit dengan perintah:

```bash
streamlit run app.py
```

Setelah perintah dijalankan, Streamlit akan menampilkan URL (biasanya `http://localhost:8501`) yang dapat diakses melalui browser untuk melihat dashboard.

## Business Dashboard
Jelaskan tentang business dashboard yang telah dibuat. Jika ada, sertakan juga link untuk mengakses dashboard tersebut.

## Menjalankan Sistem Machine Learning
Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

```

```

## Conclusion
Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- action item 1
- action item 2
