# flask_project
Flask homework

1. Необходимо разработать REST API, предоставляющее возможность ведения блога.

2. API должен иметь минимум 2 сущности:
    - пользователь
    - пост
3. Пользователь должен иметь возможность:
    - создать
    - прочитать
    - изменить
    - удалить пост

Инструкция по запуску задания (Программа  POSTman):

   - GET метод
      URL: http://127.0.0.1:5000/twit
      Просмотреть существующие твиты.
    
   - POST метод
      URL: http://127.0.0.1:5000/twit
      Создаем  твиты, в теле прописать примеры:
              Body {"id": 1, "body": "Hello, my name user1", "author": "@user1"}
              Body {"id": 2, "body": "Hello, my name user2", "author": "@user2"}
              Body {"id": 3, "body": "Hello, my name user3", "author": "@user3"}
              Body {"id": 4, "body": "Hello, my name user4", "author": "@user4"}

      Каждый твит создается отдельно.

   - PUT метод
      URL: http://127.0.0.1:5000/twit/номер id
      Изменяем существующий твит, например:
    
              URL http://127.0.0.1:5000/twit/1
              Body {"id": 1, "body": "Hello, my name Alex", "author": "@user1"}  
         
              URL http://127.0.0.1:5000/twit/4
              Body {"id": 4, "body": "Hello, my name Vika", "author": "@user4"}  
    
   - DELETE метод
     URL: http://127.0.0.1:5000/twit/номер id
     Удаляем существующий твит. Прописываем URL с номером нужного id, например:

              URL http://127.0.0.1:5000/twit/1

Проверить изменения можно спомощью GET метода.
