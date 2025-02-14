def es_anagrama(palabra1, palabra2):
    if len(palabra1) != len(palabra2):
        return False
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

if __name__ == "__main__":
    print(es_anagrama("escuela", "cuclees"))  # True
    print(es_anagrama("python", "java"))  # False