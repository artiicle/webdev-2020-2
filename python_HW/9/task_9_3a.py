# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_vlan_map(config_filename):
    with open(config_filename, 'r') as my_file:
            access_config = {}
            trunk_config = {}
            interface = '' 
            for line in my_file:
                if line.find('FastEthernet') != -1:
                    interface = line.split()[-1]
                if line.find('mode access'):
                    access_vlan = '1'
                    access_config[interface] = access_vlan
                if line.find('access vlan') != -1:
                    access_vlan = line.split()[-1]
                    access_config[interface] = access_vlan
                if line.find('trunk allowed vlan') != -1:
                    trunk_vlan = line.split()[-1]
                    trunk_config[interface] = trunk_vlan
            print('access interfaces: \n', access_config)
            print('trunk interfaces: \n', trunk_config)
    my_file.close()
    return access_config, trunk_config
get_int_vlan_map('/home/std/python-web/exercises/09_functions/config_sw1.txt')


