from pybo import db

"""
>>> q = Question(subject='플라스크 모델 질문입니다.', content='id는 자동으로 생성되나요?', create_date=datetime.now())
>>> db.session.add(q)
>>> db.session.commit()

Question.query.all()
Question.query.filter(Question.id==1).all()
Question.query.get(1)
Question.query.filter(Question.subject.like('%플라스크%')).all()

q.subject = 'Flask Model Question'
db.session.delete(q)
db.session.commit()
"""

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    ## 질문을 삭제할 때 연관된 답변 데이터가 모두 삭제되기를 바란다면
    # question = db.relationship('Question', backref=db.backref('answer_set', cascade='all, delete-orphan'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
