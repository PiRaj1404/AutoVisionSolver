import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

class ProblemSolver:
    def __init__(self):
        api_key = os.getenv('GOOGLE_API_KEY')
        genai.configure(api_key=api_key)

    def solve_problem(self, prompt):
        gen_response = genai.generate_text(prompt=prompt)
        
        return gen_response 
