# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This is a full-stack water quality monitoring application with a React TypeScript frontend and Flask Python backend. The application displays water quality data for Northeast Indian areas including turbidity, pH, TDS measurements, and overall status ratings.

## Essential Commands

### Development Setup
```powershell
# Install backend dependencies
cd backend
pip install -r requirements.txt

# Install frontend dependencies  
cd frontend
npm install
```

### Running the Application
```powershell
# Start the Flask backend (port 5000)
cd backend
python app.py

# Start the React frontend (port 3000) - in new terminal
cd frontend
npm start
```

### Building for Production
```powershell
# Build the React app
cd frontend
npm run build
```

### Testing
```powershell
# Run React tests
cd frontend
npm test

# Run the project setup verification
python test_setup.py
```

### Linting and Code Quality
```powershell
# TypeScript type checking
cd frontend
npx tsc --noEmit

# ESLint is configured via Create React App
npm run build  # Will show linting errors
```

## Architecture

### Full-Stack Structure
- **Frontend**: React 19.1 with TypeScript, Create React App
- **Backend**: Flask 2.3.3 with Flask-CORS, serving REST API
- **Data**: Static JSON data stored in Flask app (easily replaceable with database)
- **Communication**: Frontend consumes REST API at `http://localhost:5000/api`

### Frontend Architecture (`frontend/src/`)
```
src/
├── App.tsx                 # Main application component with state management
├── types/
│   └── WaterQuality.ts    # TypeScript interfaces for data contracts  
└── components/
    ├── Header.tsx         # Application header
    ├── AreaSelector.tsx   # Dropdown for selecting monitoring areas
    ├── WaterQualityTable.tsx  # Data table display component
    └── Footer.tsx         # Application footer
```

**Key Frontend Patterns:**
- React functional components with hooks
- `useState` for local state management (areas, selected area, water quality data, loading, error states)
- `useEffect` for side effects (API calls)  
- TypeScript interfaces for type safety
- Component-specific CSS files for styling
- API calls using native `fetch()` with async/await

### Backend Architecture (`backend/`)
```
backend/
├── app.py              # Flask application with API routes
└── requirements.txt    # Python dependencies
```

**API Endpoints:**
- `GET /` - Health check
- `GET /api/areas` - Returns list of available monitoring areas
- `GET /api/water-quality/<area>` - Returns water quality data for specific area
- `GET /api/water-quality` - Returns all water quality data

**Backend Patterns:**
- Flask with CORS enabled for cross-origin requests
- Static data storage in Python dictionary (production should use database)
- RESTful API design with proper HTTP status codes
- JSON responses with error handling

### Data Flow
1. App loads → Fetches available areas from `/api/areas`
2. User selects area → Triggers API call to `/api/water-quality/{area}`  
3. Data received → Updates component state and renders table
4. Error handling for network failures and invalid areas

### State Management
The app uses React's built-in state management:
- `areas`: Array of available monitoring areas
- `selectedArea`: Currently selected area string  
- `waterQualityData`: Current water quality measurements object
- `loading`: Boolean for loading states
- `error`: String for error messages

### Styling Approach
- Component-scoped CSS files
- Glass-morphism design effects
- Responsive design for mobile and desktop
- Status-based color coding (excellent/good/fair/poor)

## Development Notes

### TypeScript Configuration
- Strict mode enabled with comprehensive type checking
- Target ES5 for broad browser compatibility  
- React JSX transformation configured
- No emit mode (handled by Create React App)

### Frontend Development
- Create React App provides build tooling, dev server, and testing
- ESLint configuration extends react-app rules
- Hot reloading enabled in development
- Production builds are optimized and minified

### Backend Development  
- Flask development server with debug mode enabled
- CORS configured for frontend communication
- Simple in-memory data storage (replace with database for production)

### Testing Setup
- Jest and React Testing Library configured via Create React App
- `test_setup.py` provides project structure validation
- Component tests can be added in `*.test.tsx` files

### Production Considerations
- Frontend: Build with `npm run build` and serve static files
- Backend: Use production WSGI server (Gunicorn, uWSGI)
- Environment variables for API URLs and configuration
- Database integration for persistent data storage
- API authentication and rate limiting for production use

### Adding New Features
When adding new water quality parameters:
1. Update `WaterQualityData` interface in `types/WaterQuality.ts`
2. Modify backend data structure in `app.py`  
3. Update `WaterQualityTable.tsx` component to display new parameters
4. Add corresponding CSS styles for new parameter display

### Common Development Tasks
- **Add new monitoring area**: Update `water_quality_data` dictionary in `backend/app.py`
- **Modify styling**: Edit component-specific CSS files in `src/components/`
- **Add API endpoint**: Create new route function in `backend/app.py` with Flask decorators
- **Update data structure**: Modify TypeScript interface and backend data format simultaneously
