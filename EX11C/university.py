"""University structure library."""


class Student:
    """A student class."""
    id = 1

    def __init__(self, name):
        """
        Class constructor.

        :param name:
        """
        self.name = name
        self.id = Student.id
        Student.id += 1
        self.list_of_subjects = []

    def get_name(self):
        """Get student's name"""
        return self.name

    def get_id(self):
        """
        Return student ID number.

        :return:
        """
        return self.id

    def get_subjects(self):
        """
        Return subject list.

        :return:
        """
        return self.list_of_subjects

    def add_subject(self, subject):
        """
        Add a subject to student list.

        :param subject:
        :return:
        """
        if subject not in self.list_of_subjects:
            self.list_of_subjects.append(subject)

    def remove_subject(self, subject):
        """
        Remove a subject from student list.

        :param subject:
        :return:
        """
        if subject in self.list_of_subjects:
            self.list_of_subjects.remove(subject)


class Professor:
    """A professor class."""

    def __init__(self, name):
        """
        Class constructor.

        :param name:
        """
        self.name = name
        self.subjects_num = 0

    def get_number_of_subjects(self):
        """
        Get number of subjects.

        :return:
        """
        return self.subjects_num

    def increase_number_of_subjects(self):
        """
        Increase the subjects' num.

        :return:
        """
        self.subjects_num += 1

    def get_name(self):
        """
        Return professor name.

        :return:
        """
        return self.name


class Subjects:
    """A class of subjects."""
    list_of_subjects = []

    def __init__(self, name):
        """
        Class constructor.

        :param name:
        """
        self.name = name
        Subjects.list_of_subjects.append(self.name)
        self.subjects = Subjects.list_of_subjects
        self.professor = {}

    def get_name(self):
        """
        Return subject name.

        :return:
        """
        return self.name

    def get_professor(self):
        """
        Return teaching professor's name.

        :return:
        """
        return self.professor[self.name]

    def set_professor(self, professor):
        """
        Link between professor and subject.

        :param professor:
        :return:
        """
        self.professor[self.name] = professor

    def all_subjects(self):
        """
        All subjects.

        :return:
        """
        return self.subjects