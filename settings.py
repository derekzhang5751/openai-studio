import os
import sys

from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

load_dotenv()

# openai settings
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "you-will-not-guess")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
