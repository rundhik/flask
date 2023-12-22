# Tutorial Flask

## Dynamic Routing

### Sekilas

_Dynamic routing_ digunakan untuk mengakses URL dengan memberikan _parameter_ (nilai) berdasarkan dari _input_-an pengguna sesuai kebutuhan. Hal-hal yang diuji coba adalah :

- Menggunakan satu parameter
- Menggunakan lebih dari satu parameter
- Menggunakan prefiks dan parameter
- Menggunakan parameter sekaligus memberikan nilai default pada parameter

_Routing_ merupakan komponen mutlak yang harus ada pada sumber kode Flask. Fungsi _Routing_ selalu beriringan dengan _Controller_.

### Implementasi

- Masuk ke dalam environment Python.

      > venv\Scripts\activate
      (venv) >

- Buat file `app.py`.
- Impor pustaka yang digunakan

      from flask import Flask

- Inisiasi _library_ Flask menggunakan variabel **aplikasi**.

      aplikasi = Flask(__name__)

- Membuat default _routing_

  _Routing_ pertama pada alamat ``/`` dengan nama fungsi ``index`` sebagai controller yang menghasilkan nilai *return* berupa tipe data string dalam bentuk kode HTML.

        @aplikasi.route('/')
        def index():
            return '''
            <h1>Tutorial Flask</h1>
            <p>Selamat datang di tutorial aplikasi web menggunakan Flask</p>
            '''

- Membuat _routing_ satu parameter

    _Routing_ kedua menggunakan URL dinamis dengan nama fungsi `page` sebagai controller. Nilai dinamis yang di-_input_-kan pengguna pada URL nantinya, akan ditampung dalam variabel parameter `halaman` pada fungsi `page`. Untuk menampilkan variabel dinamisnya, pada contoh berikut dengan memanfaatkan _built-in method_ dari Python yaitu _method_ `format()`. Cara menggunakannya dengan meletakkan tanda kurung kurawal (_curly bracket_ : { }) pada tipe data _string_ (dalam kasus ini tipe data _string_ adalah yang diapit oleh tanda petik tiga), selanjutnya melakukan parsing dengan menambahkan tanda _dot_ (tanda titik : .) setelah tipe data _string_ dan mengisi parameter _method_ `format` dengan nama variabel pada fungsi `page`.

        @aplikasi.route('/<halaman>')
        def page(halaman):
            return '''
            <h1>Ini halaman {}</h1>
            <a href='/'>Kembali</a>
            '''.format(halaman)

- Membuat _routing_ menggunakan lebih dari satu parameter

    _Routing_ ketiga masih menggunakan URL dinamis dengan lebih dari satu parameter. Sama seperti pada _routing_ kedua, _parsing_ parameter variabelnya masih menggunakan _method_ `format()`. Perhatikan ketika melakukan parsing, bahwa parameter dalam _method_ `format()` akan menentukan urutan variabel yang ditampilkan pada tanda kurung kurawal yang sudah disisipkan pada tipe data _string_. Kemudian pada properti `title()`, merupakan _method_ properti dari _method_ `format()` untuk menjadikan karakter pertama pada tipe data _string_ menjadi huruf kapital.

        @aplikasi.route('/<name>/<nickname>')
        def user(name, nickname):
            return '''
            <h1>Halo {},</h1>
            <h3>Selamat Datang {} di Tutorial Flask</h3>
            <a href='/'>Kembali</a>
            '''.format(nickname, name.title())

- Membuat _routing_ menggunakan prefiks dan parameter

    _Routing_ keempat menambahkan prefiks URL `/layanan` sebelum parameter URL. Cara ini mengharuskan menyertakan prefiks URL `/layanan/` sebelum memasukkan parameter URL-nya ketika mengakses. Berbeda dengan _controller_ sebelumnya, cara parsing variabel pada fungsi `services()` dan `product()` tidak menggunakan _method_ `format()` melainkan dengan menyisipkan variabel secara langsung menggunakan tanda + sebagai operator diantara tipe data _string_.

        @aplikasi.route('/layanan/<layanan>')
        def services(layanan):
            return '<h1>' + layanan.capitalize() + '</h1>' + '<h3>Ini halaman ' + layanan + '</h3> <a href="/">Kembali</a>'

        @aplikasi.route('/produk/<produk>')
        def product(produk):
            return '''<h1>Produk : {}</h1>'''.format(produk.capitalize()) + \
            '''<h3>Menampilkan produk ''' + produk.capitalize() + \
            '''</h3> <a href="/">Kembali</a>'''

- Membuat _routing_ menggunakan parameter sekaligus memberikan nilai default pada parameter

    _Routing_ kelima menggabungkan dengan metode-metode sebelumnya sekaligus menerapkan nilai default pada parameter. Tahapannya adalah menentukan nama variable parameter beserta nilai defaultnya pada _decorator property_ `@aplikasi`.

        @aplikasi.route('/item', defaults={'mode': 'create', 'item_id': 0})

    Baris tersebut menjelaskan bahwa parameter yang nantinya akan dipakai ditampung pada variabel `mode` dan variabel `item_id`. Selanjutnya menentukan posisi ketika mengakses URL nantinya, pada _decorator property_ dibawahnya.

        @aplikasi.route('/item/<string:mode>/<int:item_id>')

    Baris tersebut menjelaskan bahwa untuk variabel parameter `mode` menggunakan tipe data _string_. Sedangkan untuk variabel parameter `item_id` menggunakan tipe data _integer_. Penjelasan dua baris ini adalah sebagai berikut :

    - Saat mengakses dengan URL `http://[SERVER_NAME]/item` maka _decorator property_ yang aktif adalah `@aplikasi.route('/item', defaults={'mode': 'create', 'item_id': 0})`. Karena tidak memasukkan variabel parameter didalamnya, maka diterjemahkan dalam _request_ sebagai `http://[SERVER_NAME]/item/create/0`. Artinya secara otomatis variabel parameter `mode` memiliki nilai `create` sedangkan variabel parameter `item_id` memiliki nilai `0`.

    - Saat mengakses dengan URL `http://[SERVER_NAME]/item/edit/10` maka _decorator property_ yang aktif adalah ` @aplikasi.route('/item/<string:mode>/<int:item_id>')`. Sehingga secara otomatis variabel parameter `mode` memiliki nilai `edit` sedangkan variabel parameter `item_id` memiliki nilai `10`.

    Selanjutnya bisa menentukan algoritma pada fungsi `item()` sesuai kebutuhan seperti pada baris kode berikut.

        @aplikasi.route('/item', defaults={'mode': 'create', 'item_id': 0})
        @aplikasi.route('/item/<string:mode>/<int:item_id>')
        def item(mode, item_id):
            if mode == 'show':
                return '<h1>Halaman Show</h1><h3>Menampilkan Produk : {} </h3> <a href="/">Kembali</a>'.format(item_id)
            elif mode == 'edit':
                return '<h1>Halaman Edit</h1><h3>Mengedit Produk : {} </h3> <a href="/">Kembali</a>'.format(item_id)
            elif mode == 'delete':
                return '<h1>Halaman Hapus</h1><h3>Menghapus Produk : {} </h3> <a href="/">Kembali</a>'.format(item_id)
            else:
                return '<h1>Halaman Create</h1><h3>Melakukan penambahan (insert) Produk </h3> <a href="/">Kembali</a>'.format(item_id)

- Menjalankan aplikasi.

      (venv) > python app.py
       * Serving Flask app 'app'
       * Debug mode: on
      WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
       * Running on http://127.0.0.1:9000
      Press CTRL+C to quit
       * Restarting with stat
       * Debugger is active!
       * Debugger PIN: 943-076-614

- Buka alamat `http://127.0.0.1:9000` melalui browser untuk meangakses _routing_ default.
- Buka alamat `http://127.0.0.1:9000/kontak` untuk mengakses _routing_ dengan satu parameter.
- Buka alamat `http://127.0.0.1:9000/John Doe/john` untuk mengakses _routing_ dengan dua parameter.
- Buka alamat `http://127.0.0.1:9000/layanan/hubungi kami` atau `http://127.0.0.1:9000/produk/laptop`untuk mengakses _routing_ menggunakan prefiks dengan dua parameter.
- Buka alamat `http://127.0.0.1:9000/item` atau `http://127.0.0.1:9000/item/show/10` atau `http://127.0.0.1:9000/item/edit/5` atau `http://127.0.0.1:9000/item/delete/32` untuk mengakses _routing_ menggunakan prefiks dengan dua parameter default.

Akses URL dengan mengubah variabel parameternya untuk mengetahui cara kerja _dyanamic routing_.
