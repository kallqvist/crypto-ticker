import os
import services

if __name__ == '__main__':
	host = os.environ.get('API_HOST', '0.0.0.0')
	port = int(os.environ.get('API_PORT', '5000'))
	debug = bool(os.environ.get('API_DEBUG', 'False').lower() == 'true')
	# services.scheduler.start()
	services.app.run(host=host, port=port, debug=debug)
