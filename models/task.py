from models import db

class Task(db.Model):
    __tablename__='tasks'

    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
    title=db.Column(db.String(20),nullable=False)
    description=db.Column(db.String(80),nullable=False)
    status=db.Column(db.String ,default='pending')
    priority=db.Column(db.String ,default='medium')
    due_date=db.Column(db.DateTime,nullable=False)
    created_at=db.Column(db.DateTime,server_default=db.func.now())
    updated_at=db.Column(db.DateTime,server_default=db.func.now(),onupdate=db.func.now())

    #relationship btn user and task :one to many

    user=db.relationship('User',back_populates='tasks')
    #relationship btn task and attachements  :one to many

    attachments=db.relationship('Attachment', back_populates='task')
    def __repr__(self):
        return f"<user_id{self.user_id},title{self.title}>"
    

    def to_dict(self):
     return {
        "id": self.id,
        "user_id": self.user_id,
        "title": self.title,
        "description": self.description,
        "status": self.status,
        "priority": self.priority,
        "due_date": self.due_date.isoformat() if self.due_date else None,
        "created_at": self.created_at.isoformat() if self.created_at else None,
        "updated_at": self.updated_at.isoformat() if self.updated_at else None
    }


   





 