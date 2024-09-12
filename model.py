from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')

class ColdMailGenerator:

    def __init__(self):
        self.llm = GoogleGenerativeAI(
            model="gemini-1.5-pro",
            google_api_key=api_key
        )
        self.prompt = """You are a job seeker. Retrieve the required skills and related info from the provided job post.
        Your task is to write a short cold email to the client regarding the job post.
        Do not provide a preamble.
        """

    def generate(self, body):
        # Concatenate the prompt and the job description body into a single string
        message_content = self.prompt + "\n" + body
        
        # Create a HumanMessage object with the concatenated content
        message = HumanMessage(
            content=message_content
        )

        # Invoke the LLM with the formatted message
        response = self.llm.invoke([message])
        print(response)  # Debugging line to print the raw response

        return response
