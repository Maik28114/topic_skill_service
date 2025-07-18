import json
import os
import uuid
from flask import Flask, jsonify, request 
from data_manager import JsonDataManager

app = Flask(__name__)
data_manager = JsonDataManager()

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
TOPICS_FILE = os.path.join(DATA_DIR, 'topics.json')
SKILLS_FILE = os.path.join(DATA_DIR, 'skills.json')

@app.route('/')
def hello_world():
    return 'Hello from Topic and Skill Service!'




# ------------------- GET METHODS -----------------
# --------------------- topics ---------------------
@app.route('/topics', methods=['GET'])
def get_topics():
    topics = data_manager.read_data(TOPICS_FILE)
    return jsonify(topics)

@app.route('/topics/<string:id>', methods=['GET'])
def get_topic_id(id):
    topics = data_manager.read_data(TOPICS_FILE)
    topic = next((topic for topic in topics if topic.get('id').lower() == id.lower()), None)
    if topic: 
        return jsonify(topic)
    return jsonify({"[ERROR]": "Topic ID not found"}), 404
# --------------------- skills ---------------------

@app.route("/skills", methods=["GET"])
def get_skills():
    skills = data_manager.read_data(SKILLS_FILE)
    return jsonify(skills)

@app.route('/skills/<string:id>', methods=['GET'])
def get_skills_id(id):
    skills = data_manager.read_data(SKILLS_FILE)
    skill = next((skill for skill in skills if skill.get('id').lower() == id.lower()), None)
    if skill:
        return jsonify(skill)
    return jsonify({"[ERROR]": "Skill ID not found"}), 404

# ------------------- POST METHODS -----------------
# --------------------- topics ---------------------

@app.route('/topics', methods=['POST'])
def create_topic():
    new_topic_data = request.json
    if not new_topic_data or 'name' not in new_topic_data or 'description' not in new_topic_data:
        return jsonify({"[ERROR]":"'Name' or 'description' not in POST"}),400
    new_topic_id = str(uuid.uuid4())
    new_topic = {
        "id": new_topic_id,
        "name": new_topic_data['name'],
        "description": new_topic_data['description']
    }
    topics = data_manager.read_data(TOPICS_FILE)
    topics.append(new_topic)

    data_manager.write_data(TOPICS_FILE, topics)
    return jsonify(new_topic), 201

@app.route('/skills', methods=['POST'])
def create_skills():
    new_skills_data = request.json
    if not new_skills_data or 'name' not in new_skills_data or 'topicId' not in new_skills_data:
        return jsonify({"ERROR]":"'Name' or 'topicId' not in POST"}),400
    new_skills_id = str(uuid.uuid4())
    new_skills = {
        "id": new_skills_id,
        "name": new_skills_data['name'],
        "topicId": new_skills_data['topicId'],
        "difficulty": new_skills_data['difficulty']

    }
    skills = data_manager.read_data(SKILLS_FILE)
    skills.append(new_skills)

    data_manager.write_data(SKILLS_FILE, skills)
    return jsonify(new_skills), 201






if __name__== '__main__':
    app.run(debug=True, port=5000)