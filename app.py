from flask import Flask

app = Flask(__name__)


@app.route('/page/v1/hello-world-<int:page_id>')
def page(page_id):
    return f"Hello world, {page_id}"


if __name__ == '__main__':
    app.run()

# fuser -k 5000/tcp
# gunicorn --bind 0.0.0.0:5000 app:app