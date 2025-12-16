from flask import Flask, request, render_template, jsonify
from tracking import create_tables, log_visitor, log_event
from user_agents import parse

app = Flask(__name__)

# Create database tables when app starts
create_tables()


@app.route("/")
def home():
    user_agent = parse(request.headers.get('User-Agent'))

    device = user_agent.device.family
    browser = user_agent.browser.family
    page = "Home"

    log_visitor(page, device, browser)

    return render_template("index.html")


@app.route("/track-event")
def track_event():
    event_type = request.args.get("type")
    event_value = request.args.get("value")
    page = request.args.get("page")

    log_event(event_type, event_value, page)
    return jsonify({"status": "ok"})
if __name__ == "__main__":
    app.run(debug=True)