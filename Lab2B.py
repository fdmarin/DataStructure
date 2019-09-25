"""
CS2302
Lab 2 Part B
Purpose: Write a Python 3 program that finds the 20 most used password using linked list
Created on September 2019
Diego Aguirre
@author: Federico Marin
"""

import time

class Node(object):
    password = ""
    count = -1
    next = None

    def __init__(self, password, count, next):
        self.count = count
        self.password = password
        self.next = next


class LList(object):
    head = None

    def __init__(self, head=None):
        self.head = None

    def append(self, x):
        # Inserts x at end of list L
        if is_empty(self):
            self.head = Node(x)
            self.tail = self.head

        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next

    # checks if is empty
    def is_empty(self):
        return self.head is None


# had issue with merge sort and googled issue, tried to resolve but ended up creating issues with bubble sort
# ignore
# def __len__(self):
#     return len(self.head)


# method checks for duplicate passwords and
def check_replace(string, link):
    temp = link.head

    while temp is not None:
        if temp.password == string:
            temp.count += 1
            return True
        else:
            temp = temp.next

    return False


# reads file as well as creates all elements into a linked list
def read_create_list():
    linkedlist = LList()

    file_to_read = open("10-million-combos.txt", "r")
    line = file_to_read.readline()
    for line in file_to_read:

        line = line.strip().split("	")
        password = line[-1]

        if not check_replace(password, linkedlist):  # If password was not found:
            linkedlist.head = Node(password, 1, linkedlist.head)

    file_to_read.close()

    tmp = linkedlist.head

    return linkedlist


# reads file as well as creates all elements into a dictionary
def read_create_dictionary():
    password_dictionary = {}
    dictionary_llist = LList()

    file_to_read = open("10-million-combos.txt", "r")
    line = file_to_read.readline()
    for line in file_to_read:

        line = line.strip().split("	")
        password = line[-1]

        if password in password_dictionary:
            password_dictionary[password].count += 1

        else:
            dictionary_llist.head = Node(password, 1, dictionary_llist.head)
            password_dictionary[password] = dictionary_llist.head

    file_to_read.close()
    tmp = dictionary_llist.head
    while tmp is not None:
        print(tmp.password, tmp.count)
        tmp = tmp.next


# method allows for only the top 20 passwords to be printed, will be used in merge and bubble sort
def print_20_list(LList):
    temp = LList.head
    for i in range(20):
        print("Password: ", temp.password, "occurred ", temp.count, " amount of times")
        # i + 1
        temp = temp.next


# mergesort method did not work for me as i realized last minute i was doing it as an array and ran out of time to
# correct

# def merge_sort(LLink):
#     counter = 0
#
#     if len(llink) > 1:
#         middle_point = len(LLink) // 2
#         leftside = LLink[:middle_point]
#         rightside = LLink[middle_point:]
#
#         merge_sort(rightside)
#         merge_sort(leftside)
#
#         a = 0
#         b = 0
#         c = 0
#         while a < len(leftside) and b < len(rightside):
#             if leftside[a] < rightside [b]:
#                 LLink[c] = leftside[a]
#                 a = a +1
#
#             else:
#                 LLink[c] = rightside[b]
#                 b = b + 1
#
#             c = c + 1
#
#         while a < len(leftside):
#             LLink[c] = leftside[a]
#             a = a + 1
#             c = c + 1
#
#         while b < len(rightside):
#             LLink[c] = rightside[b]
#             b = b + 1
#             c = c + 1
#
#     print_20_list(LLink)

# bubble sort would organize passwords in descending order with only top 20 printed
def bubble_sort(LLink):
    swap = True
    while swap:
        temp = LLink.head
        swap = False
        while temp.next is not None:
            if temp.count < temp.next.count:
                temp2 = temp.count
                temp.count = temp.next.count
                temp.next.count = temp2
                swap = True
            temp = temp.next

    print_20_list(LLink)


# main method where all other methods are called upon
def main():
    Sent_list = LList()
    Sent_list = read_create_list()
    print("this is the start of the linked list")
    read_create_list()
    print("")
    print("this is the start of the dictionary")
    read_create_dictionary()
    print("")
    print("Now using bubble sort to print order list")
    bubble_sort(Sent_list)

    # tried doing time import so i could see total run time but could not get to work
    # start_time = time.time()
    # print(format(time.time() - start_time))
    # print("")
    # print("now using merge sort to print ordered list")
    # merge_sort(test_list)


main()

