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
        </html>''')
    
if __name__ == '__main__':
    app.run(debug=True)