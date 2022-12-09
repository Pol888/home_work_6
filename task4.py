#Напишите программу, удаляющую из текста все СЛОВА, содержащие ""абв"".
start = 'Привет забвение пошли на зимбабве пошалим незабвенно.'

listik = ' '.join(list(filter(lambda x: 'абв' not in x, [i for i in start.split()])))
print(listik)