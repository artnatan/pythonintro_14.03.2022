
# 1) У вас есть строка my_string = '0123456789'.
# Сгенерировать целые числа (тип int) от 0 до 99 и распечатать их.
# Задание нужно выполнить ТОЛЬКО через цикл в цикле(См. пример выше) и приведение типов.
# Генерирование через range или другие "фишки" я засчитывать не буду ))
#
# my_string = '0123456789'
# for symbol_1 in my_string:
# 	for symbol_2 in my_string:
# 		print(int(symbol_1+symbol_2))


my_str = "My name is Vova. I am a teacher !"



for symbol in my_str:

	if symbol.isupper() and symbol not in 'EYUIOA':

		print(symbol)