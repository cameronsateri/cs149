"""Utilities for course registration.

Author: CS 149 Instructors and Cameron Sateri
Version: 11/10/22
Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""


class Section:
    """The Section class represents one section of a course.

    Attributes:
        course_code (str): The course identifier, e.g. 'CS 149'
        section_number (int): The number of this section
        capacity (int): The maximum number of students for this section
        enrolled (int): The number of students enrolled in this section

    """

    def __init__(self, course_code, section_number, capacity):
        """Initialize a new empty Section.

        Args:
            course_code (str): The course identifier, e.g. 'CS 149'
            section_number (int): The number for this section
            capacity (int): The maximum number of students for this section

        """
        self.course_code = course_code
        self.section_number = section_number
        self.capacity = capacity
        self.enrolled = 0

    def add_students(self, num_students):
        """Add some students to this section.

        If the number of students provided exceeds the remining
        capacity then no students will be added and an error message
        will be printed.

        Args:
            num_students (int): The number of students to add

        """
        seats_remaining = self.capacity - self.enrolled
        if num_students > seats_remaining:
            print("Error: not enough seats!")
        else:
            self.enrolled += num_students

    def __str__(self):
        """Create a string representation of this Section.

        NOTE: The method name __str__ has a special meaning in
        Python. This method determines what will happen when we
        convert a Section object to a string.  This will be covered in
        section 10.2.

        Returns:
            string: A string representation of this Section

        """
        result = f"{self.course_code} {self.section_number:04}"
        result += f" ({self.enrolled}/{self.capacity})"
        return result


def create_sections(course_code, section_size, total_students):
    """Create a list of Section objects adequate for all students.

    This function will generate a list of Section objects numbered
    sequentially starting at 1. The last section may not be completely
    full if If the section size doesn't divide evenly into the total
    number of students.

    Args:
        course_code (str): The course identifier, e.g. 'CS 149'
        section_size (int): The capacity for each section
        total_students (int): The total number of students that need a seat

    Returns:
        lst (list): A list of section objects adequate to seat all students

    """
    lst = []
    transverse_section = section_size
    number = 1
    while transverse_section < total_students + section_size:
        lst.append(Section(course_code, number, section_size))
        if transverse_section > total_students:
            adder = total_students + section_size - transverse_section
            lst[number - 1].add_students(adder)
        else:
            lst[number - 1].add_students(section_size)
        transverse_section += section_size
        number += 1
    return lst


if __name__ == "__main__":

    # Execution example:
    sections = create_sections("CS 149", 30, 100)
    for section in sections:
        print(section)