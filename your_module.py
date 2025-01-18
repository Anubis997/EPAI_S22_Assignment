class Person:
    def __init__(self, name: str, age: int, job: str):
        self.name = name
        self.age = age
        self.job = job
    
    def get_details(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Job: {self.job}"

class Student(Person):
    def __init__(self, name: str, age: int, job: str, grade: str):
        super().__init__(name, age, job)
        self.grade = grade
    
    def get_details(self) -> str:
        return f"{super().get_details()}, Grade: {self.grade}"

class Professor(Person):
    def __init__(self, name: str, age: int, job: str, courses: list):
        super().__init__(name, age, job)
        self.courses = courses
    
    def get_details(self) -> str:
        return f"{super().get_details()}, Courses: {self.courses}"

class Employee(Person):
    def __init__(self, name: str, age: int, job: str, department: str):
        super().__init__(name, age, job)
        self.department = department
    
    def get_details(self) -> str:
        return f"{super().get_details()}, Department: {self.department}"

class StudentProfessor(Student, Professor):
    def __init__(self, name: str, age: int, job: str, courses: list, grade: str):
        # Initialize Person first
        Person.__init__(self, name, age, job)
        # Initialize specific attributes from both parent classes
        self.courses = courses
        self.grade = grade
    
    def get_details(self) -> str:
        # Get base details from Person
        base_details = Person.get_details(self)
        # Add specific details from both Student and Professor
        return f"{base_details}, Courses: {self.courses}, Grade: {self.grade}"

class Location:
    __slots__ = ['name', 'longitude', 'latitude']
    
    def __init__(self, name: str, latitude: float, longitude: float):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
    
    def get_coordinates(self) -> tuple:
        return (self.latitude, self.longitude)