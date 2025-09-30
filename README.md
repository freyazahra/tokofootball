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

--- JAWAB TUGAS 4 ---
1. AuthenticationForm adalah salah satu fitur bawaan Django yang berfungsi sebagai formulir (form) untuk proses login pengguna. Formulir ini sudah dirancang khusus untuk memvalidasi username dan password yang dimasukkan pengguna.

Kelebihan (AuthenticationForm)
- Sangat Mudah Digunakan
Anda tidak perlu membuat kode form yang panjang. Cukup dengan mengimpor AuthenticationForm, Anda sudah bisa membuat halaman login yang berfungsi. Ini sangat menghemat waktu, terutama untuk proyek yang sederhana.
- Integrasi Penuh
Form ini terintegrasi langsung dengan sistem otentikasi (authentication system) bawaan Django. Ini berarti ia langsung bisa berkomunikasi dengan model User dan metode-metode otentikasi lainnya.
- Keamanan Terjamin
AuthenticationForm secara otomatis menangani validasi kredensial (username dan password) dengan aman. Ini termasuk penggunaan hashing password yang aman dan melindungi dari serangan umum.
- Pesan Kesalahan Jelas
Jika pengguna salah memasukkan username atau password, form ini akan menampilkan pesan kesalahan yang informatif seperti "Nama pengguna atau kata sandi tidak cocok."

Kekurangan (AuthenticationForm)
- Tidak Bisa Dikustomisasi Secara Langsung
AuthenticationForm dirancang untuk skenario yang sangat spesifik: login dengan username dan password. Jika Anda ingin menambahkan field lain seperti email, nomor telepon, atau captcha, Anda harus membuat form kustom sendiri, bukan memodifikasi AuthenticationForm ini.
-  Hanya untuk Login
Seperti namanya, form ini khusus untuk proses login. Anda tidak bisa menggunakannya untuk pendaftaran (registrasi) pengguna baru. Untuk itu, Anda harus menggunakan atau membuat form lain.
- Tidak Menangani Proses Login Sepenuhnya
AuthenticationForm hanya bertugas memvalidasi data. Setelah data valid, Anda tetap harus menulis kode di view Anda untuk benar-benar membuat pengguna ter-otentikasi (ter-login) menggunakan fungsi login(request, user).

2. Perbedaan utama antara autentikasi dan otorisasi terletak pada tujuannya. Autentikasi adalah proses pembuktian identitas, yang menjawab pertanyaan "Siapakah saya?" Contohnya saat memasukkan nama pengguna dan kata sandi untuk login. Setelah identitas terverifikasi melalui autentikasi, sistem beralih ke proses otorisasi, yang menentukan hak akses apa saja yang dimiliki. Otorisasi menjawab pertanyaan "Apa yang bisa saya lakukan?" Misalnya, meskipun sudah berhasil login sebagai pengguna, saya mungkin tidak diizinkan menghapus data atau mengakses halaman admin karena hak akses saya tidak mencakup tindakan tersebut. Singkatnya, autentikasi adalah tiket masuk, sedangkan otorisasi adalah aturan yang mengatur apa yang bisa saya lakukan di dalam.

3. Kelebihan dan kekurangan utama antara session dan cookies dalam menyimpan state pada aplikasi web terletak pada lokasi penyimpanannya. Cookies menyimpan data langsung di sisi klien (browser), menjadikannya cepat dan fleksibel untuk data yang tidak sensitif seperti preferensi tampilan, namun memiliki batasan ukuran yang kecil (sekitar 4KB) dan kurang aman karena data dapat diakses serta dimanipulasi oleh pengguna. Sebaliknya, session menyimpan data di sisi server dan hanya menyertakan ID session di browser, sehingga sangat aman untuk menyimpan informasi sensitif seperti status login dan keranjang belanja, serta memungkinkan penyimpanan data dalam jumlah besar tanpa batasan. Namun, session memiliki kelemahan karena menggunakan sumber daya server dan dapat mempersulit penskalaan aplikasi karena setiap state pengguna terikat pada server tertentu. Oleh karena itu, pemilihan antara keduanya bergantung pada tingkat keamanan dan volume data yang perlu dikelola.

4. Walaupun cookies sering digunakan, secara bawaan penggunaan cookies tidak aman dalam pengembangan web karena data yang tersimpan di sisi klien rentan terhadap manipulasi dan pencurian melalui serangan seperti Cross-Site Scripting (XSS). Namun, Django menangani risiko ini dengan beberapa fitur keamanan bawaan: ia tidak menyimpan data session secara langsung di cookie melainkan hanya menyimpan ID session yang telah ditandatangani secara digital (signed cookies), yang mencegah manipulasi. Selain itu, Django secara default menyetel flag HttpOnly pada cookie sesi untuk mencegah skrip berbahaya mencurinya, dan menyediakan mekanisme perlindungan Cross-Site Request Forgery (CSRF) yang kuat dengan menggunakan token unik untuk memvalidasi permintaan formulir. Dengan demikian, meskipun cookies memiliki risiko, Django menyediakan kerangka keamanan yang solid, asalkan developer tetap menggunakan session untuk data sensitif.

5. mengimplementasikan checklist di atas secara step-by-step
    1) Mengimplementasikan Fungsi Otentikasi
    Saya akan memulai dengan menerapkan fitur dasar otentikasi: registrasi, login, dan logout.
    - Registrasi: Saya akan membuat Form khusus untuk mendaftarkan pengguna baru (misalnya, UserCreationForm di Django) dan membuat view untuk memprosesnya. Di view ini, setelah validasi berhasil, saya akan menyimpan pengguna baru ke database dan mengarahkan mereka ke halaman login.
    - Login: Saya akan menggunakan AuthenticationForm yang sudah dibahas sebelumnya. View login akan memproses formulir ini. Jika kredensial valid, saya akan menggunakan fungsi authenticate() untuk memverifikasi pengguna, lalu login() untuk membuat sesi.
    - Logout: Ini adalah yang paling sederhana. Saya akan membuat view yang hanya memanggil fungsi logout() dan mengarahkan pengguna ke halaman utama.

    2) Menghubungkan Model Product dengan User
    Langkah ini penting untuk otorisasi. Saya akan memodifikasi model Product dengan menambahkan ForeignKey ke model User. Ini akan memungkinkan setiap produk memiliki "pemilik" atau pembuat. Contohnya, saya bisa menambahkan owner = models.ForeignKey(User, on_delete=models.CASCADE) di model Product. Relasi ini memungkinkan saya untuk menampilkan produk yang spesifik untuk pengguna yang sedang logged in, dan mencegah pengguna lain untuk mengubah produk yang bukan miliknya.

    3) Menampilkan Detail Pengguna dan Menerapkan Cookies
    Setelah otentikasi dan relasi model siap, saya akan menampilkan informasi pengguna di halaman utama. Di dalam template HTML, saya dapat menggunakan variabel {{ user.username }} untuk menampilkan nama pengguna yang sedang logged in. Untuk menerapkan cookies seperti last_login, saya akan menggunakannya sebagai bagian dari session Django. Django secara otomatis menyimpan timestamp login terakhir di model User.

    4) Membuat Akun Pengguna dan Dummy Data (dilakukan di akhir)
    Langkah ini saya tempatkan di akhir karena bersifat konfigurasi dan bukan implementasi fitur. Setelah semua fungsi utama (otentikasi, relasi, dan tampilan data) berhasil diuji, barulah saya akan membuat data dummy untuk pengujian lebih lanjut.

--- JAWAB TUGAS 4 ---
1. Urutan prioritas CSS selector
    1) Inline style (ditulis langsung di atribut elemen) memiliki prioritas paling tinggi.
    2) ID selector (#id) lebih tinggi daripada class atau tag.
    3) Class, pseudo-class, attribute selector (.class, :hover, [type="text"]).
    4) Tag/element selector (div, p, h1).
    5) Jika spesifisitas sama, maka aturan yang ditulis paling akhir (lebih bawah di file CSS) akan dipakai.Selain itu, penggunaan !important akan mengesampingkan aturan lainnya, meskipun sebaiknya digunakan dengan hati-hati.

2. Pentingnya responsive design
Responsive design penting karena memastikan tampilan website bisa menyesuaikan berbagai ukuran layar (desktop, tablet, mobile), sehingga pengalaman pengguna konsisten dan nyaman. Contoh aplikasi yang sudah menerapkan responsive design adalah Shopee: layout produk dan tombolnya otomatis menyesuaikan ketika dibuka di HP maupun PC. Sedangkan contoh aplikasi yang belum menerapkan responsive design adalah website lama dengan layout fixed width (misalnya situs sekolah lama yang tampilannya “melebar” di desktop tapi harus zoom in/out di HP), sehingga tidak ramah pengguna.

3. Perbedaan margin, border, padding
    - Margin adalah jarak luar elemen terhadap elemen lain.
    - Border adalah garis tepi elemen yang berada di antara margin dan padding.
    - Padding adalah jarak antara isi elemen (content) dengan tepi dalam border.
    Contoh implementasi CSS:
    .card {
        margin: 20px;     /* jarak antar card */
        border: 2px solid black;  /* garis tepi */
        padding: 15px;    /* jarak isi dengan border */
        }

4. Flexbox dan Grid Layout
Flexbox digunakan untuk mengatur tata letak dalam satu dimensi (baris atau kolom). Berguna untuk membuat elemen sejajar, rata tengah, atau dibagi fleksibel. Contoh: navbar yang otomatis rapi meskipun jumlah menu berubah.
Grid Layout digunakan untuk mengatur tata letak dua dimensi (baris dan kolom), cocok untuk layout kompleks seperti dashboard atau galeri produk. Contoh: menampilkan daftar produk dalam bentuk grid dengan jumlah kolom yang menyesuaikan ukuran layar.

5. Implementasi checklist step-by-step (dalam satu paragraf)
Pertama, saya menyiapkan struktur HTML dasar dari halaman-halaman yang sudah ada (login, register, tambah produk, edit produk, detail produk, dan daftar produk). Setelah itu, saya memilih framework CSS (misalnya Tailwind) untuk mempercepat styling, kemudian mulai mengatur tampilan tiap halaman agar lebih menarik dengan menambahkan warna, ukuran font, dan tata letak yang rapi. Pada halaman daftar produk, saya menambahkan kondisi menggunakan template engine: jika tidak ada produk, tampilkan gambar placeholder dan pesan khusus; jika ada, tampilkan produk dalam bentuk card dengan desain kustom yang berbeda dari tutorial. Setiap card saya lengkapi dengan tombol edit dan hapus yang terhubung ke fungsionalitas backend. Untuk navigasi, saya membuat navbar yang memuat link ke fitur utama aplikasi dan memastikan responsivitas dengan class CSS bawaan framework (misalnya flex, grid, hidden md:block) sehingga tampilan menyesuaikan baik di desktop maupun mobile. Dengan cara ini, setiap fitur pada checklist bisa terpenuhi secara sistematis tanpa hanya mengikuti template bawaan tutorial.