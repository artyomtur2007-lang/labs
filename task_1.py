text = input("Введите текст: ")

words = text.split()

word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print("Словарь с количеством слов:", word_counts)

unique_word_count = len(word_counts)

print("Количество уникальных слов:", unique_word_count)
