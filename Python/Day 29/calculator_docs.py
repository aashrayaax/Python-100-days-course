class Calculator:
    """
    A simple calculator class that performs basic math operations.
    """
    
    def add(self, x, y):
        """
        Add two numbers together.
        
        Args:
            x: First number
            y: Second number
            
        Returns:
            The sum of x and y
        """
        return x + y
    
    def multiply(self, x, y):
        """
        Multiply two numbers.
        
        Args:
            x: First number
            y: Second number
            
        Returns:
            The product of x and y
        """
        return x * y

if __name__ == "__main__":
    # This will show the documentation in the console
    print("\nClass documentation:")
    help(Calculator)
    
    calc = Calculator()
    print("\nMethod documentation:")
    help(calc.add)
