import waitress
import sys

sys.path.insert(0, './src')

import main

waitress.serve(main.app, host="0.0.0.0", port=8000)
