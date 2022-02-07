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
    for files in Path('./').glob('*.py'):
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

# 2. Create a script that should find the line that you provided to it in the provided directory.


# import glob  # шлях до директорії
# import time
# import psutil
# from concurrent.futures import ThreadPoolExecutor
#
# core_num = psutil.cpu_count()
#
#
# def find_by_pattern(filename, pattern):
#     container = []
#     with open(filename) as file:
#         for line in file:
#             if pattern in line:
#                 container.append(line)
#     return container
#
#
# def find_all_files(directory_path, pattern):
#     files = glob.glob(f'{directory_path}/*.py')
#     container = []
#     with ThreadPoolExecutor(core_num - 1) as executor:
#         result = list(executor.map(find_by_pattern, files, pattern))
#         container.append(result)
#     return container
#
#
# if __name__ == '__main__':
#     start = time.time()
#     first = find_all_files('.', pattern=['ThreadPoolExecutor'])
#     second = find_all_files('.', pattern=['ProcessPoolExecutor'])
#     third = find_all_files('.', pattern=['get_session'])
#     fourth = find_all_files('.', pattern=['result.text'])
#     fifth = find_all_files('../threads_processes', pattern=['ThreadPoolExecutor'])
#     sixth = find_all_files('../threads_processes', pattern=['ProcessPoolExecutor'])
#     seventh = find_all_files('../threads_processes', pattern=['get_session'])
#     eighth = find_all_files('../threads_processes', pattern=['result.text'])
#     print(f'Total time for search: {time.time() - start}')
#     all_search = [first, second, third, fourth, fifth, sixth, seventh, eighth]
#
#     for search in all_search:
#         for element in search:
#             print(element)
