import os
import importlib.util

def is_leap(year):
    """Returns True if the year is a leap year, False otherwise."""
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

def test_leap_year(module):
    """Tests the is_leap function in a module."""
    test_cases = {
        2000: True,
        2004: True,
        1900: False,
        2003: False
    }

    for year, expected in test_cases.items():
        assert module.is_leap(year) == expected, f"{module.__name__} failed for year {year}"

if __name__ == '__main__':
    dir_path = '.'

    for filename in os.listdir(dir_path):
        if filename.endswith('.py') and filename != 'test_leap_year.py':
            module_name = filename[:-3]  # Remove the '.py' extension
            module_path = os.path.join(dir_path, filename)

            # Load the module
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Test the module
            try:
                test_leap_year(module)
                print(f"{module.__name__}: Passed")
            except AssertionError as e:
                print(f"{module.__name__}: Failed - {e}")
