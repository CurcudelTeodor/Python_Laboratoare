To run: `> python main.py table.json`

To generate documentation:
* `\Snake>` `pip install pdoc`
* `\Snake>` `.\\venv\Scripts\python.exe -m pdoc main.py game.py snake.py food.py gui.py settings.py --output-dir docs ` or simply
`python -m pdoc main.py game.py snake.py food.py gui.py settings.py --output-dir docs `
* `cd docs`
* `\Snake\docs>` `python -m httpserver` and go to `http://localhost:8000` in a web browser
* The previous step can be replaced with running the command `\Snake\docs> start index.html`.
The default web browser should be opened.

Note: 
1. In the 3rd step you can also configure the port on which the server will start by giving the command:
`python -m http.server 8080` for example in the `\Snake\docs>` folder. You can replace 8080 with your preferred port.
2. I denoted with `\Snake\docs>` the location where the command should be run.