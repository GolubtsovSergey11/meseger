import datetime

class MyFile:

    def __init__(self, riddle):
        self.riddle = riddle

    def __enter__(self):
        print('Отгадайте загадку! \n')
        self.the_riddle = open(self.riddle, 'r', encoding='UTF-8')
        for item in self.the_riddle:
            print(item.strip())
        return self

    def _answer_riddle_(self):
        #print('Отгадайте загадку!')
        i = 0
        self.start = datetime.datetime.now()
        while True:
            self.answer = input('Введите ответ: ').capitalize()
            i += 1
            if self.answer == 'Зонтик' or self.answer == 'Зонт':
                self.stop = datetime.datetime.now()
                if i > 1:
                    print(f'Правильно, вы отгадали загадку с {i} попыток. Ваше время {self.stop - self.start}')
                else:
                    print(f'Правильно, вы отгадали загадку с {i} попытки. Ваше время {self.stop - self.start}')
                break
            else:
                print('Не правильно, попробуй еще раз.')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.the_riddle.close()


with MyFile('riddle.txt') as file:
    file._answer_riddle_()

