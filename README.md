# Personality Prediction ML Project

**Live Application:** [https://personality-2-ktty.onrender.com/](https://personality-2-ktty.onrender.com/)

This project predicts whether a person is an **Introvert** or **Extrovert** based on various behavioral traits such as time spent alone, stage fear, social event attendance, and more. It uses a Machine Learning model deployed via a Django web application.

## Model Details
- The model takes 7 features to determine the personality class.
- **Accuracy**: ~85% (This metric is an approximate baseline based on validation sets).

## Features Used
1. Time spent Alone
2. Stage fear
3. Social event attendance
4. Going outside
5. Drained after socializing
6. Friends circle size
7. Post frequency

## Local Setup

Follow these steps to set up and run the application locally on your machine:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ramuuzz/personality.git
   cd personality
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:8000/`.
