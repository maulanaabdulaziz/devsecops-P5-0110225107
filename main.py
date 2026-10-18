"""Entry point aplikasi Tabungan Impian (CLI)."""
from tabungan import TabunganImpian
from penyimpanan import simpan_data, muat_data
from laporan import format_ringkasan
from validasi import baca_nominal

DATA_FILE = "data_tabungan.json"

def main():
    data = muat_data(DATA_FILE)
    app = TabunganImpian(data)
    while True:
        print("\n=== TABUNGAN IMPIAN ===")
        print("1. Lihat ringkasan\n2. Tambah tabungan\n3. Buat/edit impian\n4. Keluar")
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            print(format_ringkasan(app))
        elif pilihan == "2":
            nominal = baca_nominal(input("Nominal yang ditabung (Rp): "))
            if nominal is None:
                print("Nominal harus berupa angka positif.")
                continue
            app.tambah_tabungan(nominal)
            simpan_data(DATA_FILE, app.to_dict())
            print("Tabungan berhasil dicatat.")
        elif pilihan == "3":
            nama = input("Nama impian: ").strip()
            target = baca_nominal(input("Target tabungan (Rp): "))
            if not nama or target is None:
                print("Nama impian wajib diisi dan target harus positif.")
                continue
            app.set_impian(nama, target)
            simpan_data(DATA_FILE, app.to_dict())
            print("Impian berhasil disimpan.")
        elif pilihan == "4":
            print("Semangat mewujudkan impian!")
            break
        else:
            print("Pilihan tidak dikenal.")

if __name__ == "__main__":
    main()
