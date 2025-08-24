# Lui - Язык декларативного описания пользовательских интерфейсов

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.6+-green.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)](https://github.com/pmswga/lui)

**Lui** - это специализированный язык программирования для декларативного описания пользовательских интерфейсов с автоматической генерацией кода на Tkinter (Python).

## 🚀 Особенности

- **Декларативный синтаксис** - описание UI в простом и понятном формате
- **Автоматическая генерация** - создание готового Python кода с Tkinter
- **Модульная архитектура** - лексер, синтаксический анализатор, генератор кода
- **Кроссплатформенность** - работает на Windows, Linux и macOS
- **Отладка** - встроенные инструменты для диагностики

## 📋 Требования

- Python 3.6 или выше
- Tkinter (обычно входит в стандартную установку Python)

## 🛠️ Установка

### Способ 1: Клонирование репозитория

```bash
git clone https://github.com/pmswga/lui.git
cd lui
```

### Способ 2: Скачивание релиза

1. Перейдите в раздел [Releases](https://github.com/pmswga/lui/releases)
2. Скачайте последнюю версию для вашей платформы
3. Распакуйте архив в нужную папку

## 🚀 Быстрый старт

### 1. Создание простого интерфейса

Создайте файл `hello.lui`:

```lui
Window {
    title: "Привет, мир!"
    width: 400
    height: 300

    Label {
        caption: "Добро пожаловать в Lui!"
        x: 150
        y: 140
    }

    Button {
        caption: "Нажми меня"
        x: 150
        y: 180
    }
}
```

### 2. Генерация Python кода

```bash
python src/lui.py --file=hello.lui
```

### 3. Запуск сгенерированного приложения

```bash
python hello.py
```

## 📖 Синтаксис языка

### Основные компоненты

#### Window (Окно)
```lui
Window {
    title: "Заголовок окна"
    width: 800
    height: 600
    background-color: "white"
}
```

#### Frame (Рамка)
```lui
Frame {
    width: 300
    height: 200
    background-color: "lightblue"
    border: 2
}
```

#### Button (Кнопка)
```lui
Button {
    caption: "Текст кнопки"
    x: 100
    y: 50
    width: 120
    height: 30
    background-color: "green"
}
```

#### Label (Метка)
```lui
Label {
    caption: "Текст метки"
    x: 50
    y: 100
    font-size: 14
    color: "black"
}
```

#### Input (Поле ввода)
```lui
Input {
    x: 100
    y: 150
    width: 200
    placeholder: "Введите текст"
}
```

### Позиционирование

- **Абсолютное позиционирование**: `x: 100, y: 200`
- **Относительное позиционирование**: `position: LEFT, position: CENTER`

### Цвета и стили

- **Цвета**: `"red"`, `"#FF0000"`, `"rgb(255,0,0)"`
- **Размеры**: `width`, `height`
- **Шрифты**: `font-size`, `font-family`

## 🎯 Примеры

### Простое окно
```lui
Window {
    title: "Моё приложение"
    width: 300
    height: 200
}
```

## 🔧 Команды интерфейса

### Основные команды

```bash
# Справка
python src/lui.py --help

# Обработка файла
python src/lui.py --file=path/to/file.lui

# Режим отладки
python src/lui.py --file=file.lui --debug

# Версия
python src/lui.py --version
```

### Флаги командной строки

| Флаг | Описание |
|------|----------|
| `--help` | Показать справку по командам |
| `--file=<путь>` | Указать путь к .lui файлу |
| `--debug` | Включить режим отладки |
| `--version` | Показать версию Lui |

## 🏗️ Архитектура проекта

```
src/
├── translator/           # Основной модуль переводчика
│   ├── lexer/          # Лексический анализатор
│   ├── syntaxer/       # Синтаксический анализатор
│   ├── generator/      # Генератор кода
│   ├── preprocessor/   # Препроцессор
│   └── postprocessor/  # Постпроцессор
├── components/          # Компоненты интерфейса
├── app.py              # Главное приложение
└── lui.py              # Точка входа
```

### Процесс компиляции

1. **Препроцессор** - обработка директив и переменных
2. **Лексер** - разбор на токены
3. **Синтаксический анализатор** - построение дерева синтаксиса
4. **Генератор** - создание Python кода
5. **Постпроцессор** - финальная обработка и сохранение

## 🧪 Тестирование

Запуск тестов:

```bash
cd tests
python -m pytest test_lexer.py
python -m pytest test_syntaxer.py
```

## 📚 Генерация документации

### Doxygen

1. Установите [Doxygen](https://www.doxygen.nl/index.html)
2. **Windows**: Откройте Doxywizard и выберите `Doxyfile` в папке `src`
3. **Linux/macOS**: 
   ```bash
   cd src
   doxygen Doxyfile
   ```

### Документация в браузере

Откройте `docs/index.html` для просмотра HTML документации.

## 🐛 Отладка

### Включение режима отладки

```bash
python src/lui.py --file=file.lui --debug
```

Режим отладки показывает:
- Список токенов
- Дерево синтаксиса
- Промежуточный код

### Логи и ошибки

При возникновении ошибок проверьте:
- Синтаксис .lui файла
- Корректность путей к файлам
- Версию Python

## 🤝 Вклад в проект

1. Форкните репозиторий
2. Создайте ветку для новой функции (`git checkout -b feature/amazing-feature`)
3. Зафиксируйте изменения (`git commit -m 'Add amazing feature'`)
4. Отправьте в ветку (`git push origin feature/amazing-feature`)
5. Откройте Pull Request

## 📄 Лицензия

Этот проект распространяется под лицензией MIT. См. файл [LICENSE](LICENSE) для подробностей.

## 🔗 Полезные ссылки

- [Домашняя страница](https://pmswga.github.io/lui/)
- [Примеры](examples/)
- [Документация](docs/)
- [Исследования](documentation/research/)

## 📞 Поддержка

Если у вас есть вопросы или предложения:

- Создайте [Issue](https://github.com/pmswga/lui/issues)
- Обратитесь к [документации](docs/)
- Изучите [примеры](examples/)

---

**Lui** - делаем создание интерфейсов простым и понятным! 🎨✨
