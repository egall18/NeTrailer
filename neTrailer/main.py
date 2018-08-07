import webapp2
import jinja2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
class MainPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('Templates/about.html')
        self.response.write(about_template.render())


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)