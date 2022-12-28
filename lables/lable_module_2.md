
# Модуль 2

## checkbox и radiobutton

    <input type="checkbox">
    <input type="radio">

 **Html example**

    <input type="radio" name="language" value="python" checked>
    <input type="radio" name="language" value="selenium">

    <div>
      <input type="radio" id="python" name="language" checked>
      <label for="python">Python</label>
    </div>
    <div>
      <input type="radio" id="java" name="language">
      <label for="java">Java</label>
    </div>

 **Python example**
    
    option1 = browser.find_element(By.CSS_SELECTOR, "[value='python']")
    option1.click()

    option1 = browser.find_element(By.CSS_SELECTOR, "[for='java']")
    option1.click()

## Метод get_attribute
html

    <input class="check-input" type="radio" name="ruler" id="peopleRule" value="people" checked>

Python

    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

**Если атрибута нет, то метод get_attribute вернёт значение None**


## Выпадающие списки

 **Html example**

    <label for="dropdown">Выберите язык программирования:</label>
    <select id="dropdown" class="custom-select">
     <option selected>--</option>
     <option value="1">Python</option>
     <option value="2">Java</option>
     <option value="3">JavaScript</option>
    </select>


 **Python example**

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    
    browser = webdriver.Chrome()
    browser.get(link)
    
    
    browser.find_element(By.TAG_NAME, "select").click()
    browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
        или
    browser.find_element(By.CSS_SELECTOR, "[value='1']").click()

или

    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value("1") # ищем элемент с текстом "Python"

ещё методы
    
    select.select_by_visible_text("text") 
    select.select_by_index(index)

## Запуск JavaScript в автосценарии

 **Python example**
 
    from selenium import webdriver
    browser = webdriver.Chrome()
    browser.execute_script("alert('Robots at work');")
        
        прокрутка кнопки
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
        прокрутка окна
    browser.execute_script("window.scrollBy(0, 100);")

 **JavaScript прокрутка окна**

    button = document.getElementsByTagName("button")[0];
    button.scrollIntoView(true);

## Отправка файла

    import os 
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    element.send_keys(file_path)

 **Alerts**

нажать OK
    
    alert = browser.switch_to.alert #далее alert=confirm=prompt
    alert.accept()

получить сообщение из окна

    alert = browser.switch_to.alert
    alert_text = alert.text

нажать Отмена

    confirm.dismiss()

отправить текст и нажать OK

    prompt = browser.switch_to.alert
    prompt.send_keys("My answer")
    prompt.accept()

 **Переход на новую вкладку**

    browser.switch_to.window(window_name)

    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]

 текущее окно

    current_window = browser.current_window_handle

## Одностраничники (single page application - SPA)

**Ожидания**

+ [Официальная документация](https://selenium-python.readthedocs.io/waits.html)
+ [Перевод на Хабре](https://habr.com/ru/post/273089/)
+ [выступление на youtube](https://www.youtube.com/watch?v=8xbb0NM4l8k&list=LLjxGlxPz50ey7VcmjVlV3JQ&index=17)

Плохой вариант:

    time.sleep(n)

**Вариант получше (Implicit Waits неявное ожидание):**

Ищет каждый элемент в течение 5 секунд, т.е. каждые 500 мс повторяет поиск, а через 5 секунд бросает исключение NoSuchElementException

    browser.implicitly_wait(5)

 *staleness_of(element) # ждет пока пропадет элемент* ??? **выяснить!!!**

 **Исключения при поиске элемента:**

**NoSuchElementException** - элемент не найден за отведенное время

**StaleElementReferenceException** - элемент был найден, но при следующем обращении к нему изменился

**ElementNotVisibleException** - элемент найден, но имеет нулевой размер (пользователь не может взаимодействовать с ним)

**Ожидание, пока не поменяется состояние конкретного элемента (Explicit Waits явное ожидание):** 

    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

 *# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной*

    button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.ID, "verify"))
        )

*# говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной*

    button = WebDriverWait(browser, 5).until_not(
            EC.element_to_be_clickable((By.ID, "verify"))
       )
*# (By.ID, "verify") - такой кортедж называют **локатором**, может быть так ((By.ID, 'селектор'),'значение'))

В модуле expected_conditions есть много других правил:
+ title_is
+ title_contains
+ presence_of_element_located
+ visibility_of_element_located
+ visibility_of
+ presence_of_all_elements_located
+ text_to_be_present_in_element
+ text_to_be_present_in_element_value
* frame_to_be_available_and_switch_to_it
* invisibility_of_element_located
* element_to_be_clickable
* staleness_of
* element_to_be_selected
* element_located_to_be_selected
* element_selection_state_to_be
* element_located_selection_state_to_be
* alert_is_present

[Подробнее об expected_conditions](https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions) 


