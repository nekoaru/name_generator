"""
Основной модуль для генерации имён.
Использует модули datetime для генерации имени файла
"""
import datetime
import random
import shutil
import sys

from configuration import FIRST_NAMES_TEMPLATE_PATH, LAST_NAMES_TEMPLATE_PATH, NUMBER_OF_NAMES, OUTPUT_DIRECTORY


def load(file: str):
    """
    Реализует чтение файла и загрузку в список
    :param file: путь до файла
    :return: список записей в файле
    """
    try:
        with open(file, 'r') as readable_file:
            loaded_lines = readable_file.read().strip().split('\n')
            loaded_lines = [line.title() for line in loaded_lines]
            return loaded_lines
    except IOError as e:
        print(f'{e} Error opening {file}. Immediate termination of the program.', file=sys.stderr)


if __name__ == '__main__':

    dt = datetime.datetime.now().strftime("_%d_%m_%Y_%H_%M_%S")
    new_file_name = 'NG' + dt + '.txt'
    names = []

    for i in range(NUMBER_OF_NAMES):
        firstName = random.choice(load(LAST_NAMES_TEMPLATE_PATH))
        lastName = random.choice(load(FIRST_NAMES_TEMPLATE_PATH))

        names.append(f'The {firstName} {lastName}\n')

    names.sort()

    with open(new_file_name, 'w') as new_file:
        for name in names:
            new_file.write(name)

    shutil.move(new_file_name, OUTPUT_DIRECTORY)
