
class Student:
    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort
        # self._cohorts = {
        #     "Edinburgh" : "E42",
        #     "Glasgow" : "G21"
        # }
    def talk(self):
        return "I can talk!"
    def say_favourite_language(self, language):
        return f"I love {language}"
