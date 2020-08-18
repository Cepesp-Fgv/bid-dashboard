from flask import Flask, request, url_for, render_template
from config import APP_SECRET_KEY, APP_DEBUG, FLASK_ENV, AWS_QUICKSIGHT_USER_EMAIL
from quicksight import QuickSightClient
import os.path

application = Flask(__name__)
application.env = FLASK_ENV
application.secret_key = APP_SECRET_KEY
application.testing = APP_DEBUG


def dated_url_for(endpoint, root_path, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(root_path, endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)

    return url_for(endpoint, **values)


def asset_filter(fl, root_path):
    return dated_url_for('static', root_path, filename=fl)


def view_dashboard():
    dashboard_id = request.args.get('id')
    quicksight = QuickSightClient()
    user = quicksight.describe_user(AWS_QUICKSIGHT_USER_EMAIL)
    dashboard_embed_url = QuickSightClient().get_dashboard_embed_url(user['User']['Arn'], dashboard_id)

    return render_template("dashboard.html", dashboard_embed_url=dashboard_embed_url)


def view_index():
    return render_template("index.html")


application.add_template_filter(lambda fl: asset_filter(fl, application.root_path), "asset")

application.add_url_rule("/dashboards", "view_dashboard", view_dashboard)

application.add_url_rule("/bid-fgv", "index", view_index)

application.add_url_rule("/", "index", view_index)

if __name__ == "__main__":
    application.debug = APP_DEBUG
    application.run()
