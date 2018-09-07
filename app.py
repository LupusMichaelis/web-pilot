import bottle
import webapi

app = application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(app=app, reloader=True)
