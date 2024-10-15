import web

urls = (
    '/', 'hello'
)

render = web.template.render('templates')

app = web.application(urls, globals())

class hello:
    def GET(self):
        return render.index()

if __name__ == "__main__":
    app.run()
