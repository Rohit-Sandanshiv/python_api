from flask import Flask
from consumer_post_bp import consumer_bp
from add_product_bp import add_product_bp
from get_consumer_bp import get_consumer_bp

app = Flask(__name__)

app.register_blueprint(consumer_bp, url_prefix='/consumer')
app.register_blueprint(add_product_bp, url_prefix='/product')
app.register_blueprint(get_consumer_bp, url_prefix='/consumer')


if __name__ == "__main__":
    app.run(debug=True)