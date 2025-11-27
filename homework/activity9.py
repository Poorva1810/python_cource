class ExpressionSolver:
    def __init__(self, expression):
        self.expression = expression

    def solve(self):
        try:
            result = eval(self.expression)
            return result
        except Exception as e:
            return f"Error: {e}"
        
    def display_result(self):
        result = self.solve()
        print(f"Expression: {self.expression}")
        print(f"Result: {result}")
expr = input("Enter a mathematical expression: ")

solver = ExpressionSolver(expr)
solver.display_result()
