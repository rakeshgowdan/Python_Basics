class StudentInfo():
    def getDeatails(self,name,id,section):
        self.name=name
        self.id=id
        self.section=section
    def output(self):
        print("your name is " +self.name+"your id is" +self.id+"your section is" +self.section)
    def __init__(self):
     i=1

print("calling class")
object=StudentInfo()
object.getDeatails('ram','20','b')
object.output()

