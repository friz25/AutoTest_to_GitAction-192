FROM python
#COPY requirements.txt .
#COPY tests/test_api.py .
COPY . .
COPY pages .
COPY tests .
RUN mkdir allure-results
RUN pip install -r requirements.txt

# установка Chrome (нужен для Selenium тестов)
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get update && apt-get install -y google-chrome-stable

CMD ["pytest", "tests/test_api.py", "--alluredir=allure-results"]

# чтоб Создать Образ / В терминале venv :
#docker build -t docker_tests .

# Запуск :
#docker run --rm docker_tests

# c записью allure-отчётов в файл (на нашем жестком) :
#docker run --rm -v C:\Django\222\AutoTest_to_GitAction\AutoTest_to_GitAction-192\docker-results\:/allure-results/ docker_tests