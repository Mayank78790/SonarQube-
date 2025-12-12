# 1. Single Inheritance
#  Ex- 1
class Employee:
    def work(self):
        print("Employee working.")

class Manager(Employee):
    def manage_team(self):
        print("Manager managing team.")
mgr = Manager()
mgr.work()
mgr.manage_team()

# Ex- 2
class Employee:
    def work(self):
        print("Employee working.")

class Developer(Employee):
    def write_code(self):
        print("Developer writing code.")
dev = Developer()
dev.work()
dev.write_code()

# 2. Multiple Inheritance
# Ex- 1
class Employee:
    def work(self):
        print("Employee working.")
class AdminRights:
    def approve_leave(self):
        print("Admin approving leave.")
class Manager(Employee, AdminRights):
    pass
mgr = Manager()
mgr.work()
mgr.approve_leave()

# Ex- 2
class Employee:
    def work(self):
        print("Employee working.")
class TechSkills:
    def code_review(self):
        print("Reviewing code.")
class Developer(Employee, TechSkills):
    pass
dev = Developer()
dev.work()
dev.code_review()

# 3. Multilevel Inheritance
# Ex- 1 
class Employee:
    def work(self):
        print("Employee working.")
class Manager(Employee):
    def manage_team(self):
        print("Manager managing team.")
class SeniorManager(Manager):
    def strategize(self):
        print("Senior Manager planning strategy.")
s_mgr = SeniorManager()
s_mgr.work()
s_mgr.manage_team()
s_mgr.strategize()

# Ex- 2
class Employee:
    def work(self):
        print("Employee working.")
class Developer(Employee):
    def develop(self):
        print("Developing software.")
class Tester(Developer):
    def test(self):
        print("Testing software.")
tester = Tester()
tester.work()
tester.develop()
tester.test()

# 4. Hierarchical Inheritance
# Ex- 1
class Employee:
    def work(self):
        print("Employee working.")
class Manager(Employee):
    def manage(self):
        print("Manager specific method.")
class Developer(Employee):
    def develop(self):
        print("Developer specific method.")
mgr = Manager()
dev = Developer()
mgr.work()
mgr.manage()
dev.work()
dev.develop()

# Ex- 2
class Employee:
    def work(self):
        print("Employee working.")
class Developer(Employee):
    def code(self):
        print("Developer coding.")
class Tester(Employee):
    def test(self):
        print("Tester testing.")
dev = Developer()
tester = Tester()
dev.work()
dev.code()
tester.work()
tester.test()

# 5. Hybrid Inheritance
# Ex- 1
class Employee:
    def work(self):
        print("Employee working.")
class Manager(Employee):
    def manage(self):
        print("Manager managing.")
class Developer(Employee):
    def develop(self):
        print("Developer developing.")
class Lead(Manager, Developer):
    def lead_team(self):
        print("Lead leads the team.")
lead = Lead()
lead.work()
lead.manage()
lead.develop()
lead.lead_team()

# Ex- 2
class Employee:
    pass
class Developer(Employee):
    pass
class Tester(Employee):
    pass
class DevTester(Developer, Tester):
    def multitask(self):
        print("DevTester can develop and test.")
dt = DevTester()
dt.multitask()