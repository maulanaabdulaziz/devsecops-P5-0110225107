# Tabungan Impian

Aplikasi CLI sederhana untuk mencatat tabungan, menetapkan target impian, dan melihat persentase progres serta sisa uang yang perlu dikumpulkan.

## Teknologi
- Python 3.12
- Python standard library (JSON untuk penyimpanan lokal)
- `unittest` untuk pengujian otomatis
- Bandit sebagai Static Application Security Testing (SAST)

## Fitur
- Menetapkan nama impian dan target tabungan.
- Menambahkan setoran dengan validasi nominal positif.
- Menyimpan saldo dan target ke `data_tabungan.json`.
- Melihat progres dan kekurangan tabungan.

## Cara menjalankan
1. Pastikan Python 3.10+ sudah terpasang.
2. Clone repository lalu masuk ke folder proyek.
3. Jalankan `python main.py`.
4. Pilih menu 1–4 sesuai instruksi di terminal.

## Menjalankan test dan SAST secara lokal
```bash
python -m unittest discover -s tests -v
python -m pip install bandit
bandit -r . -x ./tests -ll -ii
```

## Overview pipeline DevSecOps
Workflow `.github/workflows/devsecops.yml` berjalan saat ada `push` ke branch `main` dan `pull_request` yang menargetkan `main`. Job `build` mengompilasi source Python dan menjalankan unit test. Job `sast-scan` baru berjalan setelah `build` berhasil (`needs: build`), lalu menjalankan Bandit. Perintah Bandit memakai `-ll -ii`, sehingga temuan minimal tingkat severity Low dan confidence Low dapat membuat job gagal; ini menjadi Quality Gate keamanan. Periksa tab **Actions** untuk hasil aktual.
