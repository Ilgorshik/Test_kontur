#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess

# Полный путь к appcmd, иначе у меня не распознается команда без полного пути
appcmd_path = r'C:\Windows\System32\inetsrv\appcmd.exe'

# Команда для включения службы IIS
command = "net start w3svc"

try:
    subprocess.check_output(command, shell=True)
    print("Служба IIS успешно включена.")
except subprocess.CalledProcessError as error1:
    print(f"Ошибка: {error1}")

# Команда для удаления дефолтного сайта
remove_site = f'{appcmd_path} delete site "Default Web Site"'

try:
    # Выполняем команду для удаления дефолтного сайта
    subprocess.check_output(remove_site, shell=True)
    print("Стандартный сайт IIS успешно удален.")
except subprocess.CalledProcessError as error2:
    print(f"Ошибка: {error2}")

# Команда для создания нового сайта
create_site = [appcmd_path, 'add', 'site', '/name:MySite', '/bindings:http/*:4321:', '/physicalPath:C:\mysite']

try:
    # Создаем новый сайт
    subprocess.check_output(create_site, shell=True, text=True)
    print("Сайт MySite успешно создан на порту 4321 с путем C:\\mysite.")
except subprocess.CalledProcessError as error3:
    print(f"Ошибка: {error3}")