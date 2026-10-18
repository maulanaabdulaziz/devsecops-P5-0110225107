"""Validasi input nominal uang."""
def baca_nominal(teks):
    try:
        nominal = int(teks.strip())
    except (ValueError, AttributeError):
        return None
    return nominal if nominal > 0 else None
