# Russian Address Validator.

Программа, функционал которой предоставляет пользователю доступ к API сервиса dadata.ru, в частности - к функционалу подсказок адресов.

При запуске программы пользователю необходимо ввести API-ключ и выбрать язык, который будет использоваться программой при работе.
Настройки сохраняются в базу данных на движке SQLite. 

После настройки необходимо ввести адрес в произвольной форме, как на английском, так и на русском. На экран будет выведено до 20 адресов, удовлетворяющих запросу. 
Для получения точных координат адреса необходимо выбрать нужный адрес из тех, что вывелись на экран. Для этого нужно ввести число, соответствующее нужному адресу.
Если нужного адреса нет в выборке, то можно вводом нуля вернутся к вводу адреса и попробовать переформулировать запрос, например, уточнить регион или город.

Завершить работу с программой можно в любой момент путем закрытия приложения, либо введя "Q" на этапе ввода адреса. 

При повторном запуске программы у пользователя будет выбор: продолжить работу с заданеными ранее настройками (API-ключ и язык) или ввести другие. Для выбора необходимо ввести 0 или 1 соответственно. 

# Начало работы

Для начала работы необходимо:

1. установить Python (тестировалось на python3.9)
2. Установить библиотеку dadata следующей командой:
``` python
pip install dadata
```
3. Зарегистрироваться на сайте https://dadata.ru/ и получить API-ключ.
