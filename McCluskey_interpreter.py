"""
Program interpretujący zminimalizowane funkcje boolowskie wyznaczone metodą Quine'a McCluskey'a
Zawiera analizę leksykalną, parsowanie i kompilowanie formuł logicznych w postaci sumy iloczynów zmiennych,
które reprezentują kolejne bity liczby zapisanej binarnie np. !ab + cd : (not a and b) or (c and d)
oraz oblicza wartości danej formuły logicznej dla podanych liczb w systemie dziesiętnym.
Poza tym dla wartości 1 wyświetla wszystkie składowe koniunkcje o wartości 1
"""
def signs_negations(words): # tworzenie tokenów (z negacjami)
    signs_negations = []
    words_negations = []
    was_negated = 0
    for word in words:
        for sign in word:
            if sign == '!':
                if was_negated == 1:
                    was_negated = 0
                else:
                    was_negated = 1
            else:
                signs_negations.append([sign, int(was_negated)])
                if was_negated == 1:
                    was_negated = 0
        words_negations.append(signs_negations)
        signs_negations = []
    return words_negations

def variables_dict(binary): # słownik zmiennych na bity
    dict={}
    for i in range(len(binary)):
        if binary[i] == "0":
            dict[chr(int(i)+97)] = 0
        else:
            dict[chr(int(i)+97)] = 1
    return dict

def get_bits(logic_method): # ilość bitów zmiennych w zdaniu (na podstawie ilości zmiennych)
    bits = ord(max(logic_method)) - 96
    return bits

def get_binary(number, bits): #binarna forma danych
    return((bits * '0' + format(number, 'b'))[-bits:])

def compile_sentence(logic_method): # kompilowanie zdania
    logic_method = "".join(logic_method.split())
    words = logic_method.split('+') # dzielenie na alternatywy
    words_strings = words
    words = signs_negations(words) # negacje
    def compiled_method(number): # obliczanie wartości logicznej danego zdania
        dict = variables_dict(get_binary( number, get_bits(logic_method) ) )
        # wartości koniunkcji
        words_values=[]
        crucial_words=[]
        for word in words:
            value=1
            for sign in word:
                if sign[1] == 1:
                    if dict[sign[0]] == 1:
                        value*=0
                    else:
                        value*=1
                else:
                    if dict[sign[0]] == 1:
                        value*=1
                    else:
                        value*=0
            words_values.append(value)
        # wartości alternatyw
        values_sum=0
        for i in range(len(words_values)):
            values_sum+=words_values[i]
            if words_values[i] == 1:
                crucial_words.append(words_strings[i])
        if values_sum > 0:
            return (1, crucial_words)
        else:
            return 0
    return compiled_method
# sprawdzanie na poprawnych danych (zdanie i liczby dla których jego wartość logiczna powinna wynosić 1)
valid_values = [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 19, 21, 22, 23, 31]
sentence = '!a!b + !abc + a!bde + cde + !bcd + !bce + !a!ce + !abd!e'
check_sentence = compile_sentence(sentence) # kompilowanie podanego zdania

for x in range(32): # wypisanie porównania otrzymanych wyników z poprawnymi wynikami
    if x in valid_values:
        print(1, end=" ")
    else:
        print(0, end=" ")
    print(check_sentence(x))