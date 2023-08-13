import re 
from colorama import fore
import requests

website = ""
resultado = requests.get(website)
content = resultado.text