To run the app:

1. Make sure python is installed
2. Create virtual environment: python.exe -m venv 
3. Activate virtual environment: venv/scripts/Activate
4. Install dependencies: pip install -r requirements.txt
5. Run application: flask run

File Structure:
1. app.py : entrypoint to the app
2. models.py : classes and logic for AVLTree and its nodes
3. requirements.txt : file listing the dependencies the app needs
4. views.py : routing for the HTTP requests from the client
5. static
    - fonts : icons file used
    - scripts/app_script.js : AJAX call to the API, logic to show the UI
6. content/site.css : styling for the app
7. templates : Jinja templates for the HTML used in the UI