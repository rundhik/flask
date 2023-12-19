### pustaka-pustaka ###
from flask import Flask

### inisiasi pustaka ###
aplikasi = Flask(__name__)

### routing / controller ###
@aplikasi.route('/')
def index():
    return '''
    <h1>Tutorial Flask</h1>
    <p>Selamat datang di tutorial aplikasi web menggunakan Flask</p>

    <a href='/layanan'>Layanan</a> | <a href='/kontak'>Kontak</a>
    '''

@aplikasi.route('/layanan')
def services():
    return '''
    <h1>Layanan</h1>
    <h3>Ini halaman Layanan</h3>
    <a href='/'>Kembali</a>
    '''

@aplikasi.route('/kontak')
def contact():
    return '<h1>Kontak</h1> <h3>Ini halaman Kontak</h3><a href="/">Kembali</a>'


### eksekusi aplikasi ###
if __name__ == '__main__':
    aplikasi.run(debug=True, port=9000)
