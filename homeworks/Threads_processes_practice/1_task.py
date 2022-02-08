# 1. Create a script that should find the lines by provided pattern in the
# provided path directory with recursion* and threads


import os.path
import time
import psutil
from pathlib import Path
core_num = psutil.cpu_count()


def find_by_pattern(filename, pattern):
    container = []
    with open(filename) as file:
        for line in file:
            if pattern in line:
                container.append(line)
    return container


def find_all_files(pattern):
    place_list = []
    for files in Path('./').rglob('*.py'):
        info_place = os.path.abspath(files)
        place_list.append(info_place)
    container = []
    for file in place_list:
        result = find_by_pattern(file, pattern)
        container.append(result)
    return container


if __name__ == '__main__':
    start = time.time()
    first = find_all_files(pattern='ThreadPoolExecutor')
    second = find_all_files(pattern='ProcessPoolExecutor')
    third = find_all_files(pattern='get_session')
    fourth = find_all_files(pattern='result.text')

    print(f'Total time for search: {time.time() - start}')
    all_search = [first, second, third, fourth]

    for search in all_search:
        for element in search:
            print(element)