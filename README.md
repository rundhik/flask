# Tutorial Flask

## Pra Syarat
Kebutuhan minimal aplikasi :
- Python 3.10.+
- Pip 22.+

### Windows
- Install Python (dalam kasus ini pada drive `D:\Python`) dan tambahkan *PYTHONPATH* pada *Environment Variables* Windows. Jika melalui *command line* dapat menjalankan *script* berikut

        set PYTHONPATH=D:\Python;D:\Python\Scripts;

    Tambahkan direktori `D:\Python\Scripts` pada *Environment Variables*  *PATH*. Buka terminal dan ketik perintah Python atau pip untuk mengecek apakah *command* Python dan pip sudah dikenali oleh Windows. Pada kondisi tertentu, menjalankan perintah pip untuk instalasi **harus sebagai Administrator**, alangkah baiknya jika membuka *CMD* dan pilih *Run as Administrator*.

        > python -V
        Python 3.10.4
        > pip -V
        pip 23.1.1 from D:\Python\lib\site-packages\pip (Python 3.10)

- Lakukan upgrade pip terlebih dahulu untuk memudahkan pembaharuan pustaka-pustaka yang dibutuhkan di kemudian hari.

        > Python -m pip install --upgrade pip

- Pasang package `virtualenv`

        > Python -m pip install virtualenv

- Jika sudah masuk ke dalam folder proyek, buat virtual environment Python terlebih dahulu.

        > Python -m virtualenv venv

- Lakukan aktivasi pada environment yang baru saja dibuat.

        > venv\Scripts\activate
        (venv) >

    Cek apakah sudah masuk pada environment yang benar agar tidak terjadi bentrok dengan environment Python yang lain.

        (venv) > python -V
        (venv) > pip -V
        (venv) > pip list

- Selanjutnya pasang pustaka-pustaka paket yang dibutuhkan menggunakan pip.
