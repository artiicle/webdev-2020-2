# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess


def ping_ip_addresses(ip_addresses):
    availble_ips = list()
    unavailble_ips = list()
    for ip in ip_addresses:
        reply = subprocess.run(['ping', ip])
        if reply.returncode == 0:
            availble_ips.append(ip)
        else:
            unavailble_ips.append(ip)
    return availble_ips, unavailble_ips


list_of_ips = ["1.1.1", "8.8.8.8", "8.8.4.4", "8.8.7.1"]
print(ping_ip_addresses(list_of_ips))
