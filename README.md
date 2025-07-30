### CLI-and-tests  
Структура проекта:  
CLI-and-tests
+ test_utils.py      # Тесты для функций  
+ test.txt           # Тестовый файл (можно удалить)
+ requirements       # Требования (пустой файл)
- /Homework    
  + Copy.py            # Копирование файлов  
  + Delete.py          # Удаление файлов  
  + Count.py           # Подсчёт файлов
  + Rename.py          # Переименование файлов 
  + Manager.py         # Основной CLI-интерфейс  
  
  
### Использование:  
**Команда которая позволяет копировать файл:**  
python Manager.py copy путь_к_файлу путь_копии  
  **Пример:**  
   `<python  -m Homework.Manager copy test.txt copy_test.txt?>`  
**Команда которая удаляет файл:**  
python Manager.py delete путь_к_файлу  
  **Пример:**  
  `<python  -m Homework.Manager delete copy_test.txt>`   
**Команда подсчитывающая количество файлов в папке:**  
python Manager.py count путь_к_папке  
  **Пример:**  
  `<python  -m Homework.Manager count Homework>`   
**Команда переименовывающая файл с датой:**  
python Manager.py count путь_к_папке  
  **Пример:**  
  `<python  -m Homework.Manager rename test.txt>` 


**Запуск тестов:**  
Файл test_utils.py содержит тесты всех функций.  
**Запуск:**  
`<python test_utils.py>`   

### Автор  
Алексей Скрипкин
