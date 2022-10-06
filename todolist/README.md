1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

CSRF (Cross-site request forgery) adalah memaksa pengguna akhir untuk melakukan tindakan yang tidak diinginkan pada aplikasi web di mana mereka telah mengautentikasi diri mereka sendiri. Penyerang menggunakan status terotentikasi user untuk keuntungan mereka dengan mengubah permintaan user, yang mendorong user untuk melakukan tindakan yang tidak ingin mereka lakukan. Jika serangan berhasil pada akun administratif, itu dapat membahayakan seluruh aplikasi web. CSRF adalah serangan umum, jadi Django memiliki implementasi yang sangat sederhana untuk meniadakan serangan ini. Django memiliki tag {% csrf_token %} yang diimplementasikan untuk menghindari serangan berbahaya. Ini menghasilkan token di sisi server saat merender halaman dan memastikan untuk memeriksa ulang token ini untuk setiap permintaan yang masuk kembali. Jika permintaan yang masuk tidak berisi token, permintaan tersebut tidak akan dieksekusi. Apabila tidak ada potongan kode ini, maka seperti tidak ada perlindungan pada suatu aplikasi tersebut.

2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

Jawabannya bisa dikerjakan secara manual. Jika secara manual, dia akan menggunakan input secara manual dimasukkan satu persatu. Lihat saja contohnya pada login html dan bagian register html. Pada login html, terdapat bagian input secara terpisah. Dan bagian register html, contoh yanng menggunakan {{ form.as_table }}.

3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

Pembuatan form ini digunakan untuk mengambil informasi dari user, title dan description nya akan masuk pada class pada form, lalu akan terhubung pada fungsi add_task pada views.py. Lalu akan lakukan validasi, kalau input nya benar, data akan masuk menjadi value dari attribute title dan description.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

startapp todolist, memasukkan path dalam urls.py, membuat models.py, membuat beberapa fungsi di views.py seperti fungsi register, login, logout, dilanjutkan dengan pengimplementasian register.html, login.html, dan halaman utama todolist.html, lalu menambahkan halaman ask_task untuk meminta user memasukkan beberapa task, dibuatlah halaman add_task.html dan ini akan terhubung pada fungsi add_task pada views.py. Jika sudah selesai, coba lah untuk runserver. Kemudian, jalankan.


5. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

Internal CSS adalah kode CSS yang ditulis di dalam tag <style> dan kode HTML dituliskan di bagian atas (header) file HTML. Internal CSS dapat digunakan untuk membuat tampilan pada satu halaman website dan tidak digunakan pada halaman website yang lain. Cara ini akan sangat cocok dipakai untuk menciptakan halaman web dengan tampilan yang berbeda.
Kelebihan : bisa mengubah pada halaman itu saja, tidak perlu upload beberapa file karena HTML dan CSS dalam 1 file, class dan id bisa digunakan disini.
Kekurangan : tidak efisien apabila ingin menggunakan CSS dalam beberapa file, membuat performa website menjadi lebih lemot, sebab css yang berbeda akan sebabkan loading ulang saat ingin membuka halaman website baru.

External CSS adalah kode CSS yang ditulis terpisah dengan kode HTML Eksternal CSS ditulis di sebuah file khusus yang berekstensi .css. File eksternal CSS biasanya diletakkan setelah bagian <head> pada halaman.
Kelebihan : struktur kode menjadi lebih rapi, loading website menjadi lebih cepat, file css nya bisa digunakan di beberapa halaman website.
Kekurangan : halaman akan menajdi berantakan, ketika pemanggilan file css gagal oleh file HTML.

Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Setiap elemen HTML memiliki atribut style, di situ lah inline CSS ditulis. Cara ini kurang efisien karena setiap tag HTML yang diberikan harus memiliki style masing-masing. Anda akan lebih sulit dalam mengatur website jika hanya menggunakan inline style CSS. Sebab, Inline CSS digunakan hanya untuk mengubah satu elemen saja.
Kelebihan : membantu saat ingin melihat perubahan pada 1 elemen saja, memperbaiki kode dengan cepat, proses load lebih cepat.
Kekurangan : tidak efisien karena hanya diterapkan pada 1 elemen saja. 

6. Jelaskan tag HTML5 yang kamu ketahui.
Tag <header>...</header> merupakan bagian kepala dari dokumen.
Tag <nav>...</nav> merupakan bagian dari dokumen yang dimaksudkan untuk memudahkan dalam proses navigasi.
Tag <section>...</section> merupakan dokumen atau aplikasi bagian generik. Hal ini dapat digunakan bersama-sama dengan h1-h6 untuk menunjukkan struktur dokumen.
Tag <aside>...</aside> merupakan gambaran dari sebagian konten yang berhubungan dengan isi halaman.
Tag <figure>...</figure> digunakan untuk menghubungkan keterangan bersama-sama dengan beberapa konten tertanam, seperti gambar atau video.

7. Jelaskan tipe-tipe CSS selector yang kamu ketahui.
- Element Selector menggunakan tag HTML sebagai selector untuk mengubah properti yang terdapat dalam tag tersebut.
h1 {
  color: #fca205;
  font-family: "Monospace";
  font-style: italic;
}
- ID selector menggunakan ID pada tag sebagai selector-nya. Kamu dapat menambahkan ID pada templat HTML sebagai berikut (ID harus bersifat unik). Kemudian tambahkan ID tersebut sebagai selector pada file CSS kamu.
- Class selector yang dapat digunakan untuk memperindah tampilan templat HTML. Tambahkan beberapa class pada tag HTML. Kemudian tambahkan class selector berikut pada file CSS kamu.

8. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- Merubah halaman login menjadi semenarik mungkin, saya menggunakan card pada bagian login dan ada efek hovernya. Lalu meletakkan card tersebut pada bagian tengah halaman dan mengubah background serta memadukan warna. 
- Mengubah halam todolist, saya menambahkan navbar pada bagian atasnya sehingga menjadi seperti kepala pada halaman tersebut. 
