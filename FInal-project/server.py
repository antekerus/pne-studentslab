import http.server
import http.client
import socketserver
import termcolor
from urllib.parse import parse_qs, urlparse
import json
from pathlib import Path
import jinja2 as j
from http import HTTPStatus
from Seq1 import Seq1

PORT = 8081
SERVER = "rest.ensembl.org"

socketserver.TCPServer.allow_reuse_address = True

def read_html_file(filename):
    contents = Path(filename).read_text()
    contents = j.Template(contents)
    return contents

def get_id(gene):
    resource = f"/lookup/symbol/human/{gene}"
    resource_params = "?content-type=application/json"
    conn = http.client.HTTPConnection(SERVER)
    conn.request("GET", resource + resource_params)
    response = conn.getresponse()
    if response.status == HTTPStatus.OK:
        data_str = response.read().decode("utf-8")
        data = json.loads(data_str)
        id = data["id"]
        return id
    else:
        return None

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        print(url_path)
        path = url_path.path
        print(path)
        params = parse_qs(url_path.query)
        print(params)
        contents = ""
        content_type = 'text/html'
        if path == "/":
            contents = Path(f"html/index.html").read_text()
            self.send_response(200)
        elif path == "/listSpecies":
            try:
                limit = None
                if len(params) == 1:
                    limit = int(params['limit'][0])
                resource = f"/info/species"
                resource_params = "?content-type=application/json"
                conn = http.client.HTTPConnection(SERVER)
                conn.request("GET", resource + resource_params)
                response = conn.getresponse()
                if response.status == HTTPStatus.OK:
                    data_str = response.read().decode("utf-8")
                    data = json.loads(data_str)
                    species = data["species"]
                    name_species = []
                    for specie in species[:limit]:
                        name_species.append(specie["display_name"])
                    context = {
                        "limit": limit,
                        "name_species": name_species,
                        "number_of_species": len(species)
                    }
                    contents = read_html_file("./html/species.html").render(context=context)
                    self.send_response(200)
                    if limit is not None:
                        if limit > len(species):
                            context = {"error": "the value is greater than the total of species"}
                            contents = read_html_file(f"html/error.html").render(context=context)
                            self.send_response(404)
                        elif limit < 0:
                            context = {"error": "the value is negative"}
                            contents = read_html_file(f"html/error.html").render(context=context)
                            self.send_response(404)
            except (ValueError, KeyError):
                context = {"error": "the value is not a number or contains letters"}
                contents = read_html_file(f"html/error.html").render(context=context)
                self.send_response(404)
        elif path == "/karyotype":
            try:
                species = params['species'][0]
                species = species.split()
                if len(species) == 1:
                    species = species[0]
                    resource = f"/info/assembly/{species}"
                    resource_params = "?content-type=application/json"
                    conn = http.client.HTTPConnection(SERVER)
                    conn.request("GET", resource + resource_params)
                    response = conn.getresponse()
                    if response.status == HTTPStatus.OK:
                        data_str = response.read().decode("utf-8")
                        data = json.loads(data_str)
                        print(data)
                        context = {
                            "species": species,
                            "karyotype": data["karyotype"],
                        }
                        contents = read_html_file("./html/karyotype.html").render(context=context)
                        self.send_response(200)
                    else:
                        context = {"error": "the specie is not valid or does not exist"}
                        contents = read_html_file(f"html/error.html").render(context=context)
                        self.send_response(404)
                else:
                    context = {"error": "the specie is introduced incorrectly"}
                    contents = read_html_file(f"html/error.html").render(context=context)
                    self.send_response(404)
            except KeyError:
                context = {"error": "the specie introduced is not valid"}
                contents = read_html_file(f"html/error.html").render(context=context)
                self.send_response(404)
        elif path == "/chromosomeLength":
            try:
                specie = params['specie'][0]
                specie = specie.split()
                chromo = int(params['chromo'][0])
                if len(specie) == 1:
                    specie = specie[0]
                    if chromo >= 0:
                        resource = f"/info/assembly/{specie}"
                        resource_params = "?content-type=application/json"
                        conn = http.client.HTTPConnection(SERVER)
                        conn.request("GET", resource + resource_params)
                        response = conn.getresponse()
                        if response.status == HTTPStatus.OK:
                            data_str = response.read().decode("utf-8")
                            data = json.loads(data_str)
                            top_level_region = data["top_level_region"]
                            length = None
                            i = 0
                            found = False
                            while not found and i < len(top_level_region):
                                d = top_level_region[i]
                                if d["name"] == str(chromo):
                                    found = True
                                    length = d["length"]
                                i += 1
                            if found:
                                context = {
                                    "specie": specie,
                                    "chromo": chromo,
                                    "length": length,
                                }
                                contents = read_html_file("./html/chromo_length.html").render(context=context)
                                self.send_response(200)
                            else:
                                context = {"error": "the chromosome introduced is not valid"}
                                contents = read_html_file(f"html/error.html").render(context=context)
                                self.send_response(404)
                        else:
                            context = {"error": "the specie introduced is not valid"}
                            contents = read_html_file(f"html/error.html").render(context=context)
                            self.send_response(404)
                    else:
                        context = {"error": "the value of the chromosome should be greater than 0"}
                        contents = read_html_file(f"html/error.html").render(context=context)
                        self.send_response(404)
                else:
                    context = {"error": "the specie is introduced incorrectly"}
                    contents = read_html_file(f"html/error.html").render(context=context)
                    self.send_response(404)
            except (ValueError, KeyError):
                context = {"error": "the values introduced are not valid"}
                contents = read_html_file(f"html/error.html").render(context=context)
                self.send_response(404)
        elif path == "/geneSeq":
            try:
                gene = params['gene'][0]
                gene = gene.split()
                if len(gene) == 1:
                    gene = gene[0]
                    gene_id = get_id(gene)
                    if gene_id:
                        resource = f"/sequence/id/{gene_id}"
                        resource_params = "?content-type=application/json"
                        conn = http.client.HTTPConnection(SERVER)
                        conn.request("GET", resource + resource_params)
                        response = conn.getresponse()
                        if response.status == HTTPStatus.OK:
                            data_str = response.read().decode("utf-8")
                            data = json.loads(data_str)
                            sequence = data["seq"]
                            context = {
                                "gene": gene,
                                "sequence": sequence,
                            }
                            contents = read_html_file("./html/gene_seq.html").render(context=context)
                            self.send_response(200)
                    else:
                        context = {"error": "there is not an id for the gene or the gene does not exist"}
                        contents = read_html_file(f"html/error.html").render(context=context)
                        self.send_response(404)
                else:
                    context = {"error": "the gene is introduced incorrectly"}
                    contents = read_html_file(f"html/error.html").render(context=context)
                    self.send_response(404)
            except KeyError:
                context = {"error": "the values introduced are not valid"}
                contents = read_html_file(f"html/error.html").render(context=context)
                self.send_response(404)
        elif path == "/geneInfo":
            try:
                gene = params['gene'][0]
                gene = gene.split()
                if len(gene) == 1:
                    gene = gene[0]
                    gene_id = get_id(gene)
                    if gene_id:
                        resource = f"/overlap/id/{gene_id}"
                        resource_params = "?feature=gene;content-type=application/json"
                        conn = http.client.HTTPConnection(SERVER)
                        conn.request("GET", resource + resource_params)
                        response = conn.getresponse()
                        if response.status == HTTPStatus.OK:
                            data_str = response.read().decode("utf-8")
                            data = json.loads(data_str)
                            info_gene = None
                            found = False
                            i = 0
                            while not found and i < len(data):
                                if data[i]['gene_id'] == gene_id:
                                    found = True
                                    info_gene = data[i]
                                i += 1
                            if found:
                                context = {
                                    "gene": gene,
                                    "chromo_name": info_gene["assembly_name"],
                                    "start": info_gene["start"],
                                    "end": info_gene["end"],
                                    "length": info_gene["end"] - info_gene["start"],
                                    "id_gene": gene_id
                                }
                                contents = read_html_file("./html/gene_info.html").render(context=context)
                                self.send_response(200)
                            else:
                                context = {"error": "the gene introduced is not valid"}
                                contents = read_html_file(f"html/error.html").render(context=context)
                                self.send_response(404)
                    else:
                        context = {"error": "there is not an id for the gene or the gene does not exist"}
                        contents = read_html_file(f"html/error.html").render(context=context)
                        self.send_response(404)
                else:
                    context = {"error": "the gene is introduced incorrectly"}
                    contents = read_html_file(f"html/error.html").render(context=context)
                    self.send_response(404)
            except KeyError:
                context = {"error": "the values introduced are not valid"}
                contents = read_html_file(f"html/error.html").render(context=context)
                self.send_response(404)
        elif path == "/geneCalc":
            try:
                gene = params['gene'][0]
                gene = gene.split()
                if len(gene) == 1:
                    gene = gene[0]
                    gene_id = get_id(gene)
                    if gene_id:
                        resource = f"/sequence/id/{gene_id}"
                        resource_params = "?content-type=application/json"
                        conn = http.client.HTTPConnection(SERVER)
                        conn.request("GET", resource + resource_params)
                        response = conn.getresponse()
                        if response.status == HTTPStatus.OK:
                            data_str = response.read().decode("utf-8")
                            data = json.loads(data_str)
                            sequence = data["seq"]
                            s = Seq1(sequence)
                            info = s.info()
                            context = {
                                "gene": gene,
                                "info": info
                            }
                            contents = read_html_file("./html/gene_calc.html").render(context=context)
                            self.send_response(200)
                    else:
                        context = {"error": "there is not an id for the gene or the gene does not exist"}
                        contents = read_html_file(f"html/error.html").render(context=context)
                        self.send_response(404)
                else:
                    context = {"error": "the gene is introduced incorrectly"}
                    contents = read_html_file(f"html/error.html").render(context=context)
                    self.send_response(404)
            except KeyError:
                context = {"error": "the values introduced are not valid"}
                contents = read_html_file(f"html/error.html").render(context=context)
                self.send_response(404)
        elif path == "/geneList":
            try:
                chromo = int(params['chromo'][0])
                start = int(params['start'][0])
                end = int(params['end'][0])
                length = end - start
                if length > 0:
                    if chromo > 0:
                        resource = f"/overlap/region/human/{chromo}:{start}-{end}"
                        resource_params = "?content-type=application/json;" \
                                          "feature=gene;feature=transcript;feature=cds;feature=exon"
                        conn = http.client.HTTPConnection(SERVER)
                        conn.request("GET", resource + resource_params)
                        response = conn.getresponse()
                        if response.status == HTTPStatus.OK:
                            data_str = response.read().decode("utf-8")
                            data = json.loads(data_str)
                            gene_names = []
                            for gene in data:
                                if "external_name" in gene:
                                    gene_names.append(gene["external_name"])
                            context = {
                                "chromo": chromo,
                                "start": start,
                                "end": end,
                                "gene_names": gene_names
                            }
                            contents = read_html_file("./html/gene_list.html").render(context=context)
                            self.send_response(200)
                        else:
                            context = {"error": "it does not exist a gene list with these parameters"}
                            contents = read_html_file(f"html/error.html").render(context=context)
                            self.send_response(404)
                    else:
                        context = {"error": "the chromosome value must be greater than 0"}
                        contents = read_html_file(f"html/error.html").render(context=context)
                        self.send_response(404)
                else:
                    context = {"error": "the length of the chromosome must be greater than 0"}
                    contents = read_html_file(f"html/error.html").render(context=context)
                    self.send_response(404)
            except (KeyError, ValueError):
                context = {"error": "the values introduced are not valid"}
                contents = read_html_file(f"html/error.html").render(context=context)
                self.send_response(404)
        contents_bytes = contents.encode()
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(contents_bytes)))
        self.end_headers()
        self.wfile.write(contents_bytes)
        return


with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()
