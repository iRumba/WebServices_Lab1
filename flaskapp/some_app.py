import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')

if __name__ == '__main__':
    # Получаем порт из переменной окружения (если есть)
    # Если переменной нет, используем 5000 для локальной разработки
    port = int(os.environ.get('PORT', 5000))
    
    # Запускаем приложение
    # 0.0.0.0 - слушаем на всех интерфейсах (важно для Render!)
    app.run(host='0.0.0.0', port=port, debug=False) 