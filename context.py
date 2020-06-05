import datetime

class MyContext:

    def __enter__(self):
        self.start = datetime.datetime.now()
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop = datetime.datetime.now()
        self.time = self.stop - self.start
        print(f'Было потрачено времени на выполнение кода {self.time}')


with MyContext() as my_context:
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}
    result = []
    for items in ids.values():
        for i in items:
            result.append(i)
    print(list(set(result)))





