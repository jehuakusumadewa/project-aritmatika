def deret_aritmatika(N, awal=2, beda=3):
    deret = [awal + i * beda for i in range(N)]
    return deret


if __name__ == "__main__":
    N = int(input("Masukkan jumlah N: "))
    print("Output untuk N =", N, ":", deret_aritmatika(N))
