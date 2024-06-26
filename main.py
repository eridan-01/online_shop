from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def __get_html_content(self):
        return """
        <!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bosfor</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
</head>
<body>
<div class="flex-column align-items-center border-bottom box-shadow">
    <nav class="navbar navbar-expand-lg bg-body-tertiary" data-bs-theme="dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="/">
                <img src="https://sun9-56.userapi.com/impg/L-7l42bYhWWKUZ0xKIQ-ENOTSTx4hTsHnjdk6w/mKk64TOYyF4.jpg?size=1048x297&quality=95&sign=47dd03140665fe8802e0d4f9a8b23b2e&type=album"
                     alt="Bootstrap" width="210" height="60">
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                    data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
                    aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="/catalog/" role="button" data-bs-toggle="dropdown"
                           aria-expanded="false">
                            Каталог
                        </a>
                        <ul class="dropdown-menu">
                            <div class="container text-center">
                                <div class="row">
                                    <div class="col">
                                        <li>
                                            <hr class="dropdown-divider">
                                        </li>
                                        <li>
                                            <p>Площадь сооружения</p>
                                        </li>
                                        <li>
                                            <hr class="dropdown-divider">
                                        </li>
                                        <li><a class="dropdown-item" href="#">до 100 м²</a></li>
                                        <li><a class="dropdown-item" href="#">до 150 м²</a></li>
                                        <li><a class="dropdown-item" href="#">до 200 м²</a></li>
                                        <li>
                                            <hr class="dropdown-divider">
                                        </li>
                                    </div>
                                    <div class="col">
                                        <li>
                                            <p>Материал</p>
                                        </li>
                                        <li>
                                            <hr class="dropdown-divider">
                                        </li>
                                        <li><a class="dropdown-item" href="#">Каркасные</a></li>
                                        <li><a class="dropdown-item" href="#">Монолитно-каркасные</a></li>
                                        <li><a class="dropdown-item" href="#">Блоки</a></li>
                                        <li>
                                            <hr class="dropdown-divider">
                                        </li>
                                    </div>
                                    <div class="col">
                                        <li>
                                            <p>Этажность</p>
                                        </li>
                                        <li>
                                            <hr class="dropdown-divider">
                                        </li>
                                        <li><a class="dropdown-item" href="#">1 этаж</a></li>
                                        <li><a class="dropdown-item" href="#">2 этажа</a></li>
                                        <li><a class="dropdown-item" href="#">от 2 этажей</a></li>
                                        <li><a class="dropdown-item" href="#">+ мансарда</a></li>
                                    </div>
                                </div>
                            </div>
                        </ul>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/contacts/">Контакты</a>
                    </li>
                </ul>
                <form class="d-flex" role="search">
                    <input class="form-control me-2" type="search" placeholder="Поиск..." aria-label="Поиск...">
                    <button class="btn btn-outline-light" type="submit">Поиск</button>
                </form>
            </div>
        </div>
    </nav>
</div>

<div class="container">
    <div class="row text-start mt-4 bt-4">
        <div class="col-lg-9 col-md-6 col-sm-12">
            <h1>Контактная информация</h1>
            <div class="contacts-ico contacts-ico--phone">
                <span itemprop="name">Бесплатный звонок по России: </span> <br>
                <a href="tel:8777777777">8 (777) 777-77-77</a>
                <span itemprop="telephone" style="display: none;">8 (777) 777-77-77</span>
            </div>
            <div class="contacts-ico contacts-ico--phone">
                <span itemprop="name">Наш номер WatsApp: </span> <br>
                <a href="tel:8777777777">8 (777) 777-77-77</a>
                <span itemprop="telephone" style="display: none;">8 (777) 777-77-77</span>
            </div>

        </div>
        <div class="col-lg-3 col-md-6 col-sm-12">
            <div class="card mb-4 box-shadow">
                <div class="card-header">
                    <h4 class="my-0 font-weight-normal">Свяжитесь с нами</h4>
                </div>
                <div class="card-body">
                    <form method="post" action="" class="form-floating">
                        <div class="mb-3">
                            <label for="name">Имя</label>
                            <input type="text" name="name" class="form-control" id="name" placeholder="Ваше имя"
                                   required>
                        </div>
                        <div class="mb-3">
                            <label for="phone">Телефон</label>
                            <input type="text" name="phone" class="form-control" id="phone"
                                   placeholder="Контактный телефон" required>
                        </div>
                        <div class="mb-3">
                            <label for="message">Сообщение</label>
                            <textarea type="text" name="message" class="form-control" id="message"
                                      placeholder="Контактный телефон" required></textarea>
                        </div>
                        <button type="submit" class="btn btn-lg btn-block btn-dark">Отправить</button>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <footer class="bd-footer py-4 py-md-5 mt-5 bg-body-tertiary">
        <div class="container text-body-secondary">
            <div class="row">
                <div class="col-lg-3 mb-3">
                    <a class="navbar-brand" href="/">
                        <img src="https://sun9-56.userapi.com/impg/L-7l42bYhWWKUZ0xKIQ-ENOTSTx4hTsHnjdk6w/mKk64TOYyF4.jpg?size=1048x297&quality=95&sign=47dd03140665fe8802e0d4f9a8b23b2e&type=album"
                             alt="Bootstrap" width="210" height="60">
                    </a>
                    <ul class="list-unstyled small mt-3">
                        <li class="mb-2">
                            Челябинск
                        </li>
                    </ul>
                </div>
                <div class="col-6 col-lg-2 offset-lg-1 mb-3">
                    <h5>Ссылки</h5>
                    <ul class="list-unstyled">
                        <li class="mb-2"><a href="/">Главная</a></li>
                        <li class="mb-2"><a href="/catalog/">Каталог</a></li>
                        <li class="mb-2"><a href="/">Заказать проект</a></li>
                        <li class="mb-2"><a href="/">О нас</a></li>
                        <li class="mb-2"><a href="/">Акции</a></li>
                        <li class="mb-2"><a href="/contacts/">Контакты</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </footer>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL"
        crossorigin="anonymous"></script>
</body>
</html>"""

    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """
    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)
        page_content = self.__get_html_content()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")