from flask.ext.frozen import Freezer
from burger import app

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()

    # Uncomment this to test the local server
    # freezer.run(debug=True)
