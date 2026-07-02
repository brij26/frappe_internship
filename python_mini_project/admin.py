from logger import logger
import json
import os
from typing import Dict


class Admin:
    path = "D:/frappe_internship/python_mini_project/data.json"

    def __init__(self):
        self.__data = {}
        try:
            if os.path.exists(self.path):
                with open(self.path, "r") as f:
                    self.__data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.__data = {}

    @property
    def data(self) -> Dict[str, float]:
        return self.__data

    @data.setter
    def data(self, new_data: Dict[str, float]):
        self.__data = new_data

    @logger
    def add_student(self, name: str, marks: float):
        if marks < 0:
            raise ValueError("Marks can not be negative.")
        self.__data[name] = marks

    @logger
    def remove_student(self, name: str):
        if not self.__data:
            print("There is no data")
            return
        if name in self.__data:
            self.__data.pop(name, None)
            print(f"Removal of {name} is successful")
        else:
            raise ValueError(f"There is no student named : {name}")

    @logger
    def update_marks(self, name: str, new_marks: float):
        if not self.__data:
            print("No Data")
            return

        if name in self.__data:
            if new_marks < 0:
                raise ValueError("Marks Can not be negative.")
            old_marks = self.__data[name]
            self.__data[name] = new_marks
            print(
                f"Successfully changed marks from {old_marks} to {new_marks}")
        else:
            print(f"{name} is not present in data")

    @logger
    def search_student(self, name: str):
        if not self.__data:
            print("No Data")
            return

        if name in self.__data:
            return self.__data.get(name)
        else:
            print(f"No student Named : {name}")

    @logger
    def view_all_students(self):
        if not self.__data:
            print("No Data")
            return

        for student, marks in self.__data.items():
            print(student, " : ", marks)

    @property
    def average_marks(self):
        if not self.__data:
            raise ValueError("No students available.")
        return (sum(self.__data.values()) / len(self.__data))

    @logger
    def save_data(self):
        try:
            with open(self.path, "w") as f:
                json.dump(self.__data, f, indent=4)
        except Exception as e:
            print(e)

    # def __del__(self):
    #    try:
    #        with open(self.path, "w") as f:
    #            json.dump(self.__data, f, indent=4)
    #    except Exception as e:
    #        print(e)
