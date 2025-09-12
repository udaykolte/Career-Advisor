#!/usr/bin/env python3
"""
Personalized Career and Skills Advisor
A tool to help students and young professionals discover career paths and develop skills.
"""

import json
from typing import Dict, List, Tuple
from datetime import datetime

class CareerAdvisor:
    def __init__(self):
        self.user_profile = {}
        self.career_data = self._load_career_data()
        
    def _load_career_data(self) -> Dict:
        """Load predefined career paths and skills data."""
        return {
            "tech": {
                "careers": [
                    {"name": "Software Developer", "skills": ["Python", "JavaScript", "Git", "Problem Solving"]},
                    {"name": "Data Scientist", "skills": ["Python", "Statistics", "Machine Learning", "SQL"]},
                    {"name": "Web Developer", "skills": ["HTML", "CSS", "JavaScript", "React", "Node.js"]},
                    {"name": "DevOps Engineer", "skills": ["Linux", "Docker", "Kubernetes", "AWS", "CI/CD"]}
                ]
            },
            "business": {
                "careers": [
                    {"name": "Product Manager", "skills": ["Strategy", "Analytics", "Communication", "Agile"]},
                    {"name": "Digital Marketing", "skills": ["SEO", "Content Marketing", "Analytics", "Social Media"]},
                    {"name": "Business Analyst", "skills": ["Excel", "SQL", "Process Mapping", "Requirements Analysis"]}
                ]
            },
            "design": {
                "careers": [
                    {"name": "UX/UI Designer", "skills": ["Figma", "User Research", "Prototyping", "Design Systems"]},
                    {"name": "Graphic Designer", "skills": ["Adobe Creative Suite", "Typography", "Branding", "Layout"]}
                ]
            }
        }
    
    def collect_user_info(self):
        """Collect user background information."""
        print("🎯 Welcome to Your Personal Career & Skills Advisor!")
        print("=" * 50)
        
        self.user_profile["name"] = input("What's your name? ")
        self.user_profile["education"] = input("Current education level (e.g., High School, Bachelor's, etc.): ")
        self.user_profile["field"] = input("Field of study/work (if any): ")
        
        print("\n📚 Current Skills (separate with commas):")
        skills_input = input("List your current skills: ")
        self.user_profile["skills"] = [skill.strip() for skill in skills_input.split(",") if skill.strip()]
        
        print("\n🎯 Interests & Goals:")
        self.user_profile["interests"] = input("What areas interest you most? ")
        self.user_profile["career_goals"] = input("What are your career goals? ")
        self.user_profile["timeline"] = input("When do you want to achieve these goals? (e.g., 1 year, 3 years): ")
        
        print(f"\nThanks {self.user_profile['name']}! Let me analyze your profile...")
    
    def analyze_profile(self) -> Tuple[List[str], List[str]]:
        """Analyze user profile to identify strengths and growth areas."""
        strengths = []
        growth_areas = []
        
        # Basic analysis based on skills and interests
        if len(self.user_profile["skills"]) >= 3:
            strengths.append("Strong skill foundation")
        
        if any(tech_skill in " ".join(self.user_profile["skills"]).lower() 
               for tech_skill in ["python", "javascript", "programming", "coding"]):
            strengths.append("Technical aptitude")
        
        if "communication" in self.user_profile["interests"].lower():
            strengths.append("Communication-oriented")
            
        # Suggest growth areas
        growth_areas = ["Networking", "Industry Knowledge", "Practical Experience", "Soft Skills"]
        
        return strengths, growth_areas
    
    def suggest_careers(self) -> List[Dict]:
        """Suggest relevant career paths based on user profile."""
        suggested_careers = []
        user_interests = self.user_profile["interests"].lower()
        user_skills = " ".join(self.user_profile["skills"]).lower()
        
        # Match careers based on interests and skills
        for category, data in self.career_data.items():
            if category in user_interests or any(skill.lower() in user_skills 
                                               for career in data["careers"] 
                                               for skill in career["skills"]):
                suggested_careers.extend(data["careers"][:2])  # Top 2 from matching categories
        
        # If no matches, suggest popular beginner-friendly careers
        if not suggested_careers:
            suggested_careers = [
                {"name": "Software Developer", "skills": ["Python", "JavaScript", "Git", "Problem Solving"]},
                {"name": "Digital Marketing", "skills": ["SEO", "Content Marketing", "Analytics", "Social Media"]},
                {"name": "Data Analyst", "skills": ["Excel", "SQL", "Python", "Data Visualization"]}
            ]
        
        return suggested_careers[:3]  # Return top 3
    
    def recommend_resources(self, skills: List[str]) -> Dict[str, List[str]]:
        """Recommend free learning resources for required skills."""
        resources = {
            "Programming": [
                "freeCodeCamp - Complete web development curriculum",
                "Codecademy - Interactive coding lessons",
                "Python.org Tutorial - Official Python documentation"
            ],
            "Data Science": [
                "Kaggle Learn - Free micro-courses in data science",
                "Coursera Audit - Data Science courses (audit for free)",
                "YouTube: StatQuest - Statistics and ML concepts"
            ],
            "Design": [
                "Figma Academy - Free design tutorials",
                "Adobe Creative Cloud Tutorials - Free design resources",
                "Dribbble - Design inspiration and tutorials"
            ],
            "Business": [
                "Google Digital Marketing Courses - Free certification",
                "HubSpot Academy - Free marketing and sales courses",
                "Coursera Business Courses - Audit mode available"
            ],
            "General": [
                "LinkedIn Learning - Often free through libraries",
                "YouTube - Vast collection of tutorial videos",
                "edX - Free courses from top universities"
            ]
        }
        
        # Return relevant resources based on skills
        relevant_resources = []
        for skill in skills:
            skill_lower = skill.lower()
            if any(prog in skill_lower for prog in ["python", "javascript", "programming", "coding"]):
                relevant_resources.extend(resources["Programming"][:2])
            elif any(data in skill_lower for data in ["data", "analytics", "statistics", "ml"]):
                relevant_resources.extend(resources["Data Science"][:2])
            elif any(design in skill_lower for design in ["design", "figma", "ui", "ux"]):
                relevant_resources.extend(resources["Design"][:2])
            elif any(biz in skill_lower for biz in ["marketing", "business", "strategy"]):
                relevant_resources.extend(resources["Business"][:2])
        
        if not relevant_resources:
            relevant_resources = resources["General"][:3]
            
        return {"recommended": list(set(relevant_resources))}
    
    def create_roadmap(self, careers: List[Dict]) -> List[Dict]:
        """Create a 3-6 month skill development roadmap."""
        timeline = self.user_profile.get("timeline", "6 months")
        
        roadmap = [
            {
                "month": "Month 1-2",
                "focus": "Foundation Building",
                "tasks": [
                    "Complete beginner courses in your chosen field",
                    "Set up learning routine (2-3 hours daily)",
                    "Join relevant online communities",
                    "Create learning portfolio/project folder"
                ]
            },
            {
                "month": "Month 3-4", 
                "focus": "Skill Development",
                "tasks": [
                    "Work on 2-3 practical projects",
                    "Network with professionals in your field",
                    "Attend virtual meetups or webinars",
                    "Update LinkedIn profile and resume"
                ]
            },
            {
                "month": "Month 5-6",
                "focus": "Application & Growth",
                "tasks": [
                    "Apply skills to real-world problems",
                    "Seek internships or volunteer opportunities", 
                    "Build portfolio website or showcase",
                    "Start applying for entry-level positions"
                ]
            }
        ]
        
        return roadmap
    
    def generate_advice(self) -> str:
        """Generate personalized motivational advice."""
        advice_pool = [
            "🚀 Remember: Every expert was once a beginner. Start where you are, use what you have!",
            "💡 Focus on building one skill at a time. Consistency beats intensity every time.",
            "🎯 Set small, achievable daily goals. Progress compounds over time!",
            "🤝 Network genuinely - help others and opportunities will come your way.",
            "📈 Document your learning journey. Your future self will thank you!"
        ]
        
        import random
        return random.choice(advice_pool)
    
    def run_analysis(self):
        """Run complete career analysis and provide recommendations."""
        # Collect user information
        self.collect_user_info()
        
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
        
        # Display results
        self.display_results(strengths, growth_areas, career_suggestions, resources, roadmap, advice)
    
    def display_results(self, strengths, growth_areas, careers, resources, roadmap, advice):
        """Display formatted analysis results."""
        print("\n" + "="*60)
        print("🎯 YOUR PERSONALIZED CAREER ANALYSIS")
        print("="*60)
        
        print(f"\n👋 Hello {self.user_profile['name']}!")
        print(f"Analysis Date: {datetime.now().strftime('%B %d, %Y')}")
        
        print(f"\n💪 YOUR STRENGTHS:")
        for strength in strengths:
            print(f"  ✓ {strength}")
        
        print(f"\n🎯 CAREER SUGGESTIONS:")
        for i, career in enumerate(careers, 1):
            print(f"  {i}. {career['name']}")
            print(f"     Key Skills: {', '.join(career['skills'])}")
        
        print(f"\n🛠️ RECOMMENDED SKILLS TO DEVELOP:")
        unique_skills = list(set([skill for career in careers for skill in career['skills']]))
        for skill in unique_skills[:6]:  # Show top 6 skills
            print(f"  • {skill}")
        
        print(f"\n📚 FREE LEARNING RESOURCES:")
        for resource in resources["recommended"][:5]:  # Show top 5 resources
            print(f"  • {resource}")
        
        print(f"\n🗓️ YOUR {self.user_profile.get('timeline', '6-MONTH')} ROADMAP:")
        for phase in roadmap:
            print(f"\n  {phase['month']}: {phase['focus']}")
            for task in phase['tasks']:
                print(f"    - {task}")
        
        print(f"\n💫 MOTIVATION TIP:")
        print(f"  {advice}")
        
        print(f"\n🎉 You're ready to start your journey! Good luck, {self.user_profile['name']}!")
        print("="*60)

def main():
    """Main function to run the career advisor."""
    advisor = CareerAdvisor()
    try:
        advisor.run_analysis()
    except KeyboardInterrupt:
        print("\n\nThanks for using Career Advisor! Come back anytime. 👋")
    except Exception as e:
        print(f"\nOops! Something went wrong: {e}")
        print("Please try again or contact support.")

if __name__ == "__main__":
    main()