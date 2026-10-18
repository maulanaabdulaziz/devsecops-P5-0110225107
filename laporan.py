"""Pembuatan teks ringkasan tabungan."""
def rupiah(nilai):
    return "Rp" + f"{nilai:,}".replace(",", ".")

def format_ringkasan(app):
    return (
        f"Impian: {app.nama_impian}\n"
        f"Saldo: {rupiah(app.saldo)}\n"
        f"Target: {rupiah(app.target)}\n"
        f"Progres: {app.persentase:.1f}%\n"
        f"Kekurangan: {rupiah(app.kekurangan)}"
    )
