def app(environ, start_response):
	status = '200 OK'
	headers = [('Content-Type', 'text/plain')]

	lines = []
	query_body = environ['QUERY_STRING'].split("&")
	for item in query_body:
		lines.append(item)
	lines = "\n".join(lines)

	start_response(status, headers)
	return [ lines ]
