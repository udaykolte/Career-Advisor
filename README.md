# 🎯 Career & Skills Advisor

A personalized career guidance tool for students and young professionals to discover career paths, develop skills, and create actionable learning roadmaps.

## 🌟 Features

- **Personalized Career Analysis**: Get career suggestions based on your background, skills, and interests
- **Skills Gap Analysis**: Identify your strengths and areas for growth  
- **Free Learning Resources**: Curated list of high-quality, free online courses and tutorials
- **3-6 Month Roadmaps**: Step-by-step learning plans tailored to your goals
- **Motivational Guidance**: Practical advice to keep you motivated throughout your journey

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Terminal/Command Prompt

### Installation & Usage

1. **Clone or Download the Project**
   ```bash
   git clone https://github.com/yourusername/career-skills-advisor.git
   cd career-skills-advisor
   ```

2. **Run the Career Advisor**
   ```bash
   python src/career_advisor.py
   ```

3. **Follow the Interactive Prompts**
   - Enter your name, education level, and field of study
   - List your current skills (comma-separated)
   - Share your interests and career goals
   - Specify your timeline for achieving goals

4. **Get Your Personalized Report**
   The tool will provide:
   - Career suggestions matched to your profile
   - Skills you should develop
   - Free learning resources
   - A detailed 3-6 month roadmap
   - Motivational tips

## 📋 Example Output

```
🎯 YOUR PERSONALIZED CAREER ANALYSIS
============================================================

👋 Hello Sarah!
Analysis Date: September 12, 2025

💪 YOUR STRENGTHS:
  ✓ Strong skill foundation
  ✓ Technical aptitude

🎯 CAREER SUGGESTIONS:
  1. Software Developer
     Key Skills: Python, JavaScript, Git, Problem Solving
  2. Data Scientist  
     Key Skills: Python, Statistics, Machine Learning, SQL

🛠️ RECOMMENDED SKILLS TO DEVELOP:
  • Python
  • JavaScript  
  • Git
  • Problem Solving
  • Statistics
  • Machine Learning

📚 FREE LEARNING RESOURCES:
  • freeCodeCamp - Complete web development curriculum
  • Codecademy - Interactive coding lessons
  • Kaggle Learn - Free micro-courses in data science
  • YouTube - Vast collection of tutorial videos

🗓️ YOUR 6-MONTH ROADMAP:

  Month 1-2: Foundation Building
    - Complete beginner courses in your chosen field
    - Set up learning routine (2-3 hours daily)
    - Join relevant online communities
    - Create learning portfolio/project folder

  Month 3-4: Skill Development  
    - Work on 2-3 practical projects
    - Network with professionals in your field
    - Attend virtual meetups or webinars
    - Update LinkedIn profile and resume

  Month 5-6: Application & Growth
    - Apply skills to real-world problems
    - Seek internships or volunteer opportunities
    - Build portfolio website or showcase
    - Start applying for entry-level positions

💫 MOTIVATION TIP:
  🚀 Remember: Every expert was once a beginner. Start where you are, use what you have!

🎉 You're ready to start your journey! Good luck, Sarah!
============================================================
```

## 🎯 Supported Career Paths

The advisor currently provides guidance for careers in:

### Technology
- Software Developer
- Data Scientist  
- Web Developer
- DevOps Engineer

### Business
- Product Manager
- Digital Marketing Specialist
- Business Analyst

### Design
- UX/UI Designer
- Graphic Designer

## 📚 Resource Categories

The tool recommends resources from these categories:
- **Programming**: freeCodeCamp, Codecademy, Python.org
- **Data Science**: Kaggle Learn, Coursera, StatQuest
- **Design**: Figma Academy, Adobe Tutorials, Dribbble  
- **Business**: Google Digital Marketing, HubSpot Academy
- **General**: LinkedIn Learning, YouTube, edX

## 🛠️ Project Structure

```
career-skills-advisor/
├── src/
│   └── career_advisor.py    # Main application logic
├── tests/                   # Test files (coming soon)
├── docs/                    # Documentation
├── README.md               # This file
├── requirements.txt        # Python dependencies
└── .gitignore             # Git ignore rules
```

## 🔧 Customization

You can easily extend the Career Advisor by:

1. **Adding New Career Paths**: Edit the `career_data` dictionary in `career_advisor.py`
2. **Updating Resources**: Modify the `resources` dictionary in the `recommend_resources()` method
3. **Customizing Roadmaps**: Adjust the roadmap structure in `create_roadmap()`
4. **Adding Analysis Logic**: Enhance the `analyze_profile()` method

## 🤝 Contributing

We welcome contributions! Here are ways you can help:

- Add new career paths and skills
- Improve the analysis algorithm
- Add more learning resources
- Create unit tests
- Improve documentation
- Report bugs or suggest features

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🎉 About

Created to help students and young professionals make informed career decisions and develop practical skills through free, accessible resources.

**Target Audience**: Students, recent graduates, and young professionals looking for career guidance and skill development.

**Philosophy**: Everyone deserves access to quality career guidance, regardless of their background or financial situation.

---

**Happy Learning! 🚀**

*Remember: Your career journey is unique. Use this tool as a starting point, but always trust your instincts and passion.*