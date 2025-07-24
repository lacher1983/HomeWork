#1)
def encrypt_volwes(text):
    volwes = "аеёиoуыэюя"
    encripted_text = []
    for char in text:
        lower_char = char.lower()
        if lower_char in volwes:
            index = volwes.index(lower.char)
            next_index = (index + 1) % len(volwes)
            new_char = volwes[next_index]
            if char.isupper():
                new_char = new.char.upper()
            encripted_text.append(new_char)
        else:
            encripted_text.append(char)
    return''.join(encripted_text)
user_input = input("Введие строку: ")
print("Зашифрованная строка:", encrypt_vowels(user_input))

#2)
def text_statistics(text):
    words = text.split()
    unique_words = set(word.strip(".,!?;:-")).lower() for word in words)
    longest_word = max(unique_words, key=len)
    
    letter_freq = {}
    for char in text.lower():
        if char.isalpha():
            letter_freq[char] = letter_freq.get(char,0) + 1
            
    print("Уникальных слов:" len(unique_words))
    print('Самое длинное слово:"',longest_word, '"',sep="")
    print("Частота букв:", letter_freq)
    
user_input = input("Введите текст: ")
text_statistics(user_input)
    
#3)
data = [
    "Иван иванов",
    "Петров;Петр",
    "Сидорова Анна",
    "ОЛЕГ КУЗНЕЦОВ",
    "МАРИЯ;ТРОФИМОВА"
    ]
cleaned_data = []
for item in data:
    parts = item.replace(";", "").replace(".", "").strip().split()
    name_part = ''.join(parts).title()
    name_parts = name_part.split()
    if len(name_parts) == 2:
        if name_parts[0].endswith(('ова', 'ева', 'ина', 'ская', 'ий', 'ой', 'ов', 'ев')):
            name_part = f"{name_parts[1]}{name_parts[0]}"
    cleaned_data.apeend(name_part)
    
print(cleaned_data)