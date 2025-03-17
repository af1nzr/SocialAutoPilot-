<h1 align="center">SocialAutoPilot</h1>
<p align="center">
    AI-powered automation tool for Instagram & Facebook
</p>

<p align="center">
    <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
    <img src="https://img.shields.io/badge/Framework-PyQt5-orange.svg" alt="PyQt5">
    <img src="https://img.shields.io/badge/Automation-Selenium-green.svg" alt="Selenium">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License">
</p>

---

## **Overview**
SocialAutoPilot is a Python-based automation tool designed to streamline social media interactions on Instagram and Facebook. It features a **PyQt-based GUI** for easy task selection and uses **Selenium** to automate engagement activities such as liking posts, commenting, following users, and sending personalized messages. Execution limits are implemented to ensure responsible automation.

---

## **Key Features**
- Multi-Platform Support – Automate interactions on Instagram and Facebook  
- GUI-Based Control – Built with PyQt5 for an intuitive user experience  
- Execution Rate Limiting – Prevent excessive actions and reduce detection risks  
- Logging & Analytics – Track automation activities for better optimization  

---

## **Installation & Setup**
### **Prerequisites**
Ensure the following dependencies are installed:
- Python 3.8+
- Google Chrome (latest version)
- Chrome WebDriver (compatible with the installed Chrome version)

### **Installation Steps**
```sh

# Clone the repository
git clone https://github.com/yourusername/SocialAutoPilot.git
cd SocialAutoPilot

# Set up a virtual environment

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies

pip install -r requirements.txt

# Run the application

python main.py

Usage Guide

Launch the GUI by running main.py
Select the target platform (Instagram or Facebook)
Enable desired automation features
Click Submit to start automation
Technologies & Frameworks Used
Python – Core programming language
Selenium – Browser automation for web interaction
PyQt5 – GUI framework for a user-friendly experience
SQLite – Local database for logging interactions
TensorFlow Lite – Optional AI-driven engagement
Ethical Considerations & Disclaimer
SocialAutoPilot is intended strictly for educational and research purposes. Automating social media interactions may violate platform policies. Users are responsible for ensuring compliance with the applicable terms of service. The author assumes no responsibility for misuse.

Future Enhancements

AI-based engagement prediction for optimized automation strategies
Cloud-based deployment for remote automation
Machine learning-based interaction patterns to reduce detection risks

License

This project is licensed under the MIT License. See LICENSE.md for details.
