class OperationSize:
    def __init__(self, start=0, end=0, functional_length=1):
        self.start = start
        self.end = end
        self.length = end - start + 1
        self.functional_length = functional_length
