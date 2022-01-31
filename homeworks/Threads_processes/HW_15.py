import threading


def get_thread_count():
    return threading.active_count()


def say_info(name):
    print(f"Hello, {name}")


t1 = threading.Thread(target=say_info, args=['processing1', ])
t2 = threading.Thread(target=say_info, args=['processing2', ])


print(f"Active thread count before start: {get_thread_count()}")
t1.start()
t2.start()
print(f"Active thread before join: {get_thread_count()}")
t1.join()
t2.join()
print(f"All threads: {get_thread_count()} ")
