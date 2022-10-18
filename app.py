from backends import create_app
import os
import ssl
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('certificate.crt', 'private.key')

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5090, host="0.0.0.0", ssl_context=context)