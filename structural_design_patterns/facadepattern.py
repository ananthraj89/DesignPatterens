class Investor():
    def Invest(self):
        print('Investing')

class Vendor():
    def give(self):
        print('Giving the materials!!')

class Builder():
    def build(self):
        print('Building')

class Visitor():
    def visit(self):
        print('visiting...')

class BuildingFacade():
    def __init__(self):
        self.investor = Investor()  # Facade class combination of classes and function
        self.vendor = Vendor()
        self.builder = Builder()
        self.visitor = Visitor()

    def build_project(self):
        for i in range(10):
            self.investor.Invest()

        for i in range(20):
            self.vendor.give()

        for i in range(30):
            self.builder.build()

          # visitors can only visit after building the project
            # to avoid that problem we use facade in side a facade

class Facade():         # To avoid the higher range we create facade class
    def __init__(self):
        self.building_facade = BuildingFacade()
        self.visitor = Visitor()

    def project_start(self):
        self.building_facade.build_project()  #facade inside a facade

        for i in range(100):
            self.visitor.visit()

        print('Project finished')

if __name__ == '__main__':
    facade = Facade()
    facade.project_start()



