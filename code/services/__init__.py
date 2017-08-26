from flask import Flask
app = Flask(__name__)

# import all other services files here
import crypto_ticker
import crypto_rank
import fiat_ticker
