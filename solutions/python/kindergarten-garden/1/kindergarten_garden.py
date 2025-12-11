STUDENTS_LIST=["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
class Garden:
    def __init__(self, diagram, students=STUDENTS_LIST):
        self.names=sorted(students)
        self.diagram=diagram.splitlines()

    def plants(self, student):
        index=self.names.index(student)*2
        save=[self.diagram[0][index:2+index], self.diagram[1][index:index+2]]
        result=[]
        for item in save:
            for c in item:
                if c=="C":
                    result.append("Clover")
                if c=="G":
                    result.append("Grass")
                if c=="V":
                    result.append("Violets")
                if c=="R":
                    result.append("Radishes")
        return result

