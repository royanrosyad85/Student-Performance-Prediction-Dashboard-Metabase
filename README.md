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

Berikut adalah informasi dari chart yang tersedia di **Student Insight Dashboard**, disusun dalam format poin seperti permintaanmu:

---

**Dashboard bisnis yang telah dibuat di Metabase menyajikan visualisasi data yang mencakup:**

- **Jumlah Total Siswa:** 4,424  
- **Total Course:** 17
- **Rata-rata Usia Siswa:** 23.27 tahun  
- **Tingkat Dropout:** 32.12%  
- **Tingkat Keberhasilan Ujian Rata-rata:** 55.09%  

### Visualisasi Chart:

1. **Perbandingan Status Siswa Berdasarkan Course**  
   Menampilkan jumlah siswa yang **Graduate (lulus)**, **Dropout (berhenti/tidak lulus)**, dan **Enrolled (masih aktif kuliah)** untuk setiap jurusan/course.  

2. **Status Percentage of Students by Status**  
   Pie chart yang menunjukkan persentase total siswa berdasarkan status:
   - **Enrolled**: 18% → Masih aktif
   - **Dropout**: 32% → Berhenti/tidak lulus
   - **Graduate**: 50% → Sudah lulus

3. **Scholarship vs Non-scholarship Students**  
   Membandingkan jumlah siswa yang mendapat beasiswa (**Yes**) dan yang tidak (**No**) pada tiap status:

4. **Persentase Gender Berdasarkan Status**  
   Menunjukkan perbandingan jumlah **laki-laki** dan **perempuan** untuk masing-masing status:
   - Mayoritas siswa adalah **perempuan** di semua kategori (lulus, aktif, maupun drop out)

5. **Perbandingan Total Student Berdasarkan Umur**  
   Diagram batang yang memperlihatkan distribusi jumlah siswa berdasarkan usia (17–30 tahun):
   - Usia paling dominan: **19–22 tahun**
   - Jumlah siswa semakin sedikit seiring bertambahnya usia di atas **25 tahun**

🔗 **Link untuk mengakses dashboard:**  
[Klik di sini untuk mengakses dashboard di Metabase](https://jmjttiml.ap-southeast-1.clawcloudrun.com/public/dashboard/62ad6b47-d2a8-40d5-a313-1ab9f586ec53?status=)  


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
