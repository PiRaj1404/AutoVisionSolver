                                                                                                                                                                                                                               
from flask import Flask
from flask.views import MethodView
from flask_cors import CORS  
from dotenv import load_dotenv
from views.Index import IndexView
from views.TextTranslator import TranslateTextView
from views.ProblemSolver import SolveProblemView
from views.ImageTextDetector import DetectTextView
from views.SaveData import SaveDataView

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://127.0.0.1:5000", "http://localhost:5000"]}})
load_dotenv()

app.add_url_rule('/', view_func=IndexView.as_view('index'), methods=["GET"])
app.add_url_rule('/detect_text', view_func=DetectTextView.as_view('detect_text'), methods=["POST"])
app.add_url_rule('/translate_text', view_func=TranslateTextView.as_view('translate_text'), methods=["POST"])
app.add_url_rule('/solve_problem', view_func=SolveProblemView.as_view('solve_problem'), methods=["POST"])
app.add_url_rule('/save_to_file', view_func=SaveDataView.as_view('save_to_file'), methods=["POST"])


if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5000
    app.run(host=host, port=port, debug=True)