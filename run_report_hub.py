from app.routes import app


if __name__ == "__main__":

    HTTP_PORT = 8080

    app.debug = True
    app.run("0.0.0.0", port=HTTP_PORT)
