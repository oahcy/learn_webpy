import web

urls = ('/hello','hello')

app = web.application(urls,globals())

class hello:
	def GET(self):
		client = [
		web.ctx.env.get('HTTP_REFERER',"google.com"),
		web.ctx.ip,
		web.ctx.host,
		web.ctx.status,
		web.ctx.headers
		]
		return client

if __name__ == "__main__":
	app.run()
