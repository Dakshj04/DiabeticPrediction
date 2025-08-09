# Diabetes Risk Prediction System

## Project Overview
A machine learning-based web application that predicts diabetes risk using clinical parameters. The system provides both a Flask-based web interface and a Streamlit dashboard for user interaction.

## Features
- **Dual Interface Options:**
  - Flask web application for traditional web access
  - Interactive Streamlit dashboard with real-time predictions
- **Machine Learning Integration:**
  - Pre-trained model for accurate diabetes risk assessment
  - Standardized data processing using sklearn's StandardScaler
- **User-Friendly Input:**
  - Eight clinical parameters for prediction
  - Instant results with probability scores
  - Visual feedback based on risk levels

## Technical Stack
- **Backend Framework:** Flask
- **Frontend:** HTML, CSS
- **Dashboard:** Streamlit
- **Machine Learning:** Scikit-learn
- **Data Processing:** Pandas, NumPy
- **Model Serialization:** Pickle

## Input Parameters
1. Pregnancies
2. Glucose Level
3. Blood Pressure
4. Skin Thickness
5. Insulin
6. BMI (Body Mass Index)
7. Diabetes Pedigree Function
8. Age

## Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/diabetes-prediction.git

# Navigate to project directory
cd diabetes-prediction

# Install required packages
pip install -r requirements.txt
```

## Usage
### Flask Application
```bash
python application.py
```
Access the web interface at `http://localhost:5000`

### Streamlit Dashboard
```bash
streamlit run app.py
```
Access the dashboard at `http://localhost:8501`

## Project Structure
```
diabetes-prediction/
├── models/
│   ├── modelForPrediction.pkl
│   └── standardScaler.pkl
├── templates/
│   ├── home.html
│   ├── index.html
│   └── single_prediction.html
├── application.py
├── app.py
└── README.md
```

## Model Information
- The prediction model is trained on the Pima Indians Diabetes Database
- Features are standardized using StandardScaler
- Model and scaler are serialized using pickle

## Performance Metrics
- Accuracy: [Add your model's accuracy]
- Precision: [Add precision score]
- Recall: [Add recall score]
- F1 Score: [Add F1 score]

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details

## Acknowledgments
- Dataset: Pima Indians Diabetes Database
- Contributors and maintainers

## Disclaimer
This tool is for educational purposes only and should not be used as a substitute for professional medical advice.

## Author
[Your Name]
[Your Email/Contact Information]
[Your LinkedIn Profile]