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

Berikut adalah tahapan untuk menggunakan sistem machine learning melalui dashboard Streamlit:

1. **Akses Streamlit Dashboard**  
   Buka aplikasi melalui tautan berikut: [Student Status Prediction Streamlit](https://student-prediction-royanrosyad.streamlit.app/). Tunggu hingga dashboard tampil sepenuhnya di browser.

2. **Navigasi Menu**  
   Setelah dashboard terbuka, tersedia dua tab utama pada halaman utama:
   - ℹ️ **Tentang Dashboard**: Menyajikan informasi umum mengenai tujuan, manfaat, dan fitur yang digunakan dalam prediksi.
   - 🔮 **Prediksi Mahasiswa**: Menu utama untuk melakukan prediksi status mahasiswa berdasarkan data yang diinput.

3. **Melakukan Prediksi Data**  
   Pada tab **Prediksi Mahasiswa**, isikan seluruh data akademik dan data pribadi mahasiswa pada form yang tersedia. Data yang perlu diisi meliputi:
   - Informasi umum seperti urutan aplikasi, nilai kualifikasi sebelumnya, dan nilai penerimaan.
   - Data akademik semester 1 dan 2, seperti jumlah mata kuliah yang diambil, disetujui, SKS diakui, dan nilai rata-rata.
   - Data pribadi, termasuk jenis kelamin, status beasiswa, status pembayaran, status mahasiswa pindahan, dan status debitur.

   Setelah seluruh data terisi, tekan tombol **Prediksi Status Mahasiswa**. Sistem akan memproses data dan menampilkan hasil prediksi status mahasiswa (Graduate atau Dropout) beserta probabilitasnya. Jika prediksi menunjukkan risiko dropout, dashboard juga akan memberikan rekomendasi tindakan yang dapat diambil.

Dengan mengikuti langkah-langkah di atas, sistem machine learning pada dashboard Streamlit dapat dimanfaatkan untuk melakukan prediksi status mahasiswa secara mudah dan interaktif.

## Conclusion

Berdasarkan hasil analisis data yang telah dilakukan, sejumlah faktor utama yang memengaruhi **tingkat dropout mahasiswa** di Jaya Jaya Institut berhasil diidentifikasi. Faktor-faktor tersebut meliputi:

1. **Usia**: Mahasiswa pada rentang usia muda, khususnya 18–19 tahun, menunjukkan kecenderungan lebih tinggi untuk mengalami dropout. Hal ini dapat dikaitkan dengan tantangan adaptasi dari jenjang sekolah menengah ke perguruan tinggi.
2. **Prestasi Akademik**: Mahasiswa dengan capaian akademik rendah, terutama pada semester awal, memiliki risiko lebih besar untuk tidak menyelesaikan studi. Nilai akademik menjadi indikator penting dalam mendeteksi potensi masalah yang dapat berujung pada dropout.
3. **Gender**: Terdapat perbedaan tingkat dropout antara mahasiswa laki-laki dan perempuan, meskipun selisihnya tidak terlalu signifikan. Namun, kecenderungan dropout sedikit lebih tinggi pada kelompok mahasiswa perempuan.
4. **Status Beasiswa**: Mahasiswa penerima beasiswa cenderung memiliki tingkat dropout yang lebih rendah dibandingkan dengan yang tidak menerima beasiswa, menandakan bahwa dukungan finansial berperan penting dalam menjaga keberlanjutan studi.
5. **Kondisi Keuangan**: Mahasiswa yang memiliki status debitur atau tanggungan keuangan menunjukkan risiko dropout yang lebih tinggi, yang kemungkinan besar disebabkan oleh tekanan ekonomi selama masa studi.

Dengan implementasi sistem prediksi ini, Jaya Jaya Institut dapat merancang intervensi yang lebih tepat sasaran dan berbasis data untuk menekan angka dropout, meningkatkan tingkat kelulusan, serta memperkuat reputasi institusi secara menyeluruh.

### Rekomendasi Action Items

Agar upaya menurunkan angka dropout dan meningkatkan kualitas pendidikan di Jaya Jaya Institut berjalan lebih efektif, berikut lima rekomendasi utama yang dapat diterapkan:

1. **Penguatan Program Mentoring dan Bimbingan Akademik**  
   Penting untuk menyediakan program mentoring dan bimbingan akademik secara konsisten, terutama bagi mahasiswa yang teridentifikasi berisiko tinggi dropout berdasarkan hasil prediksi model machine learning. Pendampingan ini bisa dilakukan melalui sesi konsultasi rutin dengan dosen, konselor, atau mahasiswa senior, serta pelatihan keterampilan belajar yang membantu mahasiswa beradaptasi dengan lingkungan kampus dan tantangan akademik.

2. **Pengembangan Sistem Peringatan Dini dan Monitoring Berbasis Data**  
   Mengintegrasikan sistem peringatan dini ke dalam dashboard akan sangat membantu dalam mendeteksi mahasiswa yang mulai menunjukkan tanda-tanda risiko dropout, seperti penurunan nilai atau kehadiran. Dengan adanya notifikasi otomatis kepada dosen dan staf akademik, intervensi dapat dilakukan lebih cepat dan tepat sasaran, sehingga masalah dapat diatasi sebelum berkembang lebih jauh.

3. **Peningkatan Dukungan Finansial dan Program Beasiswa**  
   Memperluas akses terhadap beasiswa dan bantuan keuangan sangat penting, terutama bagi mahasiswa yang menghadapi kendala ekonomi atau memiliki status debitur. Dukungan finansial ini dapat berupa beasiswa tambahan, pinjaman pendidikan dengan cicilan ringan, atau peluang kerja paruh waktu di kampus, sehingga mahasiswa dapat lebih fokus pada studi mereka tanpa terbebani masalah ekonomi.

4. **Optimalisasi Penggunaan Dashboard Interaktif untuk Pengambilan Keputusan**  
   Dashboard analitik yang telah dikembangkan sebaiknya dimanfaatkan secara maksimal untuk memantau performa mahasiswa dan mengevaluasi efektivitas program intervensi. Memberikan pelatihan rutin kepada dosen dan staf dalam membaca serta menginterpretasi data akan memastikan setiap keputusan yang diambil benar-benar didasarkan pada bukti dan kebutuhan nyata di lapangan.

5. **Evaluasi dan Pengembangan Berkelanjutan Program Intervensi**  
   Melakukan evaluasi secara berkala terhadap program intervensi yang telah dijalankan sangat penting untuk memastikan efektivitasnya. Data dari dashboard dan hasil prediksi model dapat digunakan untuk menilai dampak setiap program, sehingga strategi yang diterapkan dapat terus disesuaikan dan ditingkatkan agar semakin efektif dalam menurunkan angka dropout dan meningkatkan retensi mahasiswa.

Dengan menerapkan rekomendasi-rekomendasi ini, Jaya Jaya Institut dapat menciptakan lingkungan akademik yang lebih suportif, menurunkan angka dropout, serta meningkatkan keberhasilan dan kepuasan mahasiswa secara menyeluruh.