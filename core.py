from flask import Flask, render_template_string, request, send_from_directory, redirect, jsonify, make_response
import os

class WebApp:
    def __init__(self, name="PyWebSimpleApp", port=8000, static_folder="static", template_folder="templates"):
        self.app = Flask(name, static_folder=static_folder, template_folder=template_folder)
        self.port = port
        self.routes = {}
        self.middlewares = []

        # Middleware simples para log de requisições
        @self.app.before_request
        def run_middlewares():
            for mw in self.middlewares:
                response = mw(request)
                if response:
                    return response

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
            context = dict(request.args)
            context.update(kwargs)
            return render_template_string(html_content, **context)

        self.app.add_url_rule(path, path, handler, methods=methods)
        self.routes[path] = html_content

    def add_page_from_file(self, path, filename, methods=['GET']):
        """
        Adiciona uma página carregando o template HTML de um ficheiro.
        """
        def handler(**kwargs):
            context = dict(request.args)
            context.update(kwargs)
            with open(os.path.join(self.app.template_folder, filename), 'r', encoding='utf-8') as f:
                template = f.read()
            return render_template_string(template, **context)

        self.app.add_url_rule(path, path, handler, methods=methods)
        self.routes[path] = f"Template file: {filename}"

    def add_api_endpoint(self, path, handler_func, methods=['GET']):
        """
        Adiciona um endpoint API com função handler_func.
        """
        self.app.add_url_rule(path, path, handler_func, methods=methods)

    def add_middleware(self, func):
        """
        Adiciona uma função middleware que recebe o objeto request.
        Se a função retornar uma resposta, interrompe a cadeia e retorna essa resposta.
        """
        self.middlewares.append(func)

    def redirect(self, location, code=302):
        """
        Retorna um redirecionamento HTTP.
        """
        return redirect(location, code=code)

    def json_response(self, data, code=200):
        """
        Retorna uma resposta JSON.
        """
        response = make_response(jsonify(data), code)
        response.headers['Content-Type'] = 'application/json'
        return response

    def get_cookie(self, name):
        """
        Lê um cookie da requisição.
        """
        return request.cookies.get(name)

    def set_cookie(self, response, key, value, max_age=None):
        """
        Define um cookie na resposta.
        """
        response.set_cookie(key, value, max_age=max_age)

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
