# Sense Stock Insight with MyFi NewsSense Backend

This project combines a modern React frontend (Sense Stock Insight) with a powerful Flask backend (MyFi NewsSense) to provide financial news analysis and market insights.

## Project Structure

- **NHCEHACK/** - Backend Flask application with NLP analysis tools
- **sense-stock-insight/** - Frontend React application with modern UI

## Setup Instructions

### Backend Setup

1. Create a Python virtual environment:
   ```
   cd NHCEHACK
   python -m venv venv
   ```

2. Activate the virtual environment:
   - Windows:
     ```
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```
     source venv/bin/activate
     ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Setup environment variables:
   - Copy `.env.example` to `.env`
   - Fill in required API keys

### Frontend Setup

1. Install dependencies:
   ```
   cd sense-stock-insight
   npm install
   ```

2. Configure backend URL:
   - Edit `.env` file if needed, default is `http://localhost:5000`

## Running the Application

### Running the Backend

```
cd NHCEHACK
venv\Scripts\activate  # or source venv/bin/activate on macOS/Linux
python flask_app.py
```

The backend will run on `http://localhost:5000`.

### Running the Frontend

```
cd sense-stock-insight
npm run dev
```

The frontend will run on `http://localhost:5173`.

## Features

- Real-time financial news analysis
- Natural language question answering about market movements
- Interactive data visualization of market trends
- Sentiment analysis of news articles
- Support for multiple market entities (Nifty, SBI, HDFC, etc.)

## API Endpoints

The backend provides several API endpoints:

- `/api/chat` - Chat interface for questions and answers
- `/api/ask` - Submit a question and get analysis
- `/api/graph` - Get graph data for visualizations
- `/api/entities` - Get available market entities
- `/api/articles` - Get financial news articles
- `/api/suggestions` - Get suggested questions

## License

This project is intended for educational purposes.