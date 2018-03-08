def levenshtein_distance(source, target):
    tmp_source = ' ' + source
    tmp_target = ' ' + target

    distance_matrix = [[None] * len(tmp_source) for _ in range(len(tmp_target))]
    distance_matrix[0] = [i for i in range(len(tmp_source))]

    for i in range(len(tmp_target)):
        distance_matrix[i][0] = i

    for i in range(1, len(tmp_target)):
        for j in range(1, len(tmp_source)):
            substitution_cost = 0 if tmp_target[i] == tmp_source[j] else 1
            distance_matrix[i][j] = min(distance_matrix[i-1][j] + 1,
                                        distance_matrix[i][j-1] + 1,
                                        distance_matrix[i-1][j-1] + substitution_cost)

    ratio = (len(source) + len(target) - distance_matrix[-1][-1]) / float(len(source) + len(target))

    levenshtein_distance.ratio = ratio
    levenshtein_distance.distance_matrix = distance_matrix

    return distance_matrix[-1][-1]
