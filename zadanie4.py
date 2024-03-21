
# Zadanie 4a: Operacje na listach
def f4a(text):
    """
    Funkcja przeprowadza operacje na liście zgodnie z poleceniem.
    """
    L = [3, "xyz", [10, 20]]
    length_L = len(L)
    element_1 = L[1]
    first_char_element_1 = L[1][0]
    element_2 = L[2]
    second_element_element_2 = L[2][1]
    return length_L, element_1, first_char_element_1, element_2, second_element_element_2

# Zadanie 4b: Wycinki
def f4b(text):
    """
    Funkcja wykonuje operacje na napisach zgodnie z poleceniem.
    """
    sequence = "Common Sequence Operations"
    subsequence = sequence[7:15]
    joined_subsequence = '.'.join(subsequence)
    text_last_5 = text[-5:]
    every_second_letter = text[::2]
    reversed_words = text[::-1].split()[::-1]
    return subsequence, joined_subsequence, text_last_5, every_second_letter, reversed_words

# Zadanie 4c: Konkatenacja i powtórzenia
def f4c(text, n):
    """
    Funkcja tworzy napis zawierający powtórzone ciągi znaków 'xD' oddzielone spacjami.
    """
    concatenated_text = ' '.join(['xD' for _ in range(n)])
    return concatenated_text

# Zadanie 4d: Podstawianie
def f4d(text):
    """
    Funkcja zastępuje ciąg 'Sequence' na 'Ciąg' w liście.
    """
    l = list("Mutable Sequence Types")
    replaced_list = ['Ciąg' if x == 'Sequence' else x for x in l]
    return replaced_list

# Zadanie 4e: Zapisz minimalnej długości sekwencję wyrażeń
def f4e(text):
    """
    Funkcja zapisuje minimalną długość sekwencji, która stworzy posortowaną listę wyrazów.
    """
    sorted_words = sorted(text.split(), key=len)
    return sorted_words

# Zadanie 4f: Listy składane (list comprehension)
def f4f(text):
    """
    Funkcja zamienia litery małe na duże i odwrotnie w napisie.
    """
    converted_text = ''.join([char.lower() if char.isupper() else char.upper() for char in text])
    return converted_text

# Zadanie 4g: Funkcja wc
def wc(text):
    """
    Funkcja wc zwraca tuple zawierającą liczbę znaków, słów, unikalnych słów oraz liczbę linii w tekście.
    """
    words = text.split()
    unique_words = set(words)
    lines = text.split('\n')
    return len(text), len(words), len(unique_words), len(lines)

# Zadanie 4h: Funkcja f4h
def f4h(text):
    """
    Funkcja f4h zwraca string z pierwszymi i ostatnimi literami wyrazów w tekście.
    """
    first_letters = ''.join([word[0] for word in text.split()])
    last_letters = ''.join([word[-1] for word in text.split()])
    return first_letters, last_letters

# Zadanie 4i: Funkcja f4i
def f4i(text):
    """
    Funkcja f4i zwraca łączną długość wyrazów w tekście.
    """
    total_length = sum(len(word) for word in text.split())
    return total_length

# Zadanie 4j: Funkcja f4j
def f4j(text):
    """
    Funkcja f4j zwraca łączną długość wyrazów w tekście za pomocą map.
    """
    total_length = sum(map(len, text.split()))
    return total_length

# Wygeneruj akapit lorem ipsum.
lorem_text = lorem.paragraph()

# Testowanie funkcji
print(f4a(lorem_text))
print(f4b(lorem_text))
print(f4c(lorem_text, 5))
print(f4d(lorem_text))
print(f4e(lorem_text))
print(f4f(lorem_text))
print(wc(lorem_text))
print(f4h(lorem_text))
print(f4i(lorem_text))
print(f4j(lorem_text))

