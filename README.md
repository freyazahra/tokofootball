# tokofootball
--- JAWABAN TUGAS 2 ---
1. Alur implemntasi checklist secara step-by-step
Jawab:
- Membuat sebuah proyek Django baru.
Langkah pertama yang saya lakukan adalah membuat sebuah proyek Django baru dahulu dengan mengikuti langkah-langkah yang ada pada tutorial 0 sebagai fondasi awal sebelum benar-benar engerjakan checklist Tugas 2. Hal ini saya lakukan untuk memastikan bahwa saya memahami alur pembuatan proyek Django dari nol, mulai dari inisialisasi proyek hingga konfigurasi awal.
Pada tahap ini, saya juga sempat mencoba melakukan push proyek ke GitHub serta melakukan deployment awal ke PWS. Tujuan dari langkah ini adalah untuk mengetes apakah proyek yang saya buat dapat dijalankan dengan benar, baik di lingkungan lokal maupun ketika di-hosting secara online. Dengan begitu, saya dapat memvalidasi sejak awal bahwa integrasi GitHub dan PWS berjalan sebagaimana mestinya.
Namun, perlu dicatat bahwa kode yang saya push pada tahap awal ini belum sesuai dengan spesifikasi Tugas 2. Hal tersebut masih berupa hasil dari tutorial 0 yang saya ikuti sebelumnya. Setelah tahap uji coba berhasil, barulah saya menyesuaikan isi proyek agar selaras dengan poin-poin checklist yang ditetapkan pada Tugas 2.
- Membuat aplikasi dengan nama main pada proyek tersebut.
Setelah berhasil membuat proyek Django, saya melanjutkan dengan menambahkan sebuah aplikasi baru bernama main => path('', include('main.urls')). Aplikasi ini saya gunakan sebagai tempat khusus untuk menampung fitur inti dari sistem yang sedang dibangun. Dengan adanya aplikasi main, saya bisa memisahkan logika utama dari aplikasi dengan konfigurasi proyek secara keseluruhan.
- Membuat Model Product pada Aplikasi main
Pada tahap ini, saya mendefinisikan sebuah model dengan nama Product di dalam file main/models.py untuk menyediakan representasi data produk yang terintegrasi dengan database, sehingga nantinya data produk dapat dikelola secara dinamis.
- Membuat sebuah fungsi pada views.py
Selanjutnya, saya membuat fungsi home di dalam main/views.py yang mengembalikan sebuah template HTML. Fungsi ini juga dilengkapi dengan context berupa informasi nama aplikasi, nama saya, dan kelas saya
- Membuat sebuah routing pada urls.py aplikasi main
Untuk memetakan fungsi home tersebut, saya menambahkan file urls.py di dalam folder main. Dengan cara ini, jika di kemudian hari terdapat fungsi tambahan pada aplikasi main, semua routing dapat dikelola secara terpusat.
- Melakukan Deployment ke PWS
Langkah terakhir yang saya lakukan adalah melakukan deployment aplikasi ke Platform Web Service (PWS) agar aplikasi dapat diakses secara online oleh orang lain. Karena sejak awal pembuatan proyek Django saya sudah menyiapkan file requirements.txt, maka pada tahap ini saya hanya perlu melakukan push kode ke GitHub agar repository dapat diakses secara publik oleh server PWS, lalu melakukan clone repository tersebut di PWS. Dengan langkah-langkah ini, aplikasi dapat dijalankan dan diakses melalui domain yang sudah disediakan oleh PWS.

2. Bagan request client ke web aplikasi berbasis Django 
Foto bagan :
https://drive.google.com/file/d/1fknQhR7RfwyBuawGhGt_GoQE6yieYDSs/view?usp=sharing
- Client Request → urls.py: Saat pengguna mengakses aplikasi, permintaan pertama kali diarahkan ke urls.py untuk dicocokkan dengan pola URL.
- urls.py → views.py: Jika ada URL yang cocok, permintaan diteruskan ke fungsi yang ada di views.py.
- views.py → models.py: Jika tampilan membutuhkan data dari database, views.py akan memanggil models.py untuk mengambil atau memproses data.
- views.py → Template (HTML): Setelah data siap, views.py akan mengirimkan data tersebut ke template HTML agar bisa ditampilkan secara visual.
- Template (HTML) → Client Response: Hasil akhirnya adalah halaman web yang sudah berisi data, lalu dikirim kembali ke pengguna sebagai respon.

3. Jelaskan peran settings.py dalam proyek Django!
settings.py berperan sebagai otak konfigurasi dari proyek Django. Tanpa file ini, aplikasi tidak bisa berjalan karena Django tidak tahu bagaimana harus menghubungkan komponen-komponen di dalam proyek.Beberapa peran pentingnya yaitu Konfigurasi Proyek (INSTALLED_APPS, MIDDLEWARE, ROOT_URLCONF, WSGI_APPLICATION), Pengaturan Database (DATABASES), Konfigurasi Template dan Static Files (TEMPLATES, STATIC_URL, MEDIA_URL), Pengaturan Keamanan (SECRET_KEY, ALLOWED_HOSTS, CSRF_COOKIE_SECURE), Pengaturan Bahasa dan Waktu (LANGUAGE_CODE, TIME_ZONE, USE_I18N, USE_TZ), Pengaturan Tambahan (API key, konfigurasi email, atau logging)

4.Bagaimana cara kerja migrasi database di Django
Migrasi database di Django adalah proses untuk menyelaraskan struktur database dengan model yang sudah kita definisikan di kode Python. Setiap kali membuat atau mengubah model (misalnya menambah field baru, mengganti tipe data, atau membuat tabel baru), Django tidak langsung mengubah database, tapi menyimpan perubahan itu dalam bentuk migration file. File ini berisi instruksi tentang apa yang harus dilakukan pada database. Setelah itu, dengan menjalankan perintah python manage.py migrate untuk benar-benar mengeksekusi instruksi tersebut di database. Dengan cara ini, database dan model selalu sinkron tanpa perlu kita menulis query SQL secara manual.

5. Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, Django dipilih sebagai permulaan dalam pembelajaran pengembangan perangkat lunak karena framework ini sudah menyediakan banyak fitur bawaan yang memudahkan pemula untuk langsung fokus ke logika aplikasi tanpa perlu repot membangun segalanya dari nol. Django memiliki struktur yang jelas, dokumentasi yang lengkap, serta komunitas yang besar sehingga mudah dipelajari. Sehingga Djanggo cocok sebagai pondasi belajar sebelum beralih ke framework lain yang mungkin lebih ringan tetapi membutuhkan lebih banyak konfigurasi manual

6. Feedback untuk asisten dosen tutorial 1
Menurut saya, tidak ada feedback khusus yang perlu diberikan untuk asisten dosen pada tutorial 1, karena materi yang disampaikan sudah sangat jelas dan mudah dipahami. Selain itu, para asisten dosen juga menunjukkan kerelaan untuk membantu kami meskipun di luar jam kuliah, sehingga kami merasa sangat terbantu dalam memahami materi dan menyelesaikan tugas.


--- JAWAB TUGAS 3 ---
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
==> Kita memerlukan data delivery karena platform hanya bisa berjalan baik jika data dapat dikirim dan diterima dengan cepat, aman, dan konsisten. Tanpa data delivery, informasi antar komponen tidak terhubung, integrasi sistem gagal, pengalaman pengguna terganggu, serta analisis dan pengambilan keputusan tidak bisa dilakukan.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
==> JSON lebih populer dibandingkan XML karena strukturnya yang lebih sederhana, ringkas, dan mudah dipahami, sehingga parsing data menjadi lebih cepat dan efisien tanpa banyak tag pembuka-penutup seperti pada XML; selain itu, JSON terintegrasi erat dengan JavaScript dan didukung luas oleh berbagai bahasa pemrograman modern, membuatnya lebih praktis untuk pertukaran data pada web API dan aplikasi berbasis web, sementara XML cenderung digunakan untuk kebutuhan dokumen kompleks atau sistem legacy.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
==> is_valid() pada form Django berfungsi untuk memeriksa apakah data input sesuai aturan validasi. Kita membutuhkannya agar hanya data yang valid, konsisten, dan aman yang diproses atau disimpan ke database.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
==> Kita membutuhkan csrf_token pada form Django untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF), yaitu serangan di mana penyerang memanfaatkan sesi login pengguna untuk mengirim permintaan berbahaya tanpa sepengetahuan mereka. Jika csrf_token tidak ditambahkan, server tidak bisa membedakan apakah permintaan berasal dari form asli aplikasi atau dari situs berbahaya, sehingga penyerang dapat memanfaatkan hal ini untuk melakukan aksi berbahaya seperti mengubah password, mentransfer saldo, atau menghapus data hanya dengan membuat korban membuka link atau halaman palsu. Dengan adanya csrf_token, setiap permintaan POST harus menyertakan token unik yang diverifikasi server, sehingga serangan CSRF dapat dicegah.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
==> dari model → form → views (HTML & XML/JSON) → urls → templates → testing & deployment consideration

6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
==> Asdos pada tutorial 2 sangat membantu karena selalu mengarahkan dengan jelas saat ada kesulitan. Penjelasannya runtut, sabar, dan membuat materi lebih mudah dipahami sehingga pengerjaan tugas jadi lebih terarah

Link SS Postman
https://drive.google.com/drive/folders/1CMvS0Q7wnAiDqXWVxxXhZ7SV8GaeKPAU?usp=sharing