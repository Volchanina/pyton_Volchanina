messages = "Не знаю, как там в Лондоне, я не была.\
Может, там собака — друг человека.\
А у нас управдом — друг человека!"
print(messages)
print("\n")
print("Шаг 1.  Посчитать количество символов")
length = len(messages)
print("Количество символов:", length)
print("\n")
print( "Шаг 2.Развернуть строку. Python yes -> sey nohtyP" )
print("Python yes ->" + "Python yes "[::-1])
print("\n")
print("Шаг3. Сделать каждое слово с большой буквы")
print(messages.title())
print("\n")
print("Шаг4. Сделать весь текст прописными буквами")
print(messages.upper())
print("\n")
print("Шаг5. Найти число вхождений 'нд', 'ам', 'о' в строку")
submessages = "нд"
count=messages.count(submessages)
print("Всего вхождений'нд':",count)
submessages = "ом"
count=messages.count(submessages)
print("Всего вхождений'ом':",count)
submessages = "о"
count=messages.count(submessages)
print("Всего вхождений'о':",count)
print("\n")
print("Шаг7.Собственные упражнения")
print("\t7.1  Вывести предложение 3 раза" ) 
submessages=messages*3
print(submessages)
print("\n")
print("\t7.2 Вывести по индексу 5,-3, с 3 по 8" ) 
print(messages[5])
print(messages[-3])
print(messages[3:8])
print("\t7.3 Составить из имеющегося предложения, следующее:\
 Не знаю, что в Лондоне, а у нас управдом - друг человека!" ) 
new_mesages=messages[:9]+"что "+messages[17:28] + (messages[-33:].lower())
print(new_mesages)
print("\n")
print("\t7.4 Создать шаблон для приглашения на семинар по проектированию:")
name = input()
data = input()
print(f'Добрый день, уважаемый,\t {name}\t, приглашаем Вас\n\
принять участие в международном семинаре по проектированию\n\
железобетонных конструкций, который пройдет {data} \
в городе Минске....')
print("\n")
print("\t7.5 Создать список")
list="мама, папа, леля, катя, юлий, ириска"
splitted=list.split(',')
print(splitted)
print("Шаг8. Развернуть предложение. Я Денис -> Денис Я")
s = "Я Денис"
memos = s.find(" ")
a=s[:int(memos)]
b=s[int(memos):]
print(b+" "+a)
print("Шаг8.Второй способ")
print(s[2:7]+" "+s[0])
print("hi")


