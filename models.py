"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database"""

    db.app = app
    db.init_app(app)


class Cupcake(db.Model):
    """Cupcake."""

    __tablename__ = "cupcake"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
    )

    flavor = db.Column(
        db.String(20),
        nullable=False,
        #make unique
    )

    size = db.Column(
        db.String(20),
        nullable=False,
    )

    rating = db.Column(
        db.Integer,
        nullable=False,
    )

    image = db.Column(
        db.String(200),
        nullable=False,
        default="https://tinyurl.com/demo/cupcake",
    )

    def serialize(self):
        """Serialize to dictionary"""

        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image,
        }
