from datetime import datetime

from flask import Blueprint, url_for, request
from werkzeug.utils import redirect

from pybo import db
from pybo.models import Question, Answer

bp = Blueprint('answer', __name__, url_prefix='/answer')


@bp.route('/create/<int:question_id>', methods=('POST',))
def create(question_id):
    question = Question.query.get_or_404(question_id)
    # form 엘리먼트를 통해 전달된 데이터는 여기서 flask.request 객체로 얻을 수 있다.
    content = request.form['content'] # POST 방식으로 전송된 데이터 중 name 속성이 'content'인 값
    answer = Answer(content=content, create_date=datetime.now())
    question.answer_set.append(answer) # Answer에서 db.backref('answer_set') 이거. 질문에 달린 답변들
    db.session.commit()
    return redirect(url_for('question.detail', question_id=question_id))
