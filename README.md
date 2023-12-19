# Tutorial Flask

## Routing

### Sekilas

Flask menggunakan arsitektur kode MVC (Model-View-Controller). Struktur kode minimum dalam Flask dibagi menjadi :

- Pemanggilan pustaka-pustaka (_libraries_) utama yang diperlukan
- Inisiasi _library_
- Routing / Controller
- Model / Database
- Eksekusi aplikasi

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

- Membuat _routing_

  Routing pertama pada alamat ``/`` dengan nama fungsi ``index`` sebagai controller yang menghasilkan nilai *return* berupa tipe data string dalam bentuk kode HTML yang diapit dengan tanda petik tiga. Penggunaan tanda petik tiga mempermudah penulisan nilai *return* berupa string jika diharuskan berganti baris.

      @aplikasi.route('/')
      def index():
          return '''
          <h1>Tutorial Flask</h1>
          <p>Selamat datang di tutorial aplikasi web menggunakan Flask</p>

          <a href='/layanan'>Layanan</a> | <a href='/kontak'>Kontak</a>
          '''

    Routing kedua pada alamat ``layanan`` dengan nama fungsi ``services`` sebagai controller juga memberikan nilai *return* berupa string dalam bentuk kode HTML yang diapit tanda petik tiga.

      @aplikasi.route('/layanan')
      def services():
          return '''
          <h1>Layanan</h1>
          <h3>Ini halaman Layanan</h3>
          <a href='/'>Kembali</a>
          '''

    Routing ketiga pada alamat ``kontak`` dengan nama fungsi ``contact`` sebagai controller juga memberikan nilai *return* berupa string dalam bentuk kode HTML namun diapit tanda petik satu. Terlihat perbedaan jika hanya menggunakan tanda petik satu (ataupun petik dua), nilai *return* berupa string harus dalam satu baris.

      @aplikasi.route('/kontak')
      def contact():
          return '<h1>Kontak</h1> <h3>Ini halaman Kontak</h3><a href="/">Kembali</a>'

- Memanggil variabel ``aplikasi`` dalam struktur modul utama *library* Flask agar dapat dieksekusi ketika aplikasi dijalankan. Menambahkan parameter ``debug=True`` agar memudahkan saat melakukan pembangunan aplikasi pada mode *development*. Sekaligus menambahkan parameter ``port=9000`` agar aplikasi dapat diakses menggunakan port secara *customize*.

      if __name__ == '__main__':
          aplikasi.run(debug=True, port=9000)

- Jalankan aplikasi. Dengan mengaktifkan mode *debug*, eksekusi aplikasi Flask akan otomatis di-*restart* jika ada perubahan pada kodenya tanpa harus Ctrl+C dan menjalankan ulang.

      (venv) > python app.py
       * Serving Flask app 'app'
       * Debug mode: on
      WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
       * Running on http://127.0.0.1:9000
      Press CTRL+C to quit
       * Restarting with stat
       * Debugger is active!
       * Debugger PIN: 943-076-614

- Akses alamat ``http://127.0.0.1:9000`` melalui browser
