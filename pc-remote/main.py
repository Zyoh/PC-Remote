import flask
import logging
import keyboard

# Logging
logging.basicConfig(encoding='utf-8', level=logging.INFO)

# Change these
HOTKEYS = [
	"F10", # Primary hotkey (top button)
	None, # Secondary hotkey (bottom button)
]

app = flask.Flask(__name__, template_folder=".")


@app.route("/", methods=["GET", "POST"])
def root():
	if flask.request.method == "POST":
		data = list(flask.request.form.keys())

		logging.debug(data)
		match data:
			case ["primary"]:
				logging.debug("Received primary action.")
				if key := HOTKEYS[0]:
					logging.info(f"Running primary action: {key}")
					keyboard.press_and_release(key)

			case ["secondary"]:
				logging.debug("Received secondary action.")
				if key := HOTKEYS[1]:
					logging.info(f"Running secondary action: {key}")
					keyboard.press_and_release(key)

			case _:
				logging.warning("Invalid POST data.")
				raise flask.abort(400)

	return flask.render_template("index.html")


def main():
	app.run("0.0.0.0", 27152, debug=False)


if __name__ == "__main__":
	main()
