class employee:
    def __init__(self):
        print("employee created")
    def __del__(self):
        print("employee deleted,destructor called")
ob=employee()
del ob            