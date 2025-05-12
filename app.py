import streamlit as st
import pandas as pd
from joblib import load
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

st.set_page_config(
    page_title="Student Status Prediction",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Memuat model dan scaler
try:
    model = load('gradient_boosting.pkl')
    standard_scaler = load('standard_scaler.pkl')
except Exception as e:
    st.error(f"Error loading model or scaler: {e}")
    st.stop()

st.markdown("<h1 style='text-align: center;'>🎓 Dashboard Prediksi Status Mahasiswa</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Jaya Jaya Maju Institut</p>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["ℹ️ Tentang Dashboard", "🔮 Prediksi Mahasiswa"])

# Content for About Dashboard Tab
with tab1:
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.image("annie-spratt-MChSQHxGZrQ-unsplash.jpg", width=400)
    
    with col2:
        st.subheader("Apa Sih Dashboard Ini?")
        st.write("Dashboard ini dibuat untuk memprediksi status mahasiswa di Jaya Jaya Maju Institut. Hasil prediksinya ada dua: Lulus (Graduate) atau Putus Sekolah (Dropout). Cukup isi beberapa data, dan sistem akan bantu kasih prediksi statusnya.")
        
        st.subheader("🎯 Kenapa Penting?")
        st.write("Tujuan utama dari dashboard ini adalah untuk mendeteksi mahasiswa yang berisiko putus kuliah sejak dini, supaya bisa langsung dikasih perhatian khusus atau pendampingan. Dengan bantuan model prediktif, dashboard ini bantu kampus ambil keputusan lebih cepat dan tepat buat ningkatin angka kelulusan.")
        
        st.write("✨ Diharapkan, kedepannya dapat menjadi dukungan strategis dalam meningkatkan tingkat retensi dan kelulusan mahasiswa di lingkungan kampus.")
    
    
    # Explanation of features used
    with st.expander("📋 Fitur-Fitur Yang Digunakan Dalam Prediksi"):
        st.markdown("""
        **Akademik:**
        * Nilai kualifikasi sebelumnya
        * Nilai penerimaan
        * Jumlah mata kuliah yang diambil dan disetujui
        * Nilai rata-rata semester
        
        **Pribadi:**
        * Jenis kelamin
        * Status beasiswa
        * Status pembayaran kuliah
        * Status mahasiswa pindahan (displaced)
        * Status debitur
        """)
    
    
    with st.expander("🧠 Informasi Teknis Model"):
        st.markdown("""
        Dashboard ini menggunakan algoritma **Gradient Boosting Classifier** yang dilatih dengan data historis mahasiswa. Model tersebut menunjukkan performa yang tinggi dengan:
        
        * **Akurasi:** ~90%  
        * **Recall untuk kelas Dropout:** ~84%  
        * **Precision untuk kelas Dropout:** ~90%
        
        Model ini memungkinkan deteksi dini mahasiswa yang berpotensi dropout dengan tingkat akurasi yang baik.
        """)

# Content for Student Prediction Tab
with tab2:
    def user_input_features():
        st.header("📚 Data Akademik")
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Informasi Umum")
            Application_order = st.slider('Urutan Aplikasi', 1, 10, 1, help="Urutan aplikasi mahasiswa mendaftar")
            Previous_qualification_grade = st.slider('Nilai Kualifikasi Sebelumnya', 0.0, 190.0, 90.0, help="Nilai dari kualifikasi pendidikan sebelumnya")
            Admission_grade = st.slider('Nilai Penerimaan', 0.0, 190.0, 90.0, help="Nilai yang diperoleh saat penerimaan masuk perguruan tinggi")
        
        with col2:
            st.subheader("Kehadiran & Status")
            Daytime_evening_attendance = st.radio('Jadwal Kuliah', ('Daytime', 'Evening'), horizontal=True, help="Apakah mahasiswa mengikuti kuliah di siang atau malam hari")
            Tuition_fees_up_to_date = st.radio('Pembayaran Biaya Kuliah Tepat Waktu', ('Yes', 'No'), horizontal=True, help="Apakah pembayaran biaya kuliah sudah up-to-date")
        
        # Semester 1 information
        st.markdown("---")
        st.subheader("Data Akademik Semester 1")
        col_sem1_1, col_sem1_2 = st.columns(2)
        
        with col_sem1_1:
            Curricular_units_1st_sem_enrolled = st.slider('Mata Kuliah Diambil (Sem 1)', 0, 30, 0, help="Jumlah mata kuliah yang diambil pada semester 1")
            Curricular_units_1st_sem_approved = st.slider('Mata Kuliah Disetujui (Sem 1)', 0, 30, 0, help="Jumlah mata kuliah yang disetujui pada semester 1")
        
        with col_sem1_2:
            Curricular_units_1st_sem_credited = st.slider('SKS Diakui (Sem 1)', 0, 30, 0, help="Jumlah SKS yang diakui pada semester 1")
            Curricular_units_1st_sem_grade = st.slider('Nilai Rata-rata (Sem 1)', 0.0, 30.0, 0.0, help="Nilai rata-rata semester 1")
        
        # Semester 2 information
        st.markdown("---")
        st.subheader("Data Akademik Semester 2")
        col_sem2_1, col_sem2_2 = st.columns(2)
        
        with col_sem2_1:
            Curricular_units_2nd_sem_enrolled = st.slider('Mata Kuliah Diambil (Sem 2)', 0, 20, 0, help="Jumlah mata kuliah yang diambil pada semester 2")
            Curricular_units_2nd_sem_approved = st.slider('Mata Kuliah Disetujui (Sem 2)', 0, 20, 0, help="Jumlah mata kuliah yang disetujui pada semester 2")
        
        with col_sem2_2:
            Curricular_units_2nd_sem_credited = st.slider('SKS Diakui (Sem 2)', 0, 20, 0, help="Jumlah SKS yang diakui pada semester 2")
            Curricular_units_2nd_sem_grade = st.slider('Nilai Rata-rata (Sem 2)', 0.0, 30.0, 0.0, help="Nilai rata-rata semester 2")
        
        # Personal information section
        st.markdown("---")
        st.header("👤 Data Pribadi Mahasiswa")
        
        col_p1, col_p2 = st.columns(2)
        
        with col_p1:
            Gender = st.radio('Jenis Kelamin', ('Male', 'Female'), horizontal=True)
            Scholarship_holder = st.radio('Penerima Beasiswa', ('Yes', 'No'), horizontal=True)
        
        with col_p2:
            Displaced = st.radio('Mahasiswa Pindahan/Displaced', ('Yes', 'No'), horizontal=True, help="Apakah mahasiswa berasal dari daerah lain")
            Debtor = st.radio('Status Debitur', ('Yes', 'No'), horizontal=True, help="Apakah mahasiswa memiliki hutang")

        data = {
            'Application_order': Application_order,
            'Daytime_evening_attendance': 1 if Daytime_evening_attendance == 'Daytime' else 0,
            'Previous_qualification_grade': Previous_qualification_grade,
            'Admission_grade': Admission_grade,
            'Displaced': 1 if Displaced == 'Yes' else 0,
            'Debtor': 1 if Debtor == 'Yes' else 0,
            'Tuition_fees_up_to_date': 1 if Tuition_fees_up_to_date == 'Yes' else 0,
            'Gender': 1 if Gender == 'Male' else 0,
            'Scholarship_holder': 1 if Scholarship_holder == 'Yes' else 0,
            'Curricular_units_1st_sem_credited': Curricular_units_1st_sem_credited,
            'Curricular_units_1st_sem_enrolled': Curricular_units_1st_sem_enrolled,
            'Curricular_units_1st_sem_approved': Curricular_units_1st_sem_approved,
            'Curricular_units_1st_sem_grade': Curricular_units_1st_sem_grade,
            'Curricular_units_2nd_sem_credited': Curricular_units_2nd_sem_credited,
            'Curricular_units_2nd_sem_enrolled': Curricular_units_2nd_sem_enrolled,
            'Curricular_units_2nd_sem_approved': Curricular_units_2nd_sem_approved,
            'Curricular_units_2nd_sem_grade': Curricular_units_2nd_sem_grade,
        }
        return pd.DataFrame(data, index=[0])

    # Collect user input
    df_input = user_input_features()

    # Generate prediction
    st.header("🔍 Hasil Prediksi")
    
    if st.button('Prediksi Status Mahasiswa', use_container_width=True):
        try:
            numerical_features = ['Application_order', 'Previous_qualification_grade', 'Admission_grade',
                                'Curricular_units_1st_sem_enrolled', 'Curricular_units_2nd_sem_enrolled',
                                'Curricular_units_1st_sem_credited', 'Curricular_units_2nd_sem_credited',
                                'Curricular_units_1st_sem_approved', 'Curricular_units_2nd_sem_approved',
                                'Curricular_units_1st_sem_grade', 'Curricular_units_2nd_sem_grade']

            # Setup preprocessing pipeline
            preprocessor = ColumnTransformer(
                transformers=[('scaler', standard_scaler, numerical_features)],
                remainder='passthrough'
            )

            pipeline = Pipeline([
                ('preprocessor', preprocessor),
                ('classifier', model)
            ])

            # Make prediction
            pipeline.named_steps['preprocessor'].fit(df_input)
            y_pred_test = pipeline.predict(df_input)

            # Display results
            status = 'Dropout' if y_pred_test[0] == 1 else 'Graduate'
            emoji = '⚠️' if status == 'Dropout' else '🎉'
            
            if hasattr(model, 'predict_proba'):
                y_pred_proba = pipeline.predict_proba(df_input)
                proba = round(y_pred_proba[0][y_pred_test[0]] * 100, 1)
                
                if status == 'Graduate':
                    st.success(f"{emoji} Status Prediksi: **{status}**")
                else:
                    st.error(f"{emoji} Status Prediksi: **{status}**")
                st.info(f"Probabilitas: **{proba}%**")
                st.caption("Hasil prediksi berdasarkan data yang dimasukkan")
                
                # Additional recommendations based on prediction
                if status == 'Dropout':
                    with st.expander("💡 Rekomendasi Tindakan"):
                        st.markdown("""
                        * Lakukan konsultasi akademik dengan mahasiswa tersebut
                        * Periksa faktor penghambat performa akademik
                        * Pertimbangkan program pendampingan khusus
                        * Evaluasi kebutuhan finansial (beasiswa/bantuan biaya)
                        """)
            else:
                st.write(f"{emoji} **{status}**")
                st.warning("Probabilitas tidak tersedia untuk model ini")
            
            with st.expander("📊 Ringkasan Data Input"):
                st.dataframe(df_input)
                
        except Exception as e:
            st.error(f"Terjadi kesalahan saat melakukan prediksi: {e}")

st.caption("© 2025 by Royanrosyad")
