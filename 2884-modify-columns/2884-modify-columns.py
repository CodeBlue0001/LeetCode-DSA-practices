import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    sal=employees['salary']*2
    return employees.assign(salary=2*employees['salary'])
    # return employees