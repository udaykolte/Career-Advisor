#!/usr/bin/env python3
"""
Flask app (backend) wiring for Career & Skills Advisor
This keeps existing templates/static untouched to preserve design.
"""
import os
import sys
from datetime import datetime
from flask import Flask, render_template, request, session, redirect, url_for

# Resolve project root
CURRENT_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))

# Ensure src/ is importable
SRC_DIR = os.path.join(PROJECT_ROOT, 'src')
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

# Import domain logic from existing src
from career_advisor import CareerAdvisor

# App with template/static folders pointing to existing frontend assets
app = Flask(
    __name__,
    template_folder=os.path.join(PROJECT_ROOT, 'templates'),
    static_folder=os.path.join(PROJECT_ROOT, 'static'),
    static_url_path='/static'
)
app.secret_key = os.environ.get('SECRET_KEY', 'career-advisor-secret-key-change-in-production')

class WebCareerAdvisor(CareerAdvisor):
    """Web-compatible version of the CareerAdvisor"""
    def __init__(self):
        super().__init__()
    
    def process_user_data(self, form_data):
        self.user_profile = {
            "name": form_data.get('name', ''),
            "education": form_data.get('education', ''),
            "field": form_data.get('field', ''),
            "skills": [s.strip() for s in form_data.get('skills', '').split(',') if s.strip()],
            "interests": form_data.get('interests', ''),
            "career_goals": form_data.get('career_goals', ''),
            "timeline": form_data.get('timeline', '')
        }
        return self.user_profile
    
    def get_analysis_results(self):
        if not self.user_profile:
            return None
        strengths, growth_areas = self.analyze_profile()
        career_suggestions = self.suggest_careers()
        all_skills = []
        for career in career_suggestions:
            all_skills.extend(career["skills"])
        resources = self.recommend_resources(all_skills)
        roadmap = self.create_roadmap(career_suggestions)
        advice = self.generate_advice()
        return {
            'user_profile': self.user_profile,
            'strengths': strengths,
            'growth_areas': growth_areas,
            'career_suggestions': career_suggestions,
            'recommended_skills': list(set(all_skills))[:8],
            'resources': resources['recommended'][:6],
            'roadmap': roadmap,
            'advice': advice,
            'analysis_date': datetime.now().strftime('%B %d, %Y')
        }

# Routes (identical to original app.py)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/assess', methods=['POST'])
def assess():
    advisor = WebCareerAdvisor()
    user_data = advisor.process_user_data(request.form)
    session['user_data'] = user_data
    results = advisor.get_analysis_results()
    if results:
        session['results'] = results
        return redirect(url_for('results'))
    else:
        return redirect(url_for('index', error='Please fill in all required fields'))

@app.route('/results')
def results():
    if 'results' not in session:
        return redirect(url_for('index'))
    return render_template('results.html', **session['results'])

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/clear')
def clear_session():
    session.clear()
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# Lightweight keep-alive/health endpoint (no design impact)
@app.route('/_keepalive')
def keepalive():
    return ('', 204)

# Career Pages
@app.route('/careers/technology')
def careers_tech():
    return render_template('careers_tech.html')

@app.route('/careers/business')
def careers_business():
    return render_template('careers_business.html')

@app.route('/careers/design')
def careers_design():
    return render_template('careers_design.html')

@app.route('/careers/security')
def careers_security():
    return render_template('careers_security.html')

# Resources Pages
@app.route('/resources/learning')
def learning_resources():
    return render_template('learning_resources.html')

@app.route('/resources/skills')
def skill_guides():
    return render_template('skill_guides.html')

@app.route('/resources/tips')
def career_tips():
    return render_template('career_tips.html')

# Additional Pages
@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Expose app for WSGI
if __name__ == '__main__':
    print('Starting backend app...')
    app.run(debug=True, host='0.0.0.0', port=5000)
