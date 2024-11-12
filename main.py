"""Imports"""

import csv
from dsmltf import scale, squared_errors
import matplotlib.pyplot as plt


def make_data() -> list:
    """
    make data:D
    """
    # Парсим данные
    with open("anime_filtered.csv", "r+", encoding="UTF-8") as f:
        data = []
        a = {
            "OVA": 0,
            "Movie": 1,
            "TV": 2,
            "Unknown": 3,
            "Music": 4,
            "Special": 5,
            "ONA": 6,
        }
        b = {
            "Picture book": 0,
            "4-koma manga": 1,
            "Visual novel": 2,
            "Unknown": 3,
            "Original": 4,
            "Radio": 5,
            "Music": 6,
            "Web manga": 7,
            "Digital manga": 8,
            "Novel": 9,
            "Other": 10,
            "Card game": 11,
            "Light novel": 12,
            "Game": 13,
            "Book": 14,
            "Manga": 15,
        }
        for i in csv.reader(f):
            data.append(i[6:9] + i[15:16])
        for i in range(1, len(data)):
            data[i][0] = a[data[i][0]]
            data[i][1] = b[data[i][1]]
            data[i][2] = float(data[i][2])
            data[i][3] = float(data[i][3])
    return data[1:]


def main() -> None:
    """main function"""
    # Получим датасет
    data_set = make_data()
    scale_data = scale(data_set)  # Прошкалируем
    y, x = [], []
    for k in range(1, 10):
        y.append(squared_errors(inps=scale_data, k=k))
        x.append(k)
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label="Исходные данные", marker="o")
    plt.xlabel("Время")
    plt.ylabel("Значение")
    plt.title("Аппроксимация полиномом")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
