import json
import os.path

class SaveData:
    def __init__(self, data_file='outputData.json'):
        self.data_file = data_file
        self.load_data()

    def load_data(self):
        
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as json_file:
                self.existing_data = json.load(json_file)
        else:
            self.existing_data = {}

    def save_solution(self, solution):
       
        subject_data = self.existing_data.setdefault(solution['subject'], {})
        topic_data = subject_data.setdefault(solution['topic'], {})
        subtopic_list = topic_data.setdefault(solution['sub_topic'], [])

        
        formatted_solution = {
            "question": solution['question'],
            "final_answer": solution['final_answer'],
            "solution_steps": solution['solution_steps']
        }
        if not any(q['question'] == formatted_solution['question'] for q in subtopic_list):
            subtopic_list.append(formatted_solution)

        
        with open(self.data_file, 'w') as json_file:
            json.dump(self.existing_data, json_file, indent=4)

        return formatted_solution
