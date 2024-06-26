from flask import request, jsonify
from flask.views import MethodView
from models.save_data import SaveData

class SaveDataView(MethodView):
    def __init__(self):
        self.solver = SaveData()

    def post(self):
        try:
            dataToSave = request.json.get('text')
            
            formatted_solution = self.solver.save_solution(dataToSave)
            
            return jsonify({"success": True, "solution": formatted_solution}), 200
            
        except Exception as e:
            return jsonify({"error": str(e)}), 400
