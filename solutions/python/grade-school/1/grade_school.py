class School:
    def __init__(self):
        self.rank={}
        self.test=[]

    def add_student(self, name, grade):
        if name in self.rank.keys():
            self.test.append(False)
            return
        self.rank[name]=grade
        self.test.append(True)
        self.rank=dict(sorted(self.rank.items(), key=lambda x : (x[1],x[0])))
        
    def roster(self):
        return list(self.rank)

    def grade(self, grade_number):
        return [name for name, grade in self.rank.items() if grade==grade_number]
        
    def added(self):
        return self.test