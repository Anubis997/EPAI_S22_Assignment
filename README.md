# EPAI_S22_Assignment

Core Class Hierarchy:

Person (Base Class)

Basic attributes: name, age, job
Base method: get_details()
Serves as the foundation for all person types


Single Inheritance Classes:

Student ← Person

Adds grade attribute
Overrides get_details() to include grade


Professor ← Person

Adds courses list
Overrides get_details() to include courses


Employee ← Person

Adds department attribute
Overrides get_details() to include department




Multiple Inheritance:

StudentProfessor ← Student, Professor

Combines attributes from both Student and Professor
Custom get_details() implementation to show both roles




Separate Utility Class:

Location (using slots)

Restricted attributes: name, longitude, latitude
Memory-efficient implementation
Prevents dynamic attribute addition


Key OOP Concepts Used:

Inheritance (both single and multiple)
Method Overriding (get_details in each subclass)
Encapsulation (attributes and methods)
Super() for method delegation
Slots for memory optimization
Type Hints for better code clarity

This system effectively models different types of people in an academic setting while demonstrating various OOP principles and Python features. 
