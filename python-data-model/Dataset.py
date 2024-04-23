from collections import namedtuple

"""
Dataset.py contains the definition of
a dataset object.

A dataset object consists of rows and columns.
Rows are called observation and columns called
variables.


"""
Variable = namedtuple('Variable', ['name', 'type'])

class Columns:
    def __init__(self, vars: list) -> None:
        self.__vars__ = [Variable(var[0], var[1]) for var in vars]

    def __repr__(self) -> str:
        content = ""
        for var in self.__vars__:
            content += f'name: {var.name}\t type: {var.type}\n'
        return content
    
    def __len__(self):
        return len(self.__vars__)
    
    def __getitem__(self, pos):
        return self.__vars__[pos]
    

age = Variable('age', 'int')
gender = Variable('gender', 'Categorical')
heartRate = Variable('heart rate', 'int')

vars = [age, gender, heartRate]

cols = Columns(vars)

print(len(cols))
print(cols)
print(cols[0])