import logging ,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_LEVEL = logging.INFO
LOG_TYPES = {
	'transaction':'transactions.log',
	'access':'access.log'
}

DATABASE = {
	'engine':'file_storage',
	'name':'accounts',
	'path':"%s/db"% BASE_DIR
}

LOG_PATH = {
	'path':"%s/log"% BASE_DIR
}


TRANSACTION_TYPE = {
    'repay':{'action':'plus', 'interest':0},
    'withdraw':{'action':'minus', 'interest':0.05},
    'transfer':{'action':'minus', 'interest':0.05},
    'consume':{'action':'minus', 'interest':0},

}