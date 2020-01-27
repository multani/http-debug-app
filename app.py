#!/usr/bin/env python3

import argparse
from bottle import route, run, template, request


@route('/')
def index():
    return '<b>hit /debug/</b>'


@route('/sum/<a:int>/<b:int>')
def sum_endpoint(a, b):
    return {"res": a + b}

@route('/json/debug/<path:re:.*>')
def json_debug(path):
    return {
        "url": request.url,
        "headers": [{k: v} for (k, v) in sorted(request.headers.items())],
    }

@route('/debug/<path:re:.*>')
def debug(path):
    headers = "\n".join("{}: {}".format(k, v) for (k, v) in sorted(request.headers.items()))
    return template("""<html>
<body>
<p>URL: {{ url }}</p>
<p>Headers:</p>
<pre>
{{ headers }}
</pre>
</body>
</html>
""",
    url=request.url, headers=headers)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--listen', default='0.0.0.0')
    parser.add_argument('-p', '--port', default=8080, type=int)
    parser.add_argument('-d', '--debug', default=False, action="store_true")

    args = parser.parse_args()
    run(host=args.listen, port=args.port, debug=args.debug)

if __name__ == '__main__':
    main()
