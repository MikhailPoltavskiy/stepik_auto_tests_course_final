Модуль 1
Поиск на странице (http://suninjuly.github.io/cats.html)
Поиск по ID (id="unique_name"):
    #unique_name
Поиск по tag (<h1></h1>):
    h1
Поиск по атрибуту(<h1 class="jumbotron-heading" value="Cat memes">Cat memes</h1>):
     [value="Cat memes"]
Поиск по name:
     [name="bullet-cat"]
Поиск по class:
     [class="jumbotron-heading"]
     или
     .jumbotron-heading
Составной класс (<article id="moto" class="lead text-muted" title="one-thing" name="moto">If there's one thing that the internet was made for, it's funny cat memes.</article>)
    [class="lead text-muted"] - порядок важен
    или
    .lead.text-muted - порядок не важен
    или
    .text-muted.lead
Поиск потомков:
    #post2 .title - пробел важен
Поиск детей:
    #post2 > div.title - пробел не важен
Порядковый номер:
    :nth-child(n)
    #posts > .item:nth-child(2) > .title
Поиск XPath:
    /html/body/header
    //img[@id='bullet']
    //div[@class="row"]/div[2]
    //p[text()="Lenin cat"]
    //div[contains(@class, "navbar")]
    //img[@name='bullet-cat' and @data-type='animal']
    //div/*[@class="jumbotron-heading"]

Selenium:
find_element() - находит и возвращает Первое совпадение, если не найдено - NoSuchElementException - ошибка
find_element(By.ID, value) — поиск по уникальному атрибуту id элемента. Если ваши разработчики проставляют всем элементам в приложении уникальный id, то вам повезло,и вы чаще всего будет использовать этот метод, так как он наиболее стабильный;
find_element(By.CSS_SELECTOR, value) — поиск элемента с помощью правил на основе CSS. Это универсальный метод поиска, так как большинство веб-приложений использует CSS для вёрстки и задания оформления страницам. Если find_element_by_id вам не подходит из-за отсутствия id у элементов, то скорее всего вы будете использовать именно этот метод в ваших тестах;
find_element(By.XPATH, value) — поиск с помощью языка запросов XPath, позволяет выполнять очень гибкий поиск элементов;
find_element(By.NAME, value) — поиск по атрибуту name элемента;
find_element(By.TAG_NAME, value) — поиск элемента по названию тега элемента;
find_element(By.CLASS_NAME, value) — поиск по значению атрибута class;
find_element(By.LINK_TEXT, value) — поиск ссылки на странице по полному совпадению;
find_element(By.PARTIAL_LINK_TEXT, value) — поиск ссылки на странице, если текст селектора совпадает с любой частью текста ссылки.
find_elements() - находит и возвращает Все совпадения, если не найдено - пустой список
find_elements(By.CSS_SELECTOR, ".good")
find_element(By.XPATH, '//button[text()="Some text"]')




