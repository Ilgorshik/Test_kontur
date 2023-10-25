#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

def all_servers(server_string):
    server_string = server_string.replace('[', '').replace(']', '')
    server_list = []
    pattern = r'vm-test(\d)-(\d)'
    matches = re.finditer(pattern, server_string)

    for match in matches:
        start = int(match.group(1))
        end = int(match.group(2))
        
        for i in range(start, end + 1):
            server_list.append(f'vm-test{i}')

    remaining_part_string = server_string.split(',')
    for part in remaining_part_string:
        if not re.match(pattern, part):
            server_list.append(part)

    return server_list

# Пример
server_string = "vm-test[1-3],vm-test3,vm-test[4-7],vm-test8"
server_list = all_servers(server_string)
print(server_list)
