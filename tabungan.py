"""Logika bisnis untuk target dan saldo tabungan."""
class TabunganImpian:
    def __init__(self, data=None):
        data = data or {}
        self.nama_impian = data.get("nama_impian", "Liburan")
        self.target = int(data.get("target", 1_000_000))
        self.saldo = int(data.get("saldo", 0))
        if self.target < 1 or self.saldo < 0:
            raise ValueError("Target harus positif dan saldo tidak boleh negatif.")

    def tambah_tabungan(self, nominal):
        if not isinstance(nominal, int) or isinstance(nominal, bool) or nominal <= 0:
            raise ValueError("Nominal harus berupa integer positif.")
        self.saldo += nominal
        return self.saldo

    def set_impian(self, nama, target):
        nama = nama.strip()
        if not nama or not isinstance(target, int) or isinstance(target, bool) or target <= 0:
            raise ValueError("Nama dan target impian harus valid.")
        self.nama_impian, self.target = nama, target

    @property
    def persentase(self):
        return min(100.0, self.saldo / self.target * 100)

    @property
    def kekurangan(self):
        return max(0, self.target - self.saldo)

    def to_dict(self):
        return {"nama_impian": self.nama_impian, "target": self.target, "saldo": self.saldo}
