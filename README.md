## Запуск

```
mkdir app
cd app
virtualenv venv
source venv/bin/activate
git clone https://github.com/KozlovDmitry/testTask
pip install -r requirements.txt
```

## Пример использования

```
python main.py test_data/test_2.xml
```

## Описание

Реализован класс Flatten, в нем объеденен функционал двух Ваших задач.
В данном классе реализованы два основных метода(с рекурсией(flatten_recursive) и без(flatten_used_queue)), которые принимают на вход объект, делают его "плоским" и возвращают максимальныю глубину.
Так же расширен функционла, чтоб вложенность поддерживала не только dict но и list

## Примеры использования

```
d = {
   "a": 5,
   "b": 6,
   "c": {
       "f": 9,
       "g": {
           "m": 17,
           "n": 3
       }
   }
}

inst = Flatten()

inst.flatten_recursive(d)
inst.result_dict              // {'a': 5, 'b': 6, 'c.f': 9, 'c.g.m': 17, 'c.g.n': 3}
inst.max_depth                // 2
```

> Так же добавлен декоратор speed_test, который выводит в консоль время вылонения(по идее, на больших объектах должно быть заметно отстование рекурсивного подхода... я не тестировал). И некоторые данные для тестовых запусков, которые находятся в test_data
