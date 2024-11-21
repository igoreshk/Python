Узнав, что ДНК не является случайной строкой, только что поступившие в Институте 
студенты группы информатиков предложили использовать алгоритм сжатия, 
который сжимает повторяющиеся символы в строке.

Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть 
группы одинаковых символов исходной строки заменяются на этот символ и 
количество его повторений в этой позиции строки.

Напишите программу, которая считывает строку, кодирует её 
предложенным алгоритмом и выводит закодированную последовательность 
на стандартный вывод. Кодирование должно учитывать регистр символов.

# put your python code here
s = str(input())
k = len(s) - 1
c = 1
t = ''
if len(s) == 1:
    t = t + s + str(c)
else:
    for i in range(0, k):
        if s[i] == s[i + 1]:
            c += 1
        elif s[i] != s[i + 1]:
            t = t + s[i] + str(c)
            c = 1
    for j in range(k, k + 1):
        if s[-1] == s[-2]:
            t = t + s[j] + str(c)
        elif s[-1] != s[-2]:
            t = t + s[j] + str(c)
            c = 1
print(t)
