from src.backends import create_app
import os
app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5090, host="0.0.0.0", processes=4, threaded=False)