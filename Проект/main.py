from flask import Flask, render_template
import random
import os

app = Flask(__name__)

# Допустим, наши мемы находятся в папке static/images
IMAGE_DIR = 'static/images'
IMAGES = [os.path.join(IMAGE_DIR, file) for file in os.listdir(IMAGE_DIR)]

@app.route('/')
def show_random_meme():
    # Выбираем случайный мем
    meme_path = random.choice(IMAGES)
    return render_template('index.html', meme=meme_path)

if __name__ == '__main__':
    app.run(debug=True)