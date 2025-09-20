#!/usr/bin/env python3
"""
Career & Skills Advisor Web Application
Flask-based web interface for personalized career guidance
"""

from flask import Flask, render_template, request, session, redirect, url_for
import sys
import os
from datetime import datetime

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Import our career advisor logic
from career_advisor import CareerAdvisor

app = Flask(__name__)
app.secret_key = 'career-advisor-secret-key-change-in-production'
# Configure for development - remove SERVER_NAME to avoid URL issues
# app.config['SERVER_NAME'] = 'localhost:5000'
# app.config['PREFERRED_URL_SCHEME'] = 'http'

class WebCareerAdvisor(CareerAdvisor):
    """Web-compatible version of the CareerAdvisor"""
    
    def __init__(self):
        super().__init__()
    
    def process_user_data(self, form_data):
        """Process user data from web form"""
        self.user_profile = {
            "name": form_data.get('name', ''),
            "education": form_data.get('education', ''),
            "field": form_data.get('field', ''),
            "skills": [skill.strip() for skill in form_data.get('skills', '').split(',') if skill.strip()],
            "interests": form_data.get('interests', ''),
            "career_goals": form_data.get('career_goals', ''),
            "timeline": form_data.get('timeline', '')
        }
        return self.user_profile
    
    def get_analysis_results(self):
        """Get complete analysis results for web display"""
        if not self.user_profile:
            return None
            
        # Perform analysis
        strengths, growth_areas = self.analyze_profile()
        career_suggestions = self.suggest_careers()
        
        # Get all required skills from suggested careers
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
            'recommended_skills': list(set(all_skills))[:8],  # Top 8 unique skills
            'resources': resources['recommended'][:6],  # Top 6 resources
            'roadmap': roadmap,
            'advice': advice,
            'analysis_date': datetime.now().strftime('%B %d, %Y')
        }

@app.route('/')
def index():
    """Home page with career assessment form"""
    return render_template('index.html')

@app.route('/assess', methods=['POST'])
def assess():
    """Process career assessment form"""
    # Create advisor instance
    advisor = WebCareerAdvisor()
    
    # Process form data
    user_data = advisor.process_user_data(request.form)
    
    # Store in session for results page
    session['user_data'] = user_data
    
    # Get analysis results
    results = advisor.get_analysis_results()
    
    if results:
        session['results'] = results
        return redirect(url_for('results'))
    else:
        return redirect(url_for('index', error='Please fill in all required fields'))

@app.route('/results')
def results():
    """Display career assessment results"""
    if 'results' not in session:
        return redirect(url_for('index'))
    
    return render_template('results.html', **session['results'])

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

@app.route('/clear')
def clear_session():
    """Clear session and restart"""
    session.clear()
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# Career Pages Routes
@app.route('/careers/technology')
def careers_tech():
    """Technology careers page"""
    return render_template('careers_tech.html')

@app.route('/careers/business')
def careers_business():
    """Business careers page"""
    return render_template('careers_business.html')

@app.route('/careers/design')
def careers_design():
    """Design careers page"""
    return render_template('careers_design.html')

@app.route('/careers/security')
def careers_security():
    """Security careers page"""
    return render_template('careers_security.html')

# Resources Pages Routes
@app.route('/resources/learning')
def learning_resources():
    """Learning resources hub page"""
    return render_template('learning_resources.html')

@app.route('/resources/skills')
def skill_guides():
    """Skill development guides page"""
    return render_template('skill_guides.html')

@app.route('/resources/tips')
def career_tips():
    """Career tips and advice page"""
    return render_template('career_tips.html')

# Additional Pages
@app.route('/blog')
def blog():
    """Blog page with career articles"""
    return render_template('blog.html')

@app.route('/contact')
def contact():
    """Contact page"""
    return render_template('contact.html')

if __name__ == '__main__':
    print("Starting Career & Skills Advisor Web Application...")
    print("Dashboard: http://localhost:5000")
    print("Ready to help users discover their career potential!")
    print()
    
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)
