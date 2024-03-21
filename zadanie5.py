# Zadanie 5a: Najdłuższy wyraz w tekście
def f5a(text):
    """
    Funkcja znajduje najdłuższy wyraz w tekście.
    """
    longest_word = max(text.split(), key=len)
    return longest_word

# Zadanie 5b: Podział tekstu na fragmenty
def chunks(line, n):
    """
    Funkcja dzieli tekst na fragmenty o długości n.
    """
    return [line[i:i+n] for i in range(0, len(line), n)]

# Zadanie 5c: Odtwarzanie polecenia hexdump
def hexdump(line):
    """
    Funkcja odtwarza polecenie hexdump dla danego tekstu.
    """
    for i in range(0, len(line), 16):
        chunk = line[i:i+16]
        hex_chunk = ' '.join([hex(ord(char))[2:].zfill(2) for char in chunk])
        text_chunk = ''.join([char if 32 <= ord(char) <= 126 else '.' for char in chunk])
        print(f"{i:08x} {hex_chunk.ljust(47)} |{text_chunk}|")
    print()

# Zadanie 5d: Rysowanie linijki
def ruler(tics, mtics):
    """
    Funkcja rysuje linijkę z podziałkami.
    """
    scale = '.' * mtics
    tick_marks = [scale if i % mtics == 0 else ' ' for i in range(tics)]
    ruler_line = '|'.join(tick_marks)
    indices_line = '0' + ' ' * (mtics - 1) + ''.join([str(i).rjust(mtics) for i in range(1, tics)])
    print(indices_line)
    print(f"|{ruler_line}|")

# Zadanie 5e: Suma sekwencji
def seqsum(data):
    """
    Funkcja zwraca listę sum liczb w sekwencjach.
    """
    return [sum(seq) for seq in data]

# Zadanie 5f: Elementy wspólne dwóch list
def common_items(list1, list2):
    """
    Funkcja zwraca listę elementów wspólnych dwóch list bez powtórzeń.
    """
    return list(set(list1) & set(list2))

# Testowanie funkcji
sample_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
print("Najdłuższy wyraz:", f5a(sample_text))
print("Podziały tekstu:", chunks(sample_text, 5))
hexdump(sample_text)
ruler(16, 3)
sample_data = [[6], [], (6,1,4), [6, 0, -5]]
print("Sumy sekwencji:", seqsum(sample_data))
print("Elementy wspólne:", common_items([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]))

