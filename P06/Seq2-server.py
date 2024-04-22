import http.server
import socketserver
import termcolor
from urllib.parse import parse_qs, urlparse
from pathlib import Path
import jinja2 as j
from Seq1 import Seq1
import os

PORT = 8081
SEQUENCES = ['ACCTG', 'GCTAA', 'TTACC', 'ACTGG', 'CATAG']
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
OPERATIONS = ["info", "comp", "rev"]

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        print(url_path)
        params = parse_qs(url_path.query)
        print(params)
        if self.path == "/":
            contents = Path(f"html/index.html").read_text()
            contents = j.Template(contents)
            context = {"n_sequences": len(SEQUENCES), "genes": GENES}
            contents = contents.render(context=context)
            self.send_response(200)
        elif self.path == "/ping?":
            contents = Path(f"html/ping.html").read_text()
            self.send_response(200)
        elif self.path.startswith("/get?"):
            try:
                seq_n = int(params['seq_n'][0])
                contents = Path(f"html/get.html").read_text()
                contents = j.Template(contents)
                context = {"number": seq_n, "sequence": SEQUENCES[seq_n]}
                contents = contents.render(context=context)
                self.send_response(200)
            except (KeyError, IndexError, ValueError):
                contents = Path(f"html/error.html").read_text()
                self.send_response(404)
        elif self.path.startswith("/gene?"):
            try:
                gene_name = params['gene_name'][0]
                contents = Path(f"html/gene.html").read_text()
                contents = j.Template(contents)
                file_name = os.path.join("Genes", gene_name + ".txt")
                s = Seq1()
                s.read_fasta(file_name)
                context = {"gene_name": gene_name, "sequence": str(s)}
                contents = contents.render(context=context)
                self.send_response(200)
            except (KeyError, IndexError, ValueError):
                contents = Path(f"html/error.html").read_text()
                self.send_response(404)
        elif self.path.startswith("/operation?"):
            try:
                bases = params['bases'][0]
                op = params['op'][0]
                contents = Path("html/operation.html").read_text()
                contents = j.Template(contents)
                s = Seq1(bases)
                if op in OPERATIONS:
                    if op == "info":
                        result = s.info()
                    elif op == "comp":
                        result = s.complement()
                    else:  # elif op == "rev":
                        result = s.reverse()
                    context = {"sequence": str(s), "op": op.lower(), "result": result}
                    contents = contents.render(context=context)
                    self.send_response(200)
            except (KeyError, IndexError, ValueError):
                contents = Path(f"html/error.html").read_text()
                self.send_response(404)
        else:
            contents = Path("html/error.html").read_text()
            self.send_response(404)

        contents_bytes = contents.encode()
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(contents_bytes)))
        self.end_headers()
        self.wfile.write(contents_bytes)


with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()
