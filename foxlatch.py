from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def view_index(request):
    htmlFile = open('templates/index.pt')
    html = ''
    for line in htmlFile:
        html += line
    htmlFile.close()
    return Response(html)

def view_about(request):
    htmlFile = open('templates/about.pt')
    html = ''
    for line in htmlFile:
        html += line
    htmlFile.close()
    return Response(html)

def make_page(config, routeName, path):
    config.add_route(routeName, path)
    if routeName == 'index':
        config.add_view(view_index, route_name = routeName)
    elif routeName == 'about':
        config.add_view(view_about, route_name = routeName)

if __name__ == '__main__':
    config = Configurator()
    make_page(config, 'index', '/')
    make_page(config, 'about', '/about')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 3333, app)
    server.serve_forever()
