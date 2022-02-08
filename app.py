"""Flask app for Cupcakes"""
from flask import Flask, request, flash, jsonify, render_template
from models import db, connect_db, Cupcake
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config["SECRET_KEY"] = "oh-so-secret"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcakes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.get('/')
def show_homepage():
    """Shows homepage"""

    return render_template('index.html')


@app.get("/api/cupcakes")
def show_all_cupcakes():
    """Shows page with all cupcakes
    returns JSON {cupcakes: [{id, flavor, size, rating, image}]}
    """

    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)


@app.get("/api/cupcakes/<int:cupcake_id>")
def show_single_cupcake(cupcake_id):
    """Show single cupcake from cupcake id
    returns JSON {cupcake: {id, flavor, size, rating, image}}
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)


@app.post("/api/cupcakes")
def create_cupcake():
    """create cupcake from JSON data and
    returns JSON {cupcake: {id, flavor, size, rating, image}}
    """

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json.get("image") or None
    # CODE REVIEW - Changed to '.get' and use 'or none'

    cupcake = Cupcake(
        flavor=flavor,
        size=size,
        rating=rating,
        image=image,
    )
    db.session.add(cupcake)
    db.session.commit()

    serialized = cupcake.serialize()

    return (jsonify(cupcake=serialized), 201)


@app.patch("/api/cupcakes/<int:cupcake_id>")
def update_cupcake(cupcake_id):
    """Updates specified cupcake
    returns JSON {cupcake: {id, flavor, size, rating, image}}
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    flavor = request.json.get("flavor") or None
    size = request.json.get("size") or None
    rating = request.json.get("rating") or None
    image = request.json.get("image") or None


    # cupcake.flavor = request.json.get("flavor", cupcake.flavor) 




    cupcake.flavor = flavor or cupcake.flavor
    cupcake.size = size or cupcake.size
    cupcake.rating = rating or cupcake.rating
    cupcake.image = image or cupcake.image

    db.session.commit()

    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)


@app.delete("/api/cupcakes/<int:cupcake_id>")
def delete_cupcake(cupcake_id):
    """Deletes specified cupcake
    returns JSON {"deleted": cupcake_id}
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify({"deleted": cupcake_id})
