

from simple_http_server import route, server
from simple_http_server_jinja import JinjaView, set_env
from jinja2 import Environment, FileSystemLoader

@route("/index")
def index(name: str = "world"):
    return JinjaView("index.html", {"name": name})

def main():
    env = Environment(loader=FileSystemLoader("/you/own/template/folder"))
    set_env(env)
    server.start(port=9090)

if __name__ == "__main__":
    main()
