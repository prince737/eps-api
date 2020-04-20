from setup import app, manager
from Users.controller import user_controller
from Test.controller import test_controller
from Rout.controller import rout_controller

app.register_blueprint(test_controller, url_prefix="/test") #registeting test_controller blueprint with the main "app" and asking it to handle all url that begins with "/test". For eg: http://127.0.0.1/test/anythingcanbehere/orhere/orhere all such urls will go the test_conrtoller file. For now we just have to defined endpoints "test_get", "test_post". Anything else will result in 404 not fond error.
app.register_blueprint(user_controller, url_prefix="/")
app.register_blueprint(rout_controller, url_prefix="/rout")

if __name__ == "__main__":
  app.run(debug=True)
  #manager.run()