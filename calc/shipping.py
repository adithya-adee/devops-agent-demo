PER_KG = 5


def marble(weight_kg):
    if weight_kg <= 0:
        return 0
    return weight_kg * PER_KG
