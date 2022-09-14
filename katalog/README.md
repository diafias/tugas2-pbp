Bagan Request Cient Flow Django

![pbp](https://user-images.githubusercontent.com/103547887/190079933-c7b87d2b-78d4-410a-81aa-82a0c3da2a16.png)

1. User mengirimkan HTTP request ke server saat mengakses web-application
2. Kemudian ditangkap oleh urls.py lalu dihubungkan ke view yang bersesuaian dengan request.
   Fungsi urls.py ini juga berfungsi untuk mencocokkan pola string atau digit yang muncul pada URL dan mengantarkannya ke view function sebagai data.
3. View.py ini berfungsi sebagai request handler yang akan menerima HTTP request lalu return HTTP response.
   Selain itu juga akan mengakses data untuk memenuhi request melalui models ke templates yang tersedia.
4. Models ini mendefinisikan struktur data dari suatu aplikasi dan menyediakan mekanisme dan memasukkan query ke database.
5. Template untuk mendefinisikan struktur atau tampilan dari file seperti HTML dengan placeholder yang digunakan untuk merepresentasikan konten. View ini membuat HTML dengan menggunakan template dan mengisinya dari model. Template ini mendefinisikan struktur file berjenis apapun.

Mengapa perlu virtual environtment
Saat mengembangkan aplikasi python, pasti harus menginstall python, lalu menginstall seluruh library yang diperlukan, lalu menuliskan code dalam suatu file .py. Dan bisa dijalankan melalui terminal. Hal tersebut yang biasa dilakukan oleh pemula. Hal ini cocok untuk project yang ukuran kecil, tapi bagaimana jika sangat kompleks. 
Pastinya akan sangat kesusahan. Maka, kita harus mengisolasi python environtment hanya untuk project tersebut saja. Hal ini berguna agar kita tidak eror saat perbedaan versi dan jenis dependensi untuk project yang berbeda. Selain itu, juga akan mengisolasi python yang akan digunakan untuk membangun project python global pada sistem. 
Sebenarnya penggunaan virtual environtment ini tidak diwajibkan pada aplikasi web berbasis django. Tapi, pasti akan menyusahkan para pengembang dikemudian hari. 

Implementasi aplikasi katalog
1. Pada aplikasi katalog akan dibuat fungsi bernama show_katalog yang akan menerima parameter request dan me-return render(request, "katalog.hml").
2. Lalu file urls.py pada aplikasi katalog akan melakukan routing pada fungsi views. Sehingga nanti halaman HTML katalog dapat ditampilkan ke browser client. Tambahkan aplikasi katalog ke urls.py yang terdapat pada folder project_django dengan menambahkan kode path(‘katalog/‘, include(‘katalog.urls.’)) pada variabel urlpatterns
3. Load data json pakai syntax python manage.py loaddata initial_catalog_data.json. Pada fungsi views, import models yang ada pada view.py. Lalu pada fungsi show_katalog, juga update fungsi sehingga bisa panggil fungsi query ke model database lalu menyimpan hasilnya ke dalam variabel context. Data nya context akan ikut di render oleh django sehingga bisa muncul ke HTML. Maka akan diperlukan iterasi untuk menampilkan pada variabel list_item.
4. Lakukan deploy, tambahkan file procfile untuk mengatur deployment. Lalu pilih mneu aplikasi baru pada heroku, hubungkan di github, setting, dan aplikasi selesai.  
