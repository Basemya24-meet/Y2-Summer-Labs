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
        <h1></h1>
        <a href=\'food1\'>food1 page</a>
        <h1></h1>
        <a href=\'food2\'>food2 page</a>
        <h1></h1>
        <a href=\'food3\'>food3 page</a>
        <h1></h1>
        <a href=\'pet1\'>pet1 page</a>
        <h1></h1>
        <a href=\'pet2\'>pet2 page</a>
        <h1></h1>
        <a href=\'pet3\'>pet3 page</a>
        <h1></h1>
        <a href=\'space1\'>space1 page</a>
        <h1></h1>
        <a href=\'space2\'>space2 page</a>
        <h1></h1>
        <a href=\'space3\'>space3 page</a>
        </html>''')

@app.route('/food1')
def food1():
    return ('''<html>
        <h1></h1>
        <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Good_Food_Display_-_NCI_Visuals_Online.jpg/800px-Good_Food_Display_-_NCI_Visuals_Online.jpg'>
        <a href=\'home\'>go to home page</a>
        </html>''')

@app.route('/food2')
def food2():
    return ('''<html>
        <h1></h1>
        <img src='https://images.immediate.co.uk/production/volatile/sites/30/2023/06/Ultraprocessed-food-58d54c3.jpg?quality=90&resize=440,400'>
        <a href=\'home\'>go to home page</a>
        </html>''')

@app.route('/food3')
def food3():
    return ('''<html>
        <h1></h1>
        <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9eeQS_UFyg20y08MiH33Vsacq3vX1RNJOkg&s'>
        <a href=\'home\'>go to home page</a>
        </html>''')

@app.route('/pet1')
def pet1():
    return ('''<html>
        <h1></h1>
        <img src='https://hips.hearstapps.com/hmg-prod/images/low-maintenance-pets-hamsters-in-hand-1643914343.jpg?fill=16:9'>
        <a href=\'home\'>go to home page</a>
        </html>''')

@app.route('/pet2')
def pet2():
    return ('''<html>
        <h1></h1>
        <img src='https://www.scripps.org/sparkle-assets/images/dogs_cats_rabbits_pets_1200x750-e017741227f7382c3ba7aaeb27b28297.jpg'>
        <a href=\'home\'>go to home page</a>
        </html>''')

@app.route('/pet3')
def pet3():
    return ('''<html>
        <h1></h1>
        <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS7BSnxk2PA5pzymv7-5RgYRHY6DtBM2njNgg&s'>
        <a href=\'home\'>go to home page</a>
        </html>''')

@app.route('/space1')
def space1():
    return ('''<html>
        <h1></h1>
        <img src='https://c02.purpledshub.com/uploads/sites/41/2019/06/GettyImages-497707356-e722dce.jpg'>
        <a href=\'home\'>go to home page</a>
        </html>''')

@app.route('/space2')
def space2():
    return ('''<html>
        <h1></h1>
        <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVkfw-0xVDvfDGzx1aeauP5DtYIHKgxY29FQ&s'>
        <a href=\'home\'>go to home page</a>
        </html>''')

@app.route('/space3')
def space3():
    return ('''<html>
        <h1></h1>
        <img src='https://cdn.hswstatic.com/gif/outer-space.jpg'>
        <a href=\'home\'>go to home page</a>
        </html>''')

if __name__ == '__main__':
    app.run(debug=True)
