"""
Practice file for Python Operators.
Refactored to pass SonarQube Reliability & Quality checks.
"""
import logging

# Set up logging to replace 'print' (Standard Industry Practice)
logging.basicConfig(level=logging.INFO, format='%(message)s')

def demonstrate_operators():
    """
    Main function to execute operator examples.
    Wrapping code in a function prevents 'Global code' issues.
    """
    
    # 1. Arithmetic Operators 
    a = 5 
    b = 3 
    logging.info("--- Arithmetic Operators ---")
    logging.info(a + b)   # addition
    logging.info(a - b)   # subtraction
    logging.info(a * b)   # multiplication
    logging.info(a % b)   # modulus

    # 2. Comparison operators
    # Note: In real apps, don't compare hardcoded numbers (Sonar sees this as a 'Always True/False' bug).
    logging.info("--- Comparison Operators ---")
    logging.info(a > b)   # greater than 
    logging.info(a < b)   # less than
    logging.info(a == b)  # equal 
    logging.info(a != b)  # not equal 

    # 3. Assignment Operators 
    c = 5 # Changed variable name to avoid 'unused assignment' confusion with 'a'
    logging.info(f"Assignment Operator value: {c}")

    # 4. Logical Operators
    # Rule for 'and' operator:
    # True and True = True 
    # True and False = False
    # False and False = False

    x = 10 
    y = 20
    logging.info("--- Logical Operators ---")
    logging.info(x > 10 and y < 10) 
    logging.info(x == 10 and y == 20)
    logging.info(x == 10 or y < 10) 

    # Rule for 'or' operator (FIXED: This was a syntax error in your original code)
    # True + False = True 

    # 'not' operator
    logging.info(not(x == 10 and y == 20))

    # 5. Identity operators
    list1 = [1, 2, 3]
    list2 = list1
    list3 = [1, 2, 3]

    logging.info("--- Identity Operators ---")
    logging.info(list1 is list2)   # is operator 
    logging.info(list1 is list3)
    logging.info(list1 is not list3) # is not operator

    # 6. Membership operators
    my_list = ['apple', 'orange', 'watermelon']
    logging.info("--- Membership Operators ---")
    logging.info('apple' in my_list) 
    logging.info('apple2' in my_list)
    logging.info('apple2' not in my_list) 

    # 7. Bitwise operators
    val1 = 5           # 0101 
    val2 = 3           # 0011 
    logging.info("--- Bitwise Operators ---")
    logging.info(val1 & val2)    # 0001 (Decimal: 1)

if __name__ == "__main__":
    demonstrate_operators()
