from flask import Flask

aplikasi = Flask(__name__)

@aplikasi.route('/')
def index():
    return '''
    <h1>Tutorial Flask</h1>
    <p>Selamat datang di tutorial aplikasi web menggunakan Flask</p>
    '''

if __name__ == '__main__':
    aplikasi.run()
