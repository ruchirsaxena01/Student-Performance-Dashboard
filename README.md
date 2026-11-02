EduAnalytics – Student Academic Performance Dashboard

Project ID: DA-003

About the Project

EduAnalytics is a data analysis and visualization project that explores student academic performance using Python. It provides an interactive dashboard to understand marks, attendance, study habits, and pass/fail distribution.

Objectives

- Analyze student academic performance.
- Compare average marks across different subjects.
- Study attendance and daily study hours.
- Calculate average marks and pass percentage.
- Explore relationships between academic variables using correlation.
- Present insights through an interactive dashboard.

Technologies Used

- Python
- Pandas
- NumPy
- Plotly
- Streamlit
- Google Colab

Dashboard Features

1. Overview: Key performance indicators, charts, and student records.
2. Subject Analysis: Subject-wise average marks and performance comparison.
3. Student Insights: Pass/fail distribution and top-performing students.
4. Correlation Analysis: Interactive correlation heatmap.
5. Filters: Filter records by attendance and result.
6. Search and Download: Search student IDs and download filtered records as CSV.

Dataset

The project uses 500 synthetic student records. The dataset includes attendance, daily study hours, marks in four subjects, average marks, and result.

Note: This is synthetic data created for educational purposes. It does not represent actual students or institutional records.

How to Run the Project

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate

4. Install the required libraries:

pip install -r requirements.txt

5. Run the dashboard:

streamlit run app.py

Project Structure

Student-Performance-Dashboard/
│
├── app.py
├── DA003_student_data.csv
├── requirements.txt
└── README.md

Important Findings

- Average marks across all subjects: approximately 59.40.
- Computer has the highest subject average.
- Mathematics has the lowest subject average.
- Overall pass percentage: 74.6%.
- Study hours and attendance show positive correlations with average marks in this synthetic dataset.

Conclusion

EduAnalytics demonstrates how Python-based data analysis and visualization can help explore academic performance patterns. The dashboard makes the results easier to understand through interactive charts, filters, and student records.

Developed as part of the DA-003 academic project.