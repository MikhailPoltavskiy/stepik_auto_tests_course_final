## Code Style в автотестах

+ Стремитесь к **максимальной линейности кода тестов**: избегайте ветвления и циклов в тест-кейсах. Если хочется добавить в тесте if, значит, нужно разбить этот тест на два теста или подготовить тестовое окружение так, чтобы не было необходимости использовать ветвление.
+ Избегайте зависимых тестов, которые нужно запускать строго в определенном порядке. При росте количества автотестов вы захотите запускать их в несколько потоков параллельно, что будет невозможно при наличии зависимых тестов. **[Зависимые тесты плохо](http://barancev.github.io/test-deps-are-evil/)**
+ Стремитесь к тому, чтобы **тест не полагался на контент**, а готовил данные самостоятельно (и удалял после завершения). Используйте чистые браузеры и новых пользователей для лучшей воспроизводимости.
+ **Абсолютная линейность проверок**. Когда вы пишете assert-утверждения в функциях, не следует использовать ветвления и циклы. Логика проверок должна быть линейна, иначе разбор багов и починка автотестов будут стоить очень дорого.
+ **Именуйте проверки в одинаковом стиле**, чтобы по первому взгляду можно было понять, что это именно проверка. Например, можно именовать функции по шаблону should_be_smth:


    def should_be_reply_comment()

+ **Тесты именуются в одинаковом стиле**. Имена тестов должны хорошо отражать различия в похожих сценариях. Можно использовать те же подходы, что и при добавлении имен к тест-кейсам в тестовой документации. Например, test_guest_can_see_teach_button() — обратите внимание на явное указание на роль пользователя.
+ Одинаковые тесты, которые отличаются только каким-то контентом (например, языком интерфейса), следует **не копировать, а параметризовать**.
+ Пишите **максимально атомарные и неделимые тесты**. Не нужно писать один мега-тест, который проверяет вообще всё, напишите лучше десяток маленьких — проще будет локализовать проблему, когда она возникнет.

**RU**
+ [Что такое красивый код](https://habr.com/ru/post/266969/)
+ [Практика хорошего кода](https://habr.com/ru/post/206868/)
+ [PEP 8 ru](https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html)

**EN**
+ [Code Style](https://docs.python-guide.org/writing/style/)
+ [PEP 8 en](https://peps.python.org/pep-0008/)


## Page Object Model

[exaple test project](https://blog.testproject.io/2019/07/16/develop-page-object-selenium-tests-using-python/)


## Отсутсвие элемента

+ Элемент потенциально может появиться на странице
+ Элемент присутствует на странице и должен исчезнуть

+ [как не надо делать](https://habr.com/ru/company/badoo/blog/419419/)
+ [Ожидания](https://selenium-python.readthedocs.io/waits.html)

Пример использования:

    def is_not_element_present(self, how, what, timeout=4):
    try:
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
    except TimeoutException:
        return True

    return False

___
    def should_not_be_success_message(self):
    assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"

___
    def is_disappeared(self, how, what, timeout=4):
    try:
        WebDriverWait(self.browser, timeout, 1, TimeoutException).\
            until_not(EC.presence_of_element_located((how, what)))
    except TimeoutException:
        return False

    return True


## Setup & Teardown внутри теста

    @pytest.mark.login
    class TestLoginFromProductPage():
        @pytest.fixture(scope="function", autouse=True)
        def setup(self):
            self.product = ProductFactory(title = "Best book created by robot")
            # создаем по апи
            self.link = self.product.link
            yield
            # после этого ключевого слова начинается teardown
            # выполнится после каждого теста в классе
            # удаляем те данные, которые мы создали 
            self.product.delete()
            
    
        def test_guest_can_go_to_login_page_from_product_page(self, browser):
            page = ProductPage(browser, self.link)
            # дальше обычная реализация теста
    
        def test_guest_should_see_login_link(self, browser):
            page = ProductPage(browser, self.link)
            # дальше обычная реализация теста


**Pytest & API**
+ [Part 1](https://www.ontestautomation.com/writing-tests-for-restful-apis-in-python-using-requests-part-1-basic-tests/)
+ [Part 2](https://www.ontestautomation.com/writing-tests-for-restful-apis-in-python-using-requests-part-2-data-driven-tests/)
+ [Part 3](https://www.ontestautomation.com/writing-tests-for-restful-apis-in-python-using-requests-part-3-working-with-xml/)

