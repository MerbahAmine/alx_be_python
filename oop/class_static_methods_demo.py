# class_static_methods_demo.py

class Calculator:
    # class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: Does not need access to class or instance."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: Can access class attributes like calculation_type."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
