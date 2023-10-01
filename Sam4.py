sentence1 = input("Введите предложение на английском: ")
print("Длина введенного предложения: ", len(sentence1))
sentence2 = sentence1.lower()
print("Ваше предложение в нижнем регистре: ", sentence2)
print("Кол-во гласных в введенном предложении: ", sentence2.count('a') + sentence2.count('e') + sentence2.count('i') + sentence2.count('o') + sentence2.count('u'))
sentence3 = sentence2.replace('ugly', 'beauty')
print("Измененое предложение: ", sentence3)

if sentence3.startswith('the') == True:
    print("Предложение начинается с The")
else: print("Предложение не начинается с The")

if sentence3.endswith('end') == True:
    print("Предложение заканчивается на End")
else: print("Предложение не заканчивается на End")
