from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return ('''<html>
        <h1>hello</h1>
        <p>welcome everyone</p>
        <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Good_Food_Display_-_NCI_Visuals_Online.jpg/800px-Good_Food_Display_-_NCI_Visuals_Online.jpg'>
        <img src='https://th-thumbnailer.cdn-si-edu.com/gIxNZjXId6_6Suhxn6Sm9TeYgog=/800x800/filters:focal(960x640:961x641)/https://tf-cmsv2-smithsonianmag-media.s3.amazonaws.com/filer_public/f6/f3/f6f3493a-467f-4474-8c52-af5d021414b6/cat-5778777_1920.jpg'>
        <img src='https://img.freepik.com/free-photo/glowing-spaceship-orbits-planet-starry-galaxy-generated-by-ai_188544-9655.jpg'>
        <a href=\'food1\'>go to food1 page</a>
        <a href=\'food2\'>go to food2 page</a>
        </html>''')

@app.route('/food1')
def food1():
    return ('''<html>
        <h1></h1>
        <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Good_Food_Display_-_NCI_Visuals_Online.jpg/800px-Good_Food_Display_-_NCI_Visuals_Online.jpg'>
        <a href=\'home\'>go to home page</a>
        <a href=\'food2\'>go to food2 page</a>
        </html>''')

@app.route('/food2')
def food2():
    return ('''<html>
        <h1></h1>
        <img src='https://images.immediate.co.uk/production/volatile/sites/30/2023/06/Ultraprocessed-food-58d54c3.jpg?quality=90&resize=440,400'>
        <a href=\'home\'>go to home page</a>
        <a href=\'food1\'>go to food1 page</a>
        </html>''')
if __name__ == '__main__':
    app.run(debug=True)
