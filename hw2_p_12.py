# Задача №12 Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

from math import sqrt
#s, p = map( int, input('s, p = ').split() )

s = int(input('Введите сумму двух чисел: '))
p = int(input('Введите произведение двух чисел: '))

z = sqrt((s/2)**2 - p)
print('Вы загадали ', int(s/2 - z), 'и', int(s/2 + z))
