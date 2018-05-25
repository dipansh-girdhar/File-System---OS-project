# -*- coding: utf-8 -*-
"""
Created on Fri May 25 11:30:54 2018

@author: Jarvis
"""

class Process:


    def __init__(self, directory):
        self.current_file = None
        self.current_directory = directory
        self.current_index = None

    def open_file(self, file_name):
        for files in self.current_directory.sub_files:
            if not files.is_directory() and files.name == file_name:
                self.current_file = files
                self.current_index = 0
                return True
        return False

    def read_next(self):
        if self.current_file:
            file = self.current_file
            if (self.current_index + 1) <= self.current_file.size:
                return file.read(self.current_index + 1)

    def write_next(self, data):
        if self.current_file:
            if (self.current_index + 1) <= self.current_file.size + 1:
                file = self.current_file
                for i in range(len(data)):
                    file.write(self.current_index + 1 + i, data[i])
                return True

        return False

    def reset_file_pointer(self):
        self.current_index = 0

    def read(self, index):
        if self.current_file:
            if index <= self.current_file.size:
                file = self.current_file
                return file.read(index)

    def write(self, index, data):
        if self.current_file:
            if index <= self.current_file.size + 1:
                file = self.current_file
                for i in range(len(data)):
                    file.write(index + i, data[i])
                return True

        return False


    def skip(self, index):
        if self.current_file:
            file = self.current_file
            if file.reposition_index(self.current_index + index):
                self.current_index += index
                return True

        return False

    def delete_directory(self, directory_name, force):
        i = -1
        for directories in self.current_directory.sub_files:
            i += 1
            if directories.name == directory_name and directories.is_directory():
                directories.delete(force)
                self.current_directory.sub_files.pop(i)
                return True
        return False