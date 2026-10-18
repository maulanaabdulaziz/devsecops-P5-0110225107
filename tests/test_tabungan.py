import unittest
from tabungan import TabunganImpian
from validasi import baca_nominal
from laporan import format_ringkasan

class TestTabunganImpian(unittest.TestCase):
    def test_tambah_tabungan(self):
        app = TabunganImpian({"target": 100000, "saldo": 20000})
        self.assertEqual(app.tambah_tabungan(5000), 25000)

    def test_nominal_tidak_valid_ditolak(self):
        app = TabunganImpian()
        with self.assertRaises(ValueError):
            app.tambah_tabungan(-10)

    def test_persentase_dibatasi_100(self):
        app = TabunganImpian({"target": 100, "saldo": 150})
        self.assertEqual(app.persentase, 100)

    def test_validasi_input(self):
        self.assertEqual(baca_nominal("25000"), 25000)
        self.assertIsNone(baca_nominal("-1"))
        self.assertIsNone(baca_nominal("abc"))

    def test_ringkasan_memuat_nama_impian(self):
        app = TabunganImpian({"nama_impian": "Laptop", "target": 1000000, "saldo": 100000})
        self.assertIn("Laptop", format_ringkasan(app))

if __name__ == "__main__":
    unittest.main()
