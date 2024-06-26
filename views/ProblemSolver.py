from flask import request, jsonify
from flask.views import MethodView
from models.problem_solver import ProblemSolver
from flask_cors import cross_origin 


class SolveProblemView(MethodView):
    def __init__(self):
        self.solver = ProblemSolver()

    @cross_origin()
    def post(self):
        prompt = request.json.get('prompt')
        
        try:
            response = self.solver.solve_problem(prompt)
            result = response.result.split(',')
            
            solution = {
                "subject": result[0].strip(),
                "topic": result[1].strip(),
                "sub_topic": result[2].strip(),
                "final_answer": result[3].strip(),
                "solution_steps": [step.strip() for step in result[4:]]

            }
            
            return jsonify({"solution": solution})
            
        except Exception as e:
            return jsonify({"error": str(e)}), 400
