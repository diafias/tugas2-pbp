1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

CSRF (Cross-site request forgery) adalah memaksa pengguna akhir untuk melakukan tindakan yang tidak diinginkan pada aplikasi web di mana mereka telah mengautentikasi diri mereka sendiri. Penyerang menggunakan status terotentikasi user untuk keuntungan mereka dengan mengubah permintaan user, yang mendorong user untuk melakukan tindakan yang tidak ingin mereka lakukan. Jika serangan berhasil pada akun administratif, itu dapat membahayakan seluruh aplikasi web. CSRF adalah serangan umum, jadi Django memiliki implementasi yang sangat sederhana untuk meniadakan serangan ini. Django memiliki tag {% csrf_token %} yang diimplementasikan untuk menghindari serangan berbahaya. Ini menghasilkan token di sisi server saat merender halaman dan memastikan untuk memeriksa ulang token ini untuk setiap permintaan yang masuk kembali. Jika permintaan yang masuk tidak berisi token, permintaan tersebut tidak akan dieksekusi. Apabila tidak ada potongan kode ini, maka seperti tidak ada perlindungan pada suatu aplikasi tersebut.

2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

Jawabannya bisa dikerjakan secara manual. Jika secara manual, dia akan menggunakan input secara manual dimasukkan satu persatu. Lihat saja contohnya pada login html dan bagian register html. Pada login html, terdapat bagian input secara terpisah. Dan bagian register html, contoh yanng menggunakan {{ form.as_table }}.

3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

Pembuatan form ini digunakan untuk mengambil informasi dari user, title dan description nya akan masuk pada class pada form, lalu akan terhubung pada fungsi add_task pada views.py. Lalu akan lakukan validasi, kalau input nya benar, data akan masuk menjadi value dari attribute title dan description.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

startapp todolist, memasukkan path dalam urls.py, membuat models.py, membuat beberapa fungsi di views.py seperti fungsi register, login, logout, dilanjutkan dengan pengimplementasian register.html, login.html, dan halaman utama todolist.html, lalu menambahkan halaman ask_task untuk meminta user memasukkan beberapa task, dibuatlah halaman add_task.html dan ini akan terhubung pada fungsi add_task pada views.py. Jika sudah selesai, coba lah untuk runserver. Kemudian, jalankan.