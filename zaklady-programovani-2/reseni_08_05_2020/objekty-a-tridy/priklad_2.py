"""
U zaměstnanců budeme nově evidovat, jestli jsou ve zkušební době.

Rozšiřte funkci __init__ třídy Employee o parametr probation, který bude typu bool. Tuto hodnotu uložte jako atribut třídy Employee.

Upravte funkci __init__ třídy Manager. Hodnotu parametru probation předejte funkci __init__ třídy Employee.

Upravte funkci getInfo. Pokud je zaměstnanec ve zkušební době, přidát k jeho/jejímu výpisu text Je ve zkušební době.
"""

class Employee:
  def takeHoliday(self, days):
    if self.remainingHolidayDays >= days:
      self.remainingHolidayDays -= days
      return f"Poté zbývá {self.remainingHolidayDays} dní."
    else:
      return f"Bohužel už máš nárok jen na {self.remainingHolidayDays} dní."
  def getInfo(self):
    vypis = f"{self.name} pracuje na pozici {self.position}. "
    if self.probation:
      vypis += "Je ve zkušební době."
    return vypis
  def __init__(self, name, position, probation):
    self.name = name
    self.position = position
    self.probation = probation
    self.remainingHolidayDays = 25

class Manager(Employee):
  def addEmployee(self, employee):
    self.employeeList.append(employee)
  def getEmployees(self):
    print("Vypisuji podřízené:")
    for employee in self.employeeList:
      print(employee.name)
  def __init__(self, name, position, probation):
    super().__init__(name, position, probation)
    self.employeeList = []
