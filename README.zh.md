# Python Simple Http Server 的 Jinja 模板扩展

## 这是什么?

这是为工程 (https://gitee.com/keijack/python-simple-http-server) 编写的一个 Jinja 模板扩展，通过这个扩展你可以参考 MVC 的架构直接返回视图层。

## 如何使用?

安装

```
python3 -m pip install simple_http_server_jinja
```

```python
from simple_http_server import route, server
from simple_http_server_jinja import JinjaView

@route("/index")
def index(name: str = "world"):
    return JinjaView("index.html", {"name": name})

@route("/page")
def page():
    return 200, render("page.html", {"a": "b"})

def main():
    server.start(port=9090)

if __name__ == "__main__":
    main()
```

在上述的代码中，你的模板应该放在你工程的 `templates` 目录下。

```
|--templates
|----index.html
|----page.html
|--main.py
```

你也可以自定义你自己的 `Jinja2` `Environment`。

```python
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
```