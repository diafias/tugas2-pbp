1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

    Asynchronous adalah proses jalannya program bisa dilakukan secara bersamaan tanpa harus menunggu proses antrian. Synchronous merupakan bagian dari Asynchronous (1 antrian) dimana proses akan dieksekusi secara bersamaan dan untuk hasil tergantung lama proses suatu fungsi synchronous . Asynchronouse hampir disemua Bahasa pemrograman ada namun untuk PHP masih belum ada. PHP sebagai server side hanya menyediakan synchronous namun bisanya di WEB Developers tetap digunakan namun menggunakan AJAX (Asynchronous Javascript And XML) untuk proses Asynchronouse.
    
    Synchronous adalah proses jalannya program secara sequential , disini yang dimaksud sequential ada berdasarkan antrian ekseskusi program. Pada dasarnya semua Bahasa pemrograman menggunakan Asynchronouse terutama PHP.

2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

    Event-Driven Programming adalah salah satu teknik pemogramman, yang konsep kerjanya tergantung dari kejadian atau event tertentu. Contohnya itu adalah pada saat bagian add_task, jika diklik oleh user maka akan menyebabkan event yang terjadi, yaitu akan muncul modal pada laman website.

3. Jelaskan penerapan asynchronous programming pada AJAX.

    Istilah teknis AJAX “Asynchronous JavaScript and XML” menunjukkan teknik berbasis teknologi JavaScript yang mengubah komunikasi dengan server dan mempercepat aplikasi web. Antarmuka bekerja lebih cepat dengan transfer data tertunda (asinkron). Dengan AJAX, aplikasi web bisa bertukar data dengan server di background tanpa halaman yang lengkap harus reload.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

    - membuat view baru untuk mengembalikan data dalam bentuk json
    - membuat path /todolist/json pada url.py 
    - menggunakan AJAX get untuk menampilkan data
    - membuat bagian untuk menambahkan task baru dengan form untuk menambahkannya, lalu menambahkannya ke path
