def soedinit_slovarya(slovar1, slovar2):
    for key in slovar2:
        value = slovar2[key]

        if key in slovar1:
            if isinstance(value, dict) and isinstance(slovar1[key], dict):
                soedinit_slovarya(slovar1[key], value)
            else:
                slovar1[key] = value
        else:
            slovar1[key] = value

    return slovar1


slovar_a = {"a": 1, "b": {"c": 1, "f": 4}}
slovar_b = {"d": 1, "b": {"c": 2, "e": 3}}

print("Начальный словарь A:", slovar_a)
print("Начальный словарь B:", slovar_b)

soedinit_slovarya(slovar_a, slovar_b)

print("Словарь A после обработки:", slovar_a)
