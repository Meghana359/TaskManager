from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from task_manager import db, ma


class Task(db.Model):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=False)
    priority = Column(Integer, default=1, nullable=False)
    description = Column(Text, nullable=True)
    start_time = Column(DateTime, nullable=True)
    end_time = Column(DateTime, nullable=True)
    time_estimate = Column(String(80), nullable=True)

    user_id = db.Column(Integer, ForeignKey('user.id'))

    def __repr__(self):
        return '<Task {} {}>'.format(self.title, self.priority)


class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Task
        include_fk = True
