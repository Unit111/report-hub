from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer
from app.routes import app


if __name__ == "__main__":

    HTTP_PORT = 8080
    DEBUG = True

    """ Run either werkzig or tornado WSGI containers depending on whether
     we need to debug the application in situ or run it live """

    if DEBUG:
        app.debug = True
        app.run("0.0.0.0", port=HTTP_PORT)
    else:
        HTTP_SERVER = HTTPServer(WSGIContainer(app))
        HTTP_SERVER.listen(HTTP_PORT)
        IOLoop.instance().start()