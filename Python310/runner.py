from utils import Utils
from repository import StudentsRepoXlsx

class TestProgramRunner:
    repo = StudentsRepoXlsx()

    def run(self):
        students = self.repo.load_students()
        login, password = Utils.input_login_pass()
        Utils.check_is_registered(students, login, password)

runner = TestProgramRunner()
runner.run()