#Лабораторна №1:

Згідно свого варіанту мені потрібно було встановити **python** версії **3.6** та **pipenv**

За допомогою команд в терміналі я додатково встановив **pyenv** склонувавши з гітхабу командою git clone https://github.com/pyenv/pyenv.git ~/.pyenv і з його допомогою встановив python потрібної версії командою **pyenv install --list**, згодом потрбіно було ввести версію python, в моєму випадку 3.6.0

При створені програми я використовував фреймворк **Flask**

Сервер запускався за допомогою **WSGI-сервера "gunicorn"**, а саме командою **gunicorn --bind 0.0.0.0:5000 app:app**

Перевірка роботи сервера здійснювалася за допомогою команди **curl -v -XGET http://localhost:5000/api/v1/hello-world-24**

Після перевірки я побачив, що проблем з сервером немає і **http-протокол** має статус 200, тому я вирішив закомітити та запушити файли моєї програми на свій гітхаб репозиторій. Для цього я використовував ряд команд, таких як:
* **get init**
* **git add README.md**
* **git commit -m "first commit"**
* **git remote add origin https://github.com/Yaroslav-Rohan/AppliedProgramming.git**
* **git push -u origin master**

Після фінальної перевірки, я зробив висновок, що задоволений результатами виконання цієї лабораторної роботи
