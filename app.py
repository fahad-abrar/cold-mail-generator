from flask import Flask, request, jsonify
from model import ColdMailGenerator
from consumer import consumer
from producer import producer
from threading import Thread
import json

cold_mail = ColdMailGenerator()
app = Flask(__name__)


@app.route("/api", methods=['POST'])
def getpost():
    job_post = request.get_json()
    if not job_post or 'jobDescription' not in job_post:
        return jsonify({'error': 'Job description is required'}), 400
    
    job = job_post.get("jobDescription")

    try:
        response = cold_mail.generate(job)
        print("Generated cold mail -->>", response)
        producer(response)
        return jsonify({'mail': response}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'An error occurred while generating the email'}), 500


if __name__=='__main__':
    app.run(debug= True)






