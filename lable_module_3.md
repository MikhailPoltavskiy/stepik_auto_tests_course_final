# Модуль 3

## Git
+ [Игра про GIT](https://learngitbranching.js.org/?locale=ru_RU )
+ [PyCharm+Git youtube ru](https://www.youtube.com/watch?v=9VKKZNqzPcE)
+ [книга по GIT](https://git-scm.com/book/ru/v2/)
+ [еще один мануал](http://www-cs-students.stanford.edu/~blynn/gitmagic/intl/ru/index.html)
+ [статья на хабре](https://habr.com/ru/company/intel/blog/344962/)
+ [тоже норм (step by step)](https://githowto.com/ru)


С августа 2021 гитхаб отказался от идеи доступа на сервер по АПИ через пароль. Процесс усложнился в пользу безопасности. Теперь в настройках профиля необходимо сгенерировать временный токен для доступа именно к тому функционалу который необходим.

Делается это тут Settings  => Developer Settings => Personal Access Token => Generate New Token (в настройках по выбору прав доступа поставить галку достаточно только в самом верхнем блоке касающемся доступа к репозиторию)

Копируем получившийся токен и используем его вместо пароля
использую PyCharm

## Концепция тестирования

[Пирамида тестирования](https://habr.com/ru/post/358950/)

Любой тест должен содержать:

    1. Входные данные.
    2. Тестовый сценарий, то есть набор шагов, которые надо выполнить для получения результата.
    3. Проверка ожидаемого результата.

Сообщение при проверке
    
    assert abs(-41) == 42, f'Should be absolute value of a number {abs(-41)} not equal 42'

**Конструкция** [if __name__ == "__main__"](https://www.youtube.com/watch?v=cW_-zGG4ef4)

Авто тесты на Python:
+ [unittest](https://docs.python.org/3/library/unittest.html) - встроенный
+ PyTest [статья на хабре](https://habr.com/ru/post/269759/)
+ nose

Сохраняем набор пакетов

    pip freeze > requirements.txt

Дла нового окружения, после активации запускаемЖ
    
    pip install -r requirements.txt

PyTest, для детального отчёта запускается с параметром **-v**

[Другие параметры запуска](https://gist.github.com/amatellanes/12136508b816469678c2)

Ожидаемая ошибка:
    
    import pytest
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import NoSuchElementException
    
    
    def test_exception1():
        try:
            browser = webdriver.Chrome()
            browser.get("http://selenium1py.pythonanywhere.com/")
            with pytest.raises(NoSuchElementException):
                browser.find_element(By.CSS_SELECTOR, "button.btn")
                pytest.fail("Не должно быть кнопки Отправить")
        finally: 
            browser.quit()
    
    def test_exception2():
        try:
            browser = webdriver.Chrome()
            browser.get("http://selenium1py.pythonanywhere.com/")
            with pytest.raises(NoSuchElementException):
                browser.find_element(By.CSS_SELECTOR, "no_such_button.btn")
                pytest.fail("Не должно быть кнопки Отправить")
        finally: 
            browser.quit()


## Фикстуры

Классический способ работы с фикстурами — создание setup- и teardown-методов в файле с тестами

[классическое примерение фикстур](https://docs.pytest.org/en/latest/how-to/xunit_setup.html)

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    link = "http://selenium1py.pythonanywhere.com/"
    
    
    class TestMainPage1():
    
        @classmethod
        def setup_class(self):
            print("\nstart browser for test suite..")
            self.browser = webdriver.Chrome()
    
        @classmethod
        def teardown_class(self):
            print("quit browser for test suite..")
            self.browser.quit()
    
        def test_guest_should_see_login_link(self):
            self.browser.get(link)
            self.browser.find_element(By.CSS_SELECTOR, "#login_link")
    
        def test_guest_should_see_basket_link_on_the_main_page(self):
            self.browser.get(link)
            self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
    
    
    class TestMainPage2():
    
        def setup_method(self):
            print("start browser for test..")
            self.browser = webdriver.Chrome()
    
        def teardown_method(self):
            print("quit browser for test..")
            self.browser.quit()
    
        def test_guest_should_see_login_link(self):
            self.browser.get(link)
            self.browser.find_element(By.CSS_SELECTOR, "#login_link")
    
        def test_guest_should_see_basket_link_on_the_main_page(self):
            self.browser.get(link)
            self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


**Фикстуры это декораторы**
    
    @pytest.fixture

+ [О декораторах](https://pythonworld.ru/osnovy/dekoratory.html)
+ **[Объяснение yield](https://www.youtube.com/watch?v=ZjaVrzOkpZk)**
+ [Статья на хабре](https://habr.com/ru/company/yandex/blog/242795/)
+ [Офф документация](https://docs.pytest.org/en/stable/explanation/fixtures.html)

**Примеры:**
+ test_fixture2.py
+ test_fixture3.py
+ test_fixture5.py
+ test_fixture_autouse.py


## Маркировка

[оф дока](https://pytest.org/en/stable/how-to/skipping.html)

    @pytest.mark.mark_name

Может быть сразу несколько маркировок

    @pytest.mark.smoke
    @pytest.mark.win10

Пропустить тест

    @pytest.mark.skip

Падающий тест (знаем, что упадет)
[оф дока](https://docs.pytest.org/en/latest/reference/reference.html#pytest.mark.xfail)

    @pytest.mark.xfail

Необходимо зарегистрировать маркировки, для этого в корне создаем pytest.ini 

    [pytest]
    markers =
        smoke: marker for smoke tests
        regression: marker for regression tests
        win10

**Примеры запуска:**

    pytest -s -v -m smoke test_fixture8.py
    pytest -s -v -m "not smoke" test_fixture8.py
    pytest -s -v -m "smoke or regression" test_fixture8.py
    pytest -s -v -m "smoke and win10" test_fixture81.py
    

    @pytest.mark.xfail(reason="fixing this bug right now")

    pytest -rx -v test_fixture10a.py (-rx выводит сообщение из reason
    pytest -rX -v test_fixture10b.py (X - подробная информация)

**Примеры:**
+ test_fixture8.py
+ test_fixture81.py
+ test_fixture9.py
+ test_fixture10.py
+ test_fixture10a.py
+ test_fixture10b.py

## Параметризация

conftest.py - в корне проекта и вынесем туда фикстуру с настройками браузера

    import pytest
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    
    
    @pytest.fixture(scope="function")
    def browser():
        print("\nstart browser for test..")
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        service = Service(executable_path="C:/chromedriver/chromedriver.exe")
        browser = webdriver.Chrome(service=service, options=options)
        yield browser
        print("\nquit browser..")
        browser.quit()


фикстура с параметризацией @pytest.mark.parametrize()

    import pytest
    from selenium.webdriver.common.by import By
    
    
    @pytest.mark.parametrize('language', ["ru", "en-gb"])
    def test_guest_should_see_login_link(browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

[оф дока](https://docs.pytest.org/en/latest/how-to/parametrize.html)

Для класса (уже с self)

    @pytest.mark.parametrize('language', ["ru", "en-gb"])
    class TestLogin:
        def test_guest_should_see_login_link(self, browser, language):
            link = f"http://selenium1py.pythonanywhere.com/{language}/"
            browser.get(link)
            browser.find_element(By.CSS_SELECTOR, "#login_link")
            # этот тест запустится 2 раза

        def test_guest_should_see_navbar_element(self, browser, language):
            # этот тест тоже запустится дважды

## Драйверы для других браузеров

**mozila**

[Драйвер мозилы geckodriver](https://github.com/mozilla/geckodriver/releases)


## Передача параметров в командной строке

[оф дока](https://docs.pytest.org/en/latest/example/simple.html)

Плагин перезапуска тестов **pytest-rerunfailures**

    pytest -v --tb=line --reruns 1 --browser_name=chrome test_rerun.py

Для сокращения выводимой служебной информации в консоле используем **--tb=line**

[подробнее про --tb=line](https://docs.pytest.org/en/stable/how-to/usage.html#modifying-python-traceback-printing)

Для PyTest большой набор плагинов

[плагины для pytest](https://docs.pytest.org/en/latest/reference/plugin_list.html)



**[Официальная дока по PyTest](https://docs.pytest.org/en/latest/contents.html)**



## Полезные ссылки

**GIT**

+ [https://learngitbranching.js.org/](https://learngitbranching.js.org/)
+ [https://git-scm.com/book/ru/v2/](https://git-scm.com/book/ru/v2/)
+ [https://hyperskill.org/learn/topic/257/](https://hyperskill.org/learn/topic/257/)
+ [https://stepik.org/course/4138/](https://stepik.org/course/4138/)
+ [http://www-cs-students.stanford.edu/~blynn/gitmagic/intl/ru/index.html](http://www-cs-students.stanford.edu/~blynn/gitmagic/intl/ru/index.html)
+ [https://habr.com/company/intel/blog/344962/](https://habr.com/company/intel/blog/344962/)
+ [https://githowto.com/ru](https://githowto.com/ru)


**Тестирование веб-приложений**

+ [https://realpython.com/python-testing/](https://realpython.com/python-testing/)
+ [пирамида тестирования на практике](https://habr.com/ru/post/358950/)
+ [unittest docs](https://docs.python.org/3/library/unittest.html)


**Тестирование с помощью PyTest**

+ [Статья](https://habr.com/ru/post/269759/)
+ [Введение](https://coderlessons.com/tutorials/python-technologies/uznaite-pytest/pytest-kratkoe-rukovodstvo)
+ [Оф дока](https://docs.pytest.org/en/latest/)
+ [Хорошие практики](https://docs.pytest.org/en/stable/explanation/goodpractices.html)
+ [Полезные флаги](https://gist.github.com/amatellanes/12136508b816469678c2)


**Использование фикстур в PyTest**

+ [Фикстуры в PyTest](https://docs.pytest.org/en/stable/explanation/fixtures.html)
+ [setup and teardown](https://docs.pytest.org/en/stable/how-to/xunit_setup.html)
+ [примеры из яндекса](https://habr.com/ru/company/yandex/blog/242795/)
+ [skip and xfail](https://pytest.org/en/stable/how-to/skipping.html)


**Параметризация, конфигурирование, плагины**

+ [оф дока](https://docs.pytest.org/en/stable/how-to/parametrize.html)
+ [command line](https://docs.pytest.org/en/stable/example/simple.html)
+ [plagins](https://docs.pytest.org/en/stable/how-to/plugins.html)
+ [plagins list](https://docs.pytest.org/en/latest/reference/plugin_list.html)
+ [invoke](https://docs.pytest.org/en/stable/how-to/usage.html#modifying-python-traceback-printing)
