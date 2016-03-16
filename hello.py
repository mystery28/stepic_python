def  wsgi_application(environ, start_response):
	status = '200 OK'
	headers = [
		('Content-Type', 'text/plain')
	]

	body = [
		'%s=%s' % (key, value) for key, value in environ.items()
	]
	body = '\n'.join(body)

	start_response(status, headers )
	return [ body ]