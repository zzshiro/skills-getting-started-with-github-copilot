# Mergington High School Activities API

The Mergington High School Activities API is a simple FastAPI web application that allows students to view and sign up for extracurricular activities. It consists of a Python FastAPI backend serving both API endpoints and static HTML/CSS/JavaScript frontend files.

**Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.**

## Working Effectively

### Prerequisites and Dependencies
- Python 3.12+ is required (check with `python --version`)
- Install dependencies: `pip install -r requirements.txt`
  - Installs: fastapi, uvicorn
  - NEVER CANCEL: Installation takes 15-30 seconds. Set timeout to 300+ seconds.

### Running the Application
- Start the server: `python -m uvicorn src.app:app --reload --host 0.0.0.0 --port 8000`
  - NEVER CANCEL: Server starts in 3-5 seconds. Set timeout to 60+ seconds for safety.
  - Server runs on http://localhost:8000
  - Auto-reload is enabled for development

### Validation and Testing
**CRITICAL**: Always manually validate changes by testing complete user scenarios.

#### API Testing
- Test activities endpoint: `curl -s http://localhost:8000/activities | python -m json.tool`
- Test signup endpoint: `curl -s -X POST "http://localhost:8000/activities/Chess%20Club/signup?email=test@mergington.edu"`
- Test error handling: `curl -s -X POST "http://localhost:8000/activities/Invalid%20Activity/signup?email=test@mergington.edu"` (should return 404)
- Test duplicate signup: Try signing up the same email twice (should return 400)
- View API documentation: http://localhost:8000/docs (interactive Swagger UI)
- Alternative docs: http://localhost:8000/redoc

#### Web Interface Testing
- Access main page: http://localhost:8000/ (redirects to static/index.html)
- Direct static access: http://localhost:8000/static/index.html
- **MANUAL VALIDATION REQUIRED**: Always test the complete user workflow:
  1. Load the webpage and verify activities display
  2. Fill out the signup form with a test email
  3. Submit the form and verify success message appears
  4. Refresh activities list to confirm participant count updated

### Application Structure
- `src/app.py` - Main FastAPI application with API endpoints
- `src/static/` - Frontend web interface files
  - `index.html` - Main webpage
  - `styles.css` - CSS styling
  - `app.js` - JavaScript for dynamic functionality
- `requirements.txt` - Python dependencies
- `.devcontainer/` - VS Code development container configuration

## Important Constraints and Limitations

### Data Storage
- All data is stored in memory (Python dictionaries)
- Data resets when server restarts
- No persistent database or file storage

### Build and Testing
- **NO BUILD STEP REQUIRED** - Python application runs directly
- **NO FORMAL TEST SUITE** - No pytest, unittest, or other testing framework
- **NO LINTING TOOLS** - No flake8, black, pylint, or mypy configured
- Always manually test functionality after making changes

### Common Issues
- The src/README.md incorrectly states `python app.py` - use uvicorn command instead
- Server must be stopped (Ctrl+C) before making significant changes to avoid file conflicts
- Static files are served from `/static/` path, not root

## Development Workflow

### Making Changes
1. Stop the running server (Ctrl+C if running)
2. Make your code changes
3. Start server: `python -m uvicorn src.app:app --reload --host 0.0.0.0 --port 8000`
4. **ALWAYS test both API and web interface manually**
5. Verify no console errors in browser developer tools

### Key Files to Monitor
- When changing API logic: Always test with both curl commands and web interface
- When changing static files: Always test web interface in browser
- When adding new activities: Update the activities dictionary in src/app.py

## Common Tasks and Quick Reference

### Repository Root Contents
```
.devcontainer/          # VS Code dev container config
.github/               # GitHub workflows and steps
.vscode/               # VS Code debugging configuration
src/                   # Application source code
  app.py              # Main FastAPI application
  static/             # Web interface files
  README.md           # Application documentation
requirements.txt       # Python dependencies
README.md             # Repository overview
LICENSE               # MIT license
```

### API Endpoints Reference
- `GET /` - Redirects to static/index.html
- `GET /activities` - Returns all activities with participant counts
- `POST /activities/{activity_name}/signup?email={email}` - Sign up for activity
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation
- `GET /static/*` - Static file serving (HTML, CSS, JS)

### Default Activities Data
```json
{
  "Chess Club": {
    "description": "Learn strategies and compete in chess tournaments",
    "schedule": "Fridays, 3:30 PM - 5:00 PM", 
    "max_participants": 12,
    "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
  },
  "Programming Class": {
    "description": "Learn programming fundamentals and build software projects",
    "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
    "max_participants": 20, 
    "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
  },
  "Gym Class": {
    "description": "Physical education and sports activities",
    "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
    "max_participants": 30,
    "participants": ["john@mergington.edu", "olivia@mergington.edu"]
  }
}
```

## Development Environment

### VS Code Configuration
- Debug configuration available in `.vscode/launch.json`
- Launch configuration: "Launch Mergington WebApp" 
- Uses uvicorn module with `src.app:app` and `--reload` flag

### Dev Container
- Python 3.13 development container configured (devcontainer uses Python 3.13, but 3.12+ is sufficient)
- Auto-installs requirements.txt on container creation
- Port 8000 forwarded automatically
- GitHub Copilot extension pre-installed

## Critical Reminders
- **NEVER CANCEL** dependency installation - allow full 300+ seconds (typically completes in 15-30 seconds)
- **ALWAYS** manually test both API endpoints and web interface after changes
- **NO BUILD PROCESS** exists - application runs directly with uvicorn
- **NO AUTOMATED TESTS** - rely on manual validation
- Data persists only during server runtime - restarts reset all data
- Use browser developer tools to check for JavaScript errors in web interface
- **ALWAYS** test error scenarios: invalid activity names, duplicate signups, malformed requests