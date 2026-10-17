# Fendix release verification: repaired Semgrep rule

`app.py` decodes a JWT with the "none" algorithm, the shape `python-jwt-decode-no-verification` matches since v3.6.3. Static analysis fixture only; it is never run.
