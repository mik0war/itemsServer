from flask import Flask

import repository

app = Flask(__name__)


@app.route('/get_items')
def get_items():
    return repository.get_items()

@app.route('/get_characteristic/<int:id>')
def get_characteristic(id):
    return repository.get_characteristic(id)


if __name__ == '__main__':
    app.run()