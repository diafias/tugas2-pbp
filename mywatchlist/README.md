[html](https://tugas2-pbp-diyah.herokuapp.com/mywatchlist/html/)
[xml](https://tugas2-pbp-diyah.herokuapp.com/mywatchlist/xml/)
[JSON](https://tugas2-pbp-diyah.herokuapp.com/mywatchlist/json/)

1. XML adalah singkatan dari eWtensible Markup LAnguage. XML ini digunakan untuk self-descriptive, sehingga akan langsung tahun informasi apa yang ingin disampaikan. XML ini biasanya digunakan pada aplikasi web maupun mobile untuk menyimpan dan mengirimkan data. 
Selain itu XML ini juga digunakan untuk pertukaran data, data dapat dipertukarkan antara sistem yang tidak kompatibel. Dokumen XML membentuk struktur seperti tree yang dimulai root, lalu branch, hingga berakhir pada leaves. XML ini harus mengandung root element yang merupakan parent dari elemen lainnya. 
JSON adalah singkatan dari JavaScript Object Notation. Bentuk JSON ini sangat mudah dimengerti. Biasanya digunakan dalam aplikasi web maupun moblie dan untuk menyimpan serta mengirimkan data. JSON ini merupakan turunan dari object JavaScript. Kemudian, data JSOn ini disimpan dalam bentuk key dan value. Key nya itu berupa brand, type, color, dan memory.
Sedangkan value nya itu berisi data primitif (string, number, boolean) atau berupa objek. Kemudian HTML, yang merupakan singkatan dari Hypertext Markup Language adalah bahasa markup standa =r untuk membuat dan menyusun halaman dan aplikasi web.
2. Kenapa  harus menggunakan data delivery karena dalam suatu platform pasti akan mengirimkan data dari satu stack ke stack lainnya. Dan suatu project itu tidak bisa disimpan dalam frontend dan harus disimpan ke backend, maka cara untuk mengirimkannya itu akan membutuhkan suatu data delivery. Ada beberapa format data yang biasanya digunakan antara lain HTML, XML dan JSON.
3. Pengimplementasian check point diatas. Pertama akan membuat sebuah aplikasi yang bernama mywatckhlist, kemudian akan mengedit settings.py dalam project django lalu mengisi nama aplikasi mywatchlist di dalamnya.
   Kemudian akan mengisi models nya dan diisi oleh beberapa variabel yang dibutuhkan. Lalu jalankan perintah migrasi untuk melakukan migrasi ke dalam database django lokal.
   Selanjutnya membuat folder fixtures, lalu ada file initial_mywatchlist_data.json yang isinya adalah list data nama-nama film.
   Lakukan implementasi view dasar, dengan mengedit view.py. Lalu membuat folder templates, dan berisi file mywatchlist.html. Selanjutnya akan lakukan routing. Daftarkan path nya kedalam url.py
   Kemduian, hubungkan models dengan view dan template, import model pada file view.py. Buat sebuah fungsi. Dan selanjutnya akan dilakukan mapping data yang telah ikut di render untuk memunculkan di halaman HTML.
   Selanjutnya implenetasi data dengan format XML dan JSON. Mengedit file view.py pada mywatchlist dan diisi dengan import lalu membuat sebuah fungsi show_xml dan show_json. 
   
POSTMAN HTML
![Screenshot (102)](https://user-images.githubusercontent.com/103547887/191656874-86fb48f0-556a-4a30-b22f-016f9102d309.png)

POSTMAN XML
![Screenshot (103)](https://user-images.githubusercontent.com/103547887/191656909-288f49ac-dda2-4db9-9f7d-5924f6884421.png)

POSTMAN JSON
![Screenshot (104)](https://user-images.githubusercontent.com/103547887/191656933-343a1885-f232-4cd4-8fca-a7308d614c0e.png)
