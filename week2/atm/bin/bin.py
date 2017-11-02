import sys ,os
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,project_path)
#print(sys.path)
from logger.logger import log

log()

print(__file__)