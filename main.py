from setup import app, manager
from Users.controller import user_controller

app.register_blueprint(user_controller, url_prefix="/")
# app.register_blueprint(user_controller, subdomain="users", url_prefix="/")


if __name__ == "__main__":
    app.run(debug=True)
    # manager.run()