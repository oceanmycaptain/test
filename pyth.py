class Student(object):
    def __init__(self,name,score):
        self._name = name
        self._scroe = score

    def get_name(self):
        return self._name
    def get_score(self):
        return self._score
    def set_score(self,score):
        if 0<=score<=100:
            self._score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self._score > 90:
            return 'A'
        elif self._score >=60:
            return 'B'
        else:
            return 'C'
bart = Student('Bart simpson',59)
print('bart.get_name()=',bart.get_name())
bart.set_score(60)
print('bart.get_score() =',bart.get_score())

#print('do not use bart._Student_name:',bart._Student__name)
