from flask import Flask, render_template_string, request, send_from_directory
import os

class WebApp:
    def __init__(self, name="PyWebSimpleApp", port=8000, static_folder="static"):
        self.app = Flask(name, static_folder=static_folder)
        self.port = port
        self.routes = {}

        # Middleware simples para log de requisições
        @self.app.before_request
        def log_request():
            print(f"[Request] {request.method} {request.path}")

        # Rota padrão
        @self.app.route('/')
        def index():
            return "<h1>Welcome to PyWebSimple!</h1><p>Edit this page with app.add_page()</p>"

        # Servir arquivos estáticos
        @self.app.route('/static/<path:filename>')
        def static_files(filename):
            return send_from_directory(self.app.static_folder, filename)

    def add_page(self, path, html_content, methods=['GET']):
        """
        Adiciona uma página HTML.
        html_content pode conter placeholders para variáveis, ex: {{ name }}
        """
        def handler(**kwargs):
            # Passa query params e kwargs para o template
            context = dict(request.args)
            context.update(kwargs)
            return render_template_string(html_content, **context)

        self.app.add_url_rule(path, path, handler, methods=methods)
        self.routes[path] = html_content

    def add_api_endpoint(self, path, handler_func, methods=['GET']):
        """
        Adiciona um endpoint API com função handler_func.
        """
        self.app.add_url_rule(path, path, handler_func, methods=methods)

    def run(self, debug=False):
        """
        Executa o servidor Flask.
        """
        self.app.run(port=self.port, debug=debug)

    def set_port(self, port):
        """
        Altera a porta do servidor.
        """
        self.port = port