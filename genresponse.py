import google.generativeai as genai
import os

class AnalyseAndGenerateResponse():
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def genResponse(self,sql_query)->str:
        response = self.model.generate_content(f"Correct this sql query syntatically if there are any error else generate a query that aims to solve the problem {sql_query}.Make sure you dont give explaination")
        return response.text