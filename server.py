import subprocess

from flask import Flask, request

app = Flask(__name__)


@app.route("/run")
def run():
    """User-controlled command executed through a shell (fixture for a blocking finding)."""
    cmd = request.args.get("cmd", "")
    return subprocess.check_output(cmd, shell=True)
