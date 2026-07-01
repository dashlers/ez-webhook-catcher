import os
import subprocess
from flask import Flask, abort

app = Flask(__name__)

# Define the folder containing your shell scripts
SCRIPTS_DIR = os.path.abspath("./scripts")
LISTEN_PORT = 30080

@app.route('/<script_name>.sh', methods=['POST'])
def catch_webhook(script_name):
    # Reconstruct the full file name
    filename = f"{script_name}.sh"
    script_path = os.path.join(SCRIPTS_DIR, filename)
    
    # Security check: Prevent directory traversal attacks (e.g., ../../../etc/passwd)
    if not os.path.abspath(script_path).startswith(SCRIPTS_DIR):
        abort(403)
        
    # Check if the script exists and is a file
    if not os.path.isfile(script_path):
        abort(404)
        
    try:
        # Popen runs the script asynchronously in the background.
        # This allows the Flask app to instantly return a 200 OK status
        # without waiting for the shell script to finish executing.b
        subprocess.Popen(["sh", script_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return "OK", 200
    except Exception:
        abort(500)

if __name__ == '__main__':
    # Ensure the scripts folder exists at startup
    if not os.path.exists(SCRIPTS_DIR):
        os.makedirs(SCRIPTS_DIR)
        print(f"Created scripts directory at: {SCRIPTS_DIR}")
        
    # Launch webserver
    app.run(host='0.0.0.0', port=LISTEN_PORT)
