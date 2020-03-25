import flask
import parseCSV

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/csv', methods=['GET'])
def parseCSV1():
    return parseCSV.csvParse()

app.run()