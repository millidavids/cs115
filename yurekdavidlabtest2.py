# Prolog
# Author: David Yurek
# Email: dayure2@g.uky.edu
# Section: 012
# December 4, 2013
# Lab Test 2: version 18


def get_file():
    loop_flag = True
    file_name = input('Enter file name: ')
    while loop_flag:
        file_list = file_name.split('.')
        if file_list[1] == 'txt':
            loop_flag = False
        else:
            file_name = input('Enter valid file name: ')
    return file_name


def get_data(file_name):
    file = open(file_name, 'r')
    data = file.read().strip()
    file.close
    return data


def get_average_and_total(lines):
    total = 0
    for index in range(len(lines)):
        temp_line = lines[index].split(',')
        denom = len(temp_line) - 1
        numer = 0
        for value in range(1, len(temp_line)):
            numer += int(temp_line[value])
        average = numer/denom
        average = round(average, 2)
        temp_line = temp_line + [average]
        lines[index] = temp_line
        print('Machine:', lines[index][0], '\tAverage Widgets:', average)
        total += numer
    return lines, total


def get_highest_average(lines_with_average):
    highest_value = 0
    for list in lines_with_average:
        if list[len(list) - 1] > highest_value:
            highest_machine = list[0]
            highest_value = list[len(list) - 1]
    return highest_machine


def main():
    file_name = get_file()
    data = get_data(file_name)
    lines = data.split('\n')
    lines_with_average, total = get_average_and_total(lines)
    print(len(lines), 'machines.')
    print(total, 'widgets made.')
    print(get_highest_average(lines_with_average), 'had the highest average widget output.')


main()


