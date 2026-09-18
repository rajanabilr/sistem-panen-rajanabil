def hitung_total_hasil(data_panen):
    """Menghitung total hasil panen dalam kg."""
    return sum(data_panen)


def main():
    data_panen = [120, 150, 100, 130]

    total = hitung_total_hasil(data_panen)

    print("SISTEM PENCATATAN HASIL PANEN DIGITAL")
    print("Data hasil panen:", data_panen, "kg")
    print("Total hasil panen:", total, "kg")


if __name__ == "__main__":
    main()