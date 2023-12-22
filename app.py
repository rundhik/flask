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
    '''

### dynamic routing dengan satu parameter ###
@aplikasi.route('/<halaman>')
def page(halaman):
    return '''
    <h1>Ini halaman {}</h1>
    <a href='/'>Kembali</a>
    '''.format(halaman)

### dynamic routing dengan lebih dari satu parameter ###
@aplikasi.route('/<name>/<nickname>')
def user(name, nickname):
    return '''
    <h1>Halo {},</h1>
    <h3>Selamat Datang {} di Tutorial Flask</h3>
    <a href='/'>Kembali</a>
    '''.format(nickname, name.title())

### dynamic routing dengan prefiks dan menggunakan satu parameter ###
@aplikasi.route('/layanan/<layanan>')
def services(layanan):
    return '<h1>'+ layanan.capitalize() +'</h1>' + '<h3>Ini halaman ' + layanan + '</h3> <a href="/">Kembali</a>'

@aplikasi.route('/produk/<produk>')
def product(produk):
    return '''<h1>Produk : {}</h1>'''.format(produk.capitalize()) + \
    '''<h3>Menampilkan produk ''' + produk.capitalize() + \
    '''</h3> <a href="/">Kembali</a>'''

### dynamic routing dengan prefiks dan menggunakan lebih dari satu parameter sekaligus memberikan nilai default pada parameter ###
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

### eksekusi aplikasi ###
if __name__ == '__main__':
    aplikasi.run(debug=True, port=9000)
