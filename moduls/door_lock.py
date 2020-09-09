import socket


class door_lock:
    '''
    Клас предназначен для удаленного открытия электромагнитного замка
    '''
    def __init__(self, ip_door: str, port_door: int, debug: bool=False):
        '''

        :param ip_door: ip сервера
        :param port_door: Порт сервера
        :param debug: при включенной отладки замок не будет открываться а будет выводить сообщения
        '''
        self.DEBUG = debug
        self.IP_DOOR = ip_door
        self.POST_DOOR = port_door

    def send_message(self, message):
        '''
        Отправляет команду на дверь
        :param message:
        :return:
        '''
        if not self.DEBUG:
            sock = socket.socket()
            sock.connect((self.IP_DOOR, self.POST_DOOR))

            sock.send(bytes(message, encoding='utf8'))
            data = sock.recv(1024)

            if data == bytes(message, encoding='utf8'):
                print("Команда дошла успешно")
            else:
                print("Что то пошло не так")

            sock.close()
        else:
            print("Команда отправленная на дверь {}".format(message))

    def open_door(self):
        '''
        Открыть дверь
        :param update:
        :param context:
        :return:
        '''
        self.send_message('open')


    def disable_door(self):
        '''
        ОТключить замок
        :param update:
        :param context:
        :return:
        '''
        self.send_message('disable_door')


    def enable_door(self):
        '''
        Активировать замок
        :param update:
        :param context:
        :return:
        '''
        self.send_message('enable_door')
