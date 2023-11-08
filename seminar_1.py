import subprocess
import re

"""
Задание 1.
Условие:
Написать функцию на Python, которой передаются в качестве параметров команда 
и текст. Функция должна возвращать True, если команда успешно выполнена и 
текст найден в её выводе и False в противном случае. Передаваться должна
 только одна строка, разбиение вывода использовать не нужно.
"""
"""
if __name__ == '__main__':
    def my_func(command, text):
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE,
                                encoding='utf-8')
        out = result.stdout
        if result.returncode == 0 and text in out:
            return True
        else:
            return False


    print(my_func("cat /etc/os-release", "jammy"))
"""
""""
Задание 2. (повышенной сложности)
Доработать функцию из предыдущего задания таким образом, чтобы у неё появился
дополнительный режим работы, в котором вывод разбивается на слова с удалением
всех знаков пунктуации (их можно взять из списка string.punctuation
модуля string). В этом режиме должно проверяться наличие слова в выводе.
"""
if __name__ == '__main__':
    def my_func(command, text):
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE,
                                encoding='utf-8')
        out = re.split('\W+', result.stdout)
        if result.returncode == 0 and text in out:
            print(out)
            return True
        else:
            return False


    print(my_func("cat /etc/os-release", "jammy"))
