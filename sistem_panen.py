def hitung_total_hasil(data_panen):
    """Menghitung total hasil panen dalam kg."""
    return sum(data_panen)


def hitung_diskon(total, persen):
    """Menghitung nilai setelah diskon."""
    if not 0 <= persen <= 100:
        raise ValueError("Persentase diskon harus 0-100.")

    nilai_diskon = total * persen / 100
    return total - nilai_diskon


def main():
    data_panen = [120, 150, 100, 130]

    total = hitung_total_hasil(data_panen)

    print("SISTEM PENCATATAN HASIL PANEN DIGITAL")
    print("Data hasil panen:", data_panen, "kg")
    print("Total hasil panen:", total, "kg")

    harga = 500000
    persen_diskon = 10

    setelah_diskon = hitung_diskon(harga, persen_diskon)

    print("Harga awal:", harga)
    print("Diskon:", persen_diskon, "%")
    print("Harga setelah diskon:", setelah_diskon)


if __name__ == "__main__":
    main()