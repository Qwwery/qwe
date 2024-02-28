from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/')
def misiya():
    return "Миссия Колонизация Марса"


@app.route('/index')
def deviz():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def reklama():
    fraza = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
             'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return "</br>".join(fraza)


@app.route('/promotion_image')
def promotion_image():
    fraza = []
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                  </head>
                  <body>
                    <h1 style='color:red'>Жди нас, Марс!</h1>
                    <img src='data:image/jpeg;base64,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' width=200 height=200>
                    <p class="alert alert-dark">Человечество выростает из детства.</p>
                    <p class="alert alert-success">Человеству мала одна планета.</p>
                    <p class="alert alert-dark">Мы сделаем обитаемыми безжизненные пока планеты.</p>
                    <p class="alert alert-warning" role="alert">И начнем с марса!</p>
                    <p class="alert alert-danger">Присоединяйся!</p>
                  </body>
                </html>"""


@app.route('/image_mars')
def image_mars():
    fraza = []
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src='data:image/jpeg;base64,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' width=200 height=200>
                    <p>Вот она какая, красная планта.</p>
                  </body>
                </html>"""


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Отбор астронавтов</title>
                              </head>
                              <body>
                                <h1 align='center'>Анкета претендента</h1>
                                <h4 align='center'>На участие в миссии</h4>
                                <div>
                                    <form class="login_form" method="post">
                                        <input class="form-control" id="email" placeholder="Введите фамилию" name="lastname">
                                        <input class="form-control" id="email" placeholder="Введите имя" name="name">
                                        <br>
                                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                        <div class="form-group">
                                            <label for="classSelect">Какое у вас образование?</label>
                                            <br>
                                            <select class="form-control" id="classSelect" name="class">
                                              <option>Начальное</option>
                                              <option>Основное</option>
                                              <option>Среднее</option>
                                              <option>Высшее образование I степени (бакалавриат)</option>
                                              <option>Высшее образование II степени (специалитет, магистратура)</option>
                                              <option>Высшее образование III степени (подготовка кадров высшей квалификации)</option>
                                            </select>
                                         </div>
                                         <p>Какие у вас есть профессии</p>
                                         <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">инженер-исследователь</label>
                                        </div>
                                        
                                         <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="1" name="accept">
                                            <label class="form-check-label" for="1">пилот</label>
                                        </div>
                                        
                                         <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="2" name="accept">
                                            <label class="form-check-label" for="2">строитель</label>
                                        </div>
                                        
                                         <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="3" name="accept">
                                            <label class="form-check-label" for="3">экзобиолог</label>
                                        </div>
                                        
                                         <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="4" name="accept">
                                            <label class="form-check-label" for="4">врач</label>
                                        </div>
                                        
                                         <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="5" name="accept">
                                            <label class="form-check-label" for="5">инженер по терраформированию</label>
                                        </div>
                                        
                                         <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="6" name="accept">
                                            <label class="form-check-label" for="6">климатолог</label>
                                        </div>
                                        
                                         <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="7" name="accept">
                                            <label class="form-check-label" for="7">специалист по радиационной защите</label>
                                        </div>
                                        
                                         <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="8" name="accept">
                                            <label class="form-check-label" for="8">астрогеолог</label>
                                        </div>
                                        
                                         <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="9" name="accept">
                                            <label class="form-check-label" for="9">гляциолог</label>
                                        </div>
                                        
                                         <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="10" name="accept">
                                            <label class="form-check-label" for="10">инженер жизнеобеспечения</label>
                                        </div>
                                        
                                         <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="11" name="accept">
                                            <label class="form-check-label" for="11">метеоролог</label>
                                        </div>
                                        
                                         <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="12" name="accept">
                                            <label class="form-check-label" for="12">оператор марсохода</label>
                                        </div>
                                        
                                         <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="13" name="accept">
                                            <label class="form-check-label" for="13">киберинженер</label>
                                        </div>
                                        
                                         <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="14" name="accept">
                                            <label class="form-check-label" for="14">штурман</label>
                                        </div>
                                        
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="15" name="accept">
                                            <label class="form-check-label" for="15">пилот дронов</label>
                                        </div>
                                        <br>
                                        <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div>
                                        <br>
                                        <div class="form-group">
                                            <label for="about">Немного о себе</label>
                                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                        </div>
                                        <br>
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        <br>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                        </div>
                                        <br>
                                        <button type="submit" class="btn btn-primary">Записаться</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        return "Форма отправлена"


@app.route('/choice/<string:name>')
def choice(name):
    return f"""
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport"
                  content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>Варианты выбора</title>
            <link rel="stylesheet" 
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
            crossorigin="anonymous">
        </head>
        <body>
            <h1>Моё предложение: {name}.</h1>
            <h2>{name} - классная планета.</h2>
            <h2 class="alert alert-dark">{name} - планета соглнечной системы</h2>
            <h2 class="alert alert-secondary">На ней есть магнитное поле.</h2>
            <h2 class="alert alert-danger">На ней есть инопланетные существа(возможно)</h2>
            <h2 class="alert alert-warning">Я люблю плaнету {name}</h2>
        </body>
        </html>
        
    """


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f"""
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport"
                  content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>Варианты выбора</title>
            <link rel="stylesheet" 
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
            crossorigin="anonymous">
        </head>
        <body>
            <h1>Результаты отбора</h1>
            <h2>Претендентана участие в миссии {nickname}:</h2>
            <h2 class="alert alert-success">Поздравляем! Ваш рейтинг после {level} этапа отбора</h2>
            <h2>состравляет {rating}!</h2>
            <h2 class="alert alert-warning">Желаем удачи!</h2>
        </body>
        </html>

    """


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Загрузка файла</title>
                      </head>
                      <body>
                        <h1 align='center'>Загрузка фотографии</h1>
                        <h4 align='center'>для участия в миссии</h4>
                        <div>
                            <form class="login_form" method="post">
                                <div class="form-group">
                                    <label for="photo">Приложите фотографию</label>
                                    <input accept=".png,.jpg" type="file" class="form-control-file" 
                                            id="photo" name="file">
                                </div>
                                <br>
                                <img src="static/photo/Задача.png">
                                <br>
                                <br>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                        </div>
                      </body>
                    </html>'''
    elif request.method == 'POST':

        print(request.form['file'])
        f = request.files['file']
        print(f)
        return f'''<!doctype html>
                           <html lang="en">
                             <head>
                               <meta charset="utf-8">
                               <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                               <link rel="stylesheet"
                               href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                               integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                               crossorigin="anonymous">
                               <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                               <title>Загрузка файла</title>
                             </head>
                             <body>
                               <h1 align='center'>Успех!</h1>
                               <div>
                                   <form class="login_form" method="post">
                                        <br>
                                        <p>qew</p>
                                   </form>
                               </div>
                             </body>
                           </html>'''


@app.route('/carousel')
def carousel():
    return f'''<!DOCTYPE html>
    <html lang="en">
    <head>
      <title>Пейзажи Марса</title>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet">
      <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" 
              integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" 
              crossorigin="anonymous"></script>
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.min.js" 
              integrity="sha384-Atwg2Pkwv9vp0ygtn1JAojH0nYbwNJLPhwyoVbhoPwBhjQPR5VtM2+xf0Uwh9KtT" 
              crossorigin="anonymous"></script>
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
    </head>
    
    
    <body class="body">
    <h1 align="center">Пейзажи Марса</h1>
    <div id="carouselExampleDark" class="carousel carousel-dark slide">
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="0" class="active" 
                aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="1" 
                aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="2" 
                aria-label="Slide 3"></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active" data-bs-interval="10000">
          <img src="{url_for('static', filename='img/Пейзаж 1.jpg')}" class="d-block w-100" alt="...">
          <div class="carousel-caption d-none d-md-block">
            <h5>\/\/</h5>
          </div>
        </div>
        <div class="carousel-item" data-bs-interval="2000">
          <img src="{url_for('static', filename='img/Пейзаж 2.png')}" class="d-block w-100" alt="...">
          <div class="carousel-caption d-none d-md-block">
            <h5>W</h5>
          </div>
        </div>
        <div class="carousel-item">
          <img src="{url_for('static', filename='img/Пейзаж 3.jpg')}" class="d-block w-100" alt="...">
          <div class="carousel-caption d-none d-md-block">
            <h5>VV</h5>
          </div>
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleDark" 
              data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleDark" 
              data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
    
    </body>
    </html>
            '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
