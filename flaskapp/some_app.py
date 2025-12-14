from flask import Flask, render_template

# Создаем экземпляр приложения Flask
app = Flask(__name__)

# Создаем маршрут для главной страницы
@app.route('/')
def hello():
    # Рендерим шаблон hello.html
    return render_template('hello.html')

# Запускаем приложение
if __name__ == '__lab1__':
    app.run(debug=True)