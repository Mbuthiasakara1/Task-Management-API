from models import db

class User(db.Model):
    __tablename__='users'

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(100),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    password=db.Column(db.String(200),nullable=False)
    created_at=db.Column(db.DateTime,server_default=db.func.now())
    updated_at=db.Column(db.DateTime,server_default=db.func.now())


    #relationship btn user and task :one to many

    tasks=db.relationship('Task',back_populates='user')

    def __repr__(self):
        return f"<username{self.username},email{self.email}"
    
    def to_dict(self):
        return{
            "id":self.id,
            "username":self.username,
            "email":self.email,
            "created_at":self.created_at.isoformat() if self.created_at else None,
            "updated_at":self.updated_at.isoformat() if self.created_at else None
        }
