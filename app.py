from flask import Flask, render_template, request
from forms import filmForm
import movieRcomndr as mR
app = Flask(__name__)

app.config['SECRET_KEY'] = '3f3b1eda2b930950d37bcbc3b11c94d4'


@app.route('/')
def main():
    form = filmForm()
    return render_template('main.html', title='Main')


@app.route('/results', methods=['POST'])
def show_results():
    favMovie = request.form['favMovie']
    movies = mR.getRecommendations(favMovie)
    return render_template('results.html', favMovie=movies)



if __name__ == '__main__':
    app.run(debug = True)