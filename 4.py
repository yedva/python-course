"""
Создать (не программно) текстовый файл со следующим содержимым:

One — 1

Two — 2

Three — 3

Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

from google_trans_new import google_translator
translator = google_translator()

with open('4.txt', 'r') as f:
    translated_lines = []
    for line in f:
        if line[:2].isalpha():  # если есть слово, то переводим
            line = translator.translate(line, lang_tgt='ru')
        translated_lines.append(line)


new_file = open('4_new.txt', 'w')
new_file.writelines(translated_lines)
new_file.close()
