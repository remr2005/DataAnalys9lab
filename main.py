"""Imports"""

import csv
from dsmltf import scale, KMeans, bottom_up_cluster, generate_clusters, get_values

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
            data[i][2] = int(data[i][2])
            data[i][3] = float(data[i][3])
    return data[1:]


def main() -> None:
    """main function"""
    # Получим датасет
    data_set = make_data()
    scale_data = scale(data_set[:100])  # Прошкалируем
    clast = KMeans(8) # Устанавливаем число кластеров
    clast.train(scale_data) # Тренируем?
    print(clast.means)
    # восходящая кластеризация
    base_claster = bottom_up_cluster(scale_data)
    print([get_values(cluster) for cluster in generate_clusters(base_claster, 8)])
    # возможно стоит впихнуть сюда графики 


if __name__ == "__main__":
    main()

"""
Так как в этой лабе куча ошибок в самой dsmltf то держите то, что нужно исправить ручками
def bottom_up_cluster(inps, distance_agg=min):
    clusters = [(inp,) for inp in inps]
    while len(clusters) > 1:
        c1, c2 = min([(cluster1, cluster2)
                      for i, cluster1 in enumerate(clusters)
                      for cluster2 in clusters[:i]],
                     key=lambda x: cluster_distance( *x, distance_agg))
        clusters = [c for c in clusters if c != c1 and c != c2]
        merged_cluster = (len(clusters), [c1, c2])
        clusters.append(merged_cluster)
    return clusters[0]

def get_values(cluster):
    if is_leaf(cluster):
        return [cluster[0]]
    else:
        return [val for child in get_children(cluster) for val in get_values(child)]

def cluster_distance(cluster1, cluster2, distance_agg=min):
    values1 = list(get_values(cluster1))
    values2 = list(get_values(cluster2))
    return distance_agg([distance(list(inp1), list(inp2)) for inp1 in values1 for inp2 in values2])
"""