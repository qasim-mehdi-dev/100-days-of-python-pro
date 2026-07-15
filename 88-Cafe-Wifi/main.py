from flask import jsonify, Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(250), nullable=True)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "map_url": self.map_url,
            "img_url": self.img_url,
            "location": self.location,
            "has_sockets": self.has_sockets,
            "has_toilet": self.has_toilet,
            "has_wifi": self.has_wifi,
            "can_take_calls": self.can_take_calls,
            "seats": self.seats,
            "coffee_price": self.coffee_price,
        }
    
@app.route("/all", methods=["GET"])
def get_all_cafes():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()

    all_cafes = [cafe.to_dict() for cafe in cafes]
    return jsonify(cafes=all_cafes), 200

@app.route("/search", methods=["GET"])
def search_cafes():
    location = request.args.get("loc")

    cafes = db.session.execute(db.select(Cafe).filter_by(location=location)).scalars().all()

    if cafes:
        matching_cafes = [cafe.to_dict() for cafe in cafes]
        return jsonify(cafes=matching_cafes), 200
    else:
        return jsonify(
            error={
                "Not Found": "Sorry, we don't have a cafe at that location."
            }
        ), 404
    
@app.route("/add", methods=["POST"])
def add_cafe():
    data = request.get_json(silent=True) or request.form

    new_cafe = Cafe(
        name=data.get("name"),
        map_url=data.get("map_url"),
        img_url=data.get("img_url"),
        location=data.get("location"),
        has_sockets=str(data.get("has_sockets")).lower() in ["true", "1"],
        has_toilet=str(data.get("has_toilet")).lower() in ["true", "1"],
        has_wifi=str(data.get("has_wifi")).lower() in ["true", "1"],
        can_take_calls=str(data.get("can_take_calls")).lower() in ["true", "1"],
        seats=data.get("seats"),
        coffee_price=data.get("coffee_price"),
    )

    db.session.add(new_cafe)
    db.session.commit()

    return jsonify(
        response={
            "success": "Successfully added the new cafe."
        }
    ), 201

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price") or request.form.get("new_price")

    cafe = db.session.get(Cafe, cafe_id)  

    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()

        return jsonify(
            success="Successfully updated the price."
        ), 200
    else:
        return jsonify(
            error={
                "Not Found": "Sorry, a cafe with that id was not found in the database."
            }
        ), 404
    
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def report_closed(cafe_id):
    API_KEY = "fgvdfgdkflhidfhdhfkds"

    api_key = request.headers.get("api-key") or request.args.get("api-key")

    if api_key == API_KEY:
        cafe = db.session.get(Cafe, cafe_id)  

        if cafe:
            db.session.delete(cafe)
            db.session.commit()

            return jsonify(
                success="Successfully deleted the cafe."
            ), 200
        else:
            return jsonify(
                error={
                    "Not Found": "Sorry, a cafe with that id was not found."
                }
            ), 404
    else:
        return jsonify(
            error="Unauthorized. Make sure you have the correct api-key."
        ), 403
    
if __name__ == "__main__":
    app.run(debug=True)