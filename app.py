from backends import create_app
import os
app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=443, host="0.0.0.0")