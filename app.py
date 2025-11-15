from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Portfolio projeleri
projects = [
    {
        'id': 1,
        'title': 'E-Ticaret Platformu',
        'description': 'Modern ve kullanıcı dostu bir e-ticaret çözümü',
        'tech': ['Python', 'Flask', 'PostgreSQL', 'React'],
        'image': 'project1.jpg',
        'link': '#'
    },
    {
        'id': 2,
        'title': 'Yapay Zeka Chat Botu',
        'description': 'Doğal dil işleme ile akıllı sohbet uygulaması',
        'tech': ['Python', 'TensorFlow', 'NLP', 'FastAPI'],
        'image': 'project2.jpg',
        'link': '#'
    },
    {
        'id': 3,
        'title': 'Veri Analizi Paneli',
        'description': 'Gerçek zamanlı veri görselleştirme ve analiz',
        'tech': ['Python', 'Pandas', 'D3.js', 'Django'],
        'image': 'project3.jpg',
        'link': '#'
    },
    {
        'id': 4,
        'title': 'Mobil Uygulama API',
        'description': 'Yüksek performanslı RESTful API servisi',
        'tech': ['Python', 'FastAPI', 'Redis', 'Docker'],
        'image': 'project4.jpg',
        'link': '#'
    }
]

# Yetenekler
skills = [
    {'name': 'Python', 'level': 95},
    {'name': 'JavaScript', 'level': 90},
    {'name': 'React', 'level': 85},
    {'name': 'Flask/Django', 'level': 90},
    {'name': 'SQL/NoSQL', 'level': 85},
    {'name': 'Machine Learning', 'level': 80},
    {'name': 'Docker/DevOps', 'level': 85},
    {'name': 'Git/GitHub', 'level': 90}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/projects')
def get_projects():
    return jsonify(projects)

@app.route('/api/skills')
def get_skills():
    return jsonify(skills)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
