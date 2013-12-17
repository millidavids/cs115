# Prolog
# Author: David Yurek
# Email: dayure2@g.uky.edu
# Section: 012
# December 1, 2013
# Lab 15 Individual


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


def get_student_list(file_name):
    student_list = file_name.split('\n')
    for index in range(len(student_list)):
        student_list[index] = student_list[index].split()
    return student_list


def get_doc(file_name):
    file = open(file_name, 'r')
    doc = file.read()
    file.close()
    return doc.strip()


def get_grades(student_list):
    for student_index in range(1, len(student_list)):
        correct = 0
        for grade_index in range(1, len(student_list[0])):
            if student_list[0][grade_index] == student_list[student_index][grade_index]:
                correct += 1
        student_list[student_index].append(correct)
    return student_list


def show_results(student_list):
    number_answers = len(student_list[0]) - 1
    number_of_students = len(student_list) - 1
    total_stu_answers = 0
    for student_index in range(1, len(student_list)):
        student = student_list[student_index][0]
        number_correct = student_list[student_index][len(student_list[student_index]) - 1]
        print(student, 'got', number_correct, 'out of', number_answers, 'correct.')
        total_stu_answers += number_correct
    print('\nThere are', number_of_students, 'students.')
    if number_of_students > 0:
        print('The class average is', total_stu_answers/number_of_students)


def main():
    file_name = get_file()
    student_doc = get_doc(file_name)
    student_list = get_student_list(student_doc)
    student_list = get_grades(student_list)
    show_results(student_list)



main()