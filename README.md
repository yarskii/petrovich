# Проект Web/Mobile тестирования сайта компании СТД Петрович

   <p align="center">
      <img src="https://github.com/yarskii/petrovich/blob/main/resources/screenshots/logo_petrovich.jpeg" alt="Логотип компании Петрович" width="730" height="250"/>
   </p>

---

Этот проект содержит автоматизированные тесты для веб-сайта [Петрович](https://petrovich.ru/).

## Описание

Проект включает набор автоматизированных тестов, написанных с использованием фреймворков Selene, Allure и Pytest. Тесты
проверяют основные функциональные возможности сайта, такие как авторизация, поиск товаров, добавление товаров в корзину
и навигация по каталогу.

---

## Используемые инструменты

[//]: # (<p align="center">)

[//]: # (  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python Logo" height="25" width="" />)

[//]: # (  <img src="https://img.shields.io/badge/selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white" alt="Selenium Logo" height="25" width="" />)

[//]: # (  <img src="https://img.shields.io/badge/Google_Chrome-4285F4?style=for-the-badge&logo=Google-Chrome&logoColor=white" alt="Chrome Logo" height="25" width="" />)

[//]: # (  <img src="https://img.shields.io/badge/jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white" alt="Jenkins Logo" height="25" width="" />)

[//]: # (  <img src="https://img.shields.io/badge/allure-F7C03F?style=for-the-badge&logo=allure&logoColor=black" alt="Allure Logo" height="25" width="" />)

[//]: # (  <img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram Logo" height="25" width="" />)

[//]: # (  <img src="https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" alt="Pytest Logo" height="25" width="" />)

[//]: # (  <img src="https://img.shields.io/badge/appium-1886DD?style=for-the-badge&logo=appium&logoColor=white" alt="Appium Logo" height="25" width="" />)

[//]: # (  <img src="https://img.shields.io/badge/browserstack-5879F7?style=for-the-badge&logo=browserstack&logoColor=white" alt="Browserstack Logo" height="25" width="" />)

[//]: # (  <img src="https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green" alt="PyCharm Logo" height="25" width="" />)

[//]: # (  <img src="https://img.shields.io/badge/android%20studio-3DDC84?style=for-the-badge&logo=android-studio&logoColor=white" alt="Android Studio Logo" height="25" width="" />)

[//]: # (  <img src="https://img.shields.io/badge/allure%20testops-F7C03F?style=for-the-badge&logo=allure&logoColor=black" alt="Allure TestOps Logo" height="25" width="" />)

[//]: # (  <img src="https://img.shields.io/badge/jira-0052CC?style=for-the-badge&logo=jira&logoColor=white" alt="Jira Logo" height="25" width="" />)

[//]: # (</p>)

<p align="center">
  <img src="https://img.icons8.com/color/48/000000/python.png" alt="Python Logo" height="40" width="40" />
  <img src="https://img.icons8.com/color/48/000000/selenium.png" alt="Selenium Logo" height="40" width="40" />
  <img src="https://img.icons8.com/color/48/000000/google-chrome.png" alt="Chrome Logo" height="40" width="40" />
  <img src="https://img.icons8.com/color/48/000000/jenkins.png" alt="Jenkins Logo" height="40" width="40" />
  <img src="https://img.icons8.com/color/48/000000/allure.png" alt="Allure Logo" height="40" width="40" />
  <img src="https://img.icons8.com/color/48/000000/telegram-app.png" alt="Telegram Logo" height="40" width="40" />
  <img src="https://img.icons8.com/color/48/000000/pytest.png" alt="Pytest Logo" height="40" width="40" />
  <img src="https://img.icons8.com/color/48/000000/appium.png" alt="Appium Logo" height="40" width="40" />
  <img src="https://img.icons8.com/color/48/000000/browserstack.png" alt="BrowserStack Logo" height="40" width="40" />
  <img src="https://img.icons8.com/color/48/000000/pycharm.png" alt="PyCharm Logo" height="40" width="40" />
  <img src="https://img.icons8.com/color/48/000000/android-studio.png" alt="Android Studio Logo" height="40" width="40" />
  <img src="https://img.icons8.com/color/48/000000/allure-testops.png" alt="Allure TestOps Logo" height="40" width="40" />
  <img src="https://img.icons8.com/color/48/000000/jira.png" alt="Jira Logo" height="40" width="40" />
</p>


| Инструмент       | Описание                                                                                                                   |
|------------------|----------------------------------------------------------------------------------------------------------------------------|
| **Selene**       | Обертка над Selenium, облегчающая написание тестов и взаимодействие с веб‑элементами.                                      |
| **Allure**       | Инструмент для создания красочных отчетов о тестировании с поддержкой различных языков.                                    |
| **Pytest**       | Фреймворк для написания и запуска тестов. Он предоставляет удобный синтаксис и разнообразные возможности для тестирования. |
| **Appium**       | Инструмент для автоматизации мобильных приложений, позволяет тестировать приложения на Android и iOS.                      |
| **Browserstack** | Облачный сервис для запуска тестов на реальных устройствах и браузерах.                                                    |

---

## Содержание

<details>
<summary>Установка</summary>

### Клонирование репозитория

Для начала работы, клонируйте репозиторий и перейдите в директорию проекта:

   ```sh
    git clone https://github.com/yarskii/petrovich.git
    cd cft_tests
   ```

### Создание виртуального окружения (опционально)

   ```sh
    python -m venv venv
    source venv/bin/activate  # Для Linux/macOS
    .\venv\Scripts\activate   # Для Windows
   ```

### Установка зависимостей

Создайте файл `requirements.txt`, содержащий список всех зависимостей проекта:

   ```sh
    pip freeze > requirements.txt
   ```

Затем установите зависимости:

   ```sh
    pip install -r requirements.txt
   ```

Если у вас уже есть файл `requirements.txt`, просто выполните команду:

   ```sh
    pip install -r requirements.txt
   ```

</details>

<details>
<summary>Запуск тестов</summary>

### Локальный запуск

Чтобы запустить все тесты, выполните команду:

   ```sh
    pytest
   ```

Для запуска конкретного теста, используйте следующую команду:

   ```sh
    pytest tests/ui/authentication/test_successful_login_ui.py
   ```

### Параметры запуска

Вы можете использовать различные параметры для управления поведением тестов:

- `-s`: Выводить все выводы в консоль.
- `-v`: Детализированное логирование.
- `--alluredir=allure-results`: Сохранять результаты тестов для генерации отчетов Allure.

Пример команды:

   ```sh
    pytest --alluredir=allure-results
   ```

</details>


<details>
<summary>Генерация отчетов Allure</summary>

### Установка Allure Commandline

Следуйте инструкциям на официальном сайте [Allure](https://docs.qameta.io/allure/#_installing_a_commandline) для
установки Allure Commandline.

### Генерация отчета

После выполнения тестов с параметром `--alluredir`, вы можете сгенерировать отчет следующей командой:

   ```sh
    allure serve allure-results
   ```

</details>

<details>
<summary>Запуск проекта в Jenkins</summary>

1. Откройте [проект](https://jenkins.autotests.cloud/job/petrovich/)
2. Выберите `Build with parameters`
3. Измените параметры, если требуется:
    - Укажите комментарий
    - Выберите вариант теста
    - Выберите версию браузера
    - Выберите мобильное окружение (для мобильных тестов)
4. Нажмите `Build`
5. После сборки, результат работы можно увидеть в `Allure Report`

> **Доступные параметры**:
> - Варианты тестов: `tests`, `tests/api`, `tests/mobile`, `tests/ui`...
> - Версия браузера: `99`, `100`, `113`, `114`, `120`, `121`, `122`, `123`, `124`, `125`, `126`
---
</details>

<details>
<summary>Диграмма</summary>

### Последовательность действий при запуске тестов

```mermaid
sequenceDiagram
    participant Developer as Разработчик
    participant LocalEnv as Локальная Среда
    participant Jenkins as Jenkins
    participant Allure as Отчеты Allure

    Developer->>LocalEnv: Клонирование Репозитория
    LocalEnv->>Developer: Установка Зависимостей
    Developer->>LocalEnv: Активация Виртуального Окружения
    LocalEnv->>Jenkins: Пуш Кода
    Jenkins->>Jenkins: Сборка с Параметрами
    Jenkins->>Jenkins: Запуск Тестов
    Jenkins->>Allure: Генерация Отчета
    Allure-->>Developer: Просмотр Отчета
```

</details>

<details>
<summary>Скриншоты</summary>

### Cтраница тестов Jenkins

   <p align="center">
      <img src="https://github.com/yarskii/petrovich/blob/main/resources/screenshots/jenkins_home.png" alt="Cтраница тестов Jenkins" width="630" height="320"/>
   </p>

### Общий отчёт Allure

   <p align="center">
      <img src="https://github.com/yarskii/petrovich/blob/main/resources/screenshots/allure_results.png" alt="Общий отчёт Allure" width="630" height="320"/>
   </p>

### Детальный отчёт о пройденном тесте

   <p align="center">
      <img src="https://github.com/yarskii/petrovich/blob/main/resources/screenshots/allure_reports.png" alt="Детальный отчёт о пройденном тесте" width="630" height="320"/>
   </p>

### Видео-отчет о прохождении теста UI

   <p align="center">
      <img src="https://github.com/yarskii/petrovich/blob/main/resources/screenshots/video_test_example.gif" alt="Видео-отчет о прохождении теста" width="630" height="320"/>
   </p>

### Видео-отчет о прохождении мобильного теста

   <p align="center">
      <img src="https://github.com/yarskii/petrovich/blob/main/resources/screenshots/with_login.gif" alt="Видео-отчет о прохождении теста" width="630" height="630"/>
   </p>

### Отчет в Telegram

   <p align="center">
      <img src="https://github.com/yarskii/petrovich/blob/main/resources/screenshots/telegram_report.png" alt="Отчет в Telegram"/>
   </p>
</details>

---

## Лицензия

Этот проект лицензирован под MIT License. Подробности смотрите в файле [LICENSE](LICENSE).

---

Если у вас есть вопросы или предложения, пожалуйста, создайте issue на GitHub или свяжитесь со мной напрямую.

Автор: Ярослав Гусев
