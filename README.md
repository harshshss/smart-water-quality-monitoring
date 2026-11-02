# Smart Water Quality Monitoring

A complete web application for monitoring water quality data across Northeast India. Built with React.js frontend and Flask Python backend.

## Features

- **Area Selection**: Dropdown to select different Northeast Indian areas
- **Real-time Data Display**: Shows water quality parameters (Turbidity, pH, TDS, Status)
- **Clean UI**: Modern, responsive design with glass-morphism effects
- **REST API**: Flask backend serving predefined water quality data
- **Responsive**: Works seamlessly on desktop and mobile devices

## Project Structure

```
smart-water-quality-monitoring/
├── backend/
│   ├── app.py              # Flask API server
│   └── requirements.txt    # Python dependencies
├── frontend/
│   ├── public/            # Static assets
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── types/         # TypeScript interfaces
│   │   └── App.tsx        # Main application
│   └── package.json       # Node.js dependencies
└── README.md              # This file
```

## Prerequisites

Before running this application, ensure you have the following installed:

- **Node.js** (version 16 or higher) - [Download here](https://nodejs.org/)
- **Python** (version 3.8 or higher) - [Download here](https://python.org/)
- **npm** or **yarn** (comes with Node.js)

## Installation & Setup

### 1. Clone/Navigate to the Project

```bash
# If you received this as a zip file, extract it
# Otherwise, navigate to the project directory
cd smart-water-quality-monitoring
```

### 2. Backend Setup (Flask)

```bash
# Navigate to backend directory
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Alternative: Create virtual environment (recommended)
python -m venv venv
# On Windows:
venv\\Scripts\\activate
# On macOS/Linux:
source venv/bin/activate

# Then install dependencies
pip install -r requirements.txt
```

### 3. Frontend Setup (React)

```bash
# Navigate to frontend directory (from project root)
cd frontend

# Install Node.js dependencies
npm install

# Alternative: Using yarn
yarn install
```

## Running the Application

### Start the Backend Server

```bash
# From the backend directory
cd backend

# Run the Flask server
python app.py
```

The backend server will start on `http://localhost:5000`

**Backend API Endpoints:**
- `GET /` - Health check
- `GET /api/areas` - Get all available areas
- `GET /api/water-quality/<area>` - Get water quality data for specific area
- `GET /api/water-quality` - Get all water quality data

### Start the Frontend Application

**Open a new terminal/command prompt** and run:

```bash
# From the frontend directory
cd frontend

# Start the React development server
npm start

# Alternative: Using yarn
yarn start
```

The frontend application will start on `http://localhost:3000` and should automatically open in your browser.

## Usage

1. **Start both servers** (backend on port 5000, frontend on port 3000)
2. **Open your browser** to `http://localhost:3000`
3. **Select an area** from the dropdown menu
4. **View water quality data** displayed in the table below
5. **Switch between areas** to see different water quality readings

## Available Areas

The application includes water quality data for the following Northeast Indian areas:

- Guwahati (Assam)
- Shillong (Meghalaya)
- Imphal (Manipur)
- Kohima (Nagaland)
- Aizawl (Mizoram)
- Agartala (Tripura)
- Itanagar (Arunachal Pradesh)
- Gangtok (Sikkim)

## Water Quality Parameters

- **Turbidity**: Measured in NTU (Nephelometric Turbidity Units)
- **pH Level**: Acidity/alkalinity scale (0-14)
- **TDS**: Total Dissolved Solids in ppm (parts per million)
- **Overall Status**: Excellent, Good, Fair, or Poor

## Troubleshooting

### Common Issues

1. **Port 3000 or 5000 already in use**:
   - Kill the process using the port or use different ports
   - For React: `PORT=3001 npm start`
   - For Flask: Modify `app.run(port=5001)` in app.py

2. **CORS errors**:
   - Ensure Flask-CORS is installed and configured (already included)

3. **API connection failed**:
   - Verify backend server is running on port 5000
   - Check that both frontend and backend are running simultaneously

4. **Python dependencies installation failed**:
   - Try creating a virtual environment first
   - Ensure pip is updated: `pip install --upgrade pip`

5. **Node.js dependencies installation failed**:
   - Clear npm cache: `npm cache clean --force`
   - Delete `node_modules` and `package-lock.json`, then run `npm install` again

### Development Notes

- **Frontend**: Built with Create React App and TypeScript
- **Backend**: Flask with CORS enabled for cross-origin requests
- **Data**: Static JSON data (easily replaceable with database)
- **Styling**: Modern CSS with glass-morphism effects and responsive design

## Production Deployment

For production deployment:

1. **Frontend**: Run `npm run build` and serve the `build` folder
2. **Backend**: Use a production WSGI server like Gunicorn
3. **Environment**: Set appropriate environment variables and remove debug mode

## License

This project is open source and available under the MIT License.

---

**Happy monitoring! 🌊📊**
