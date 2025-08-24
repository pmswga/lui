# LUI - Language for User Interface

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Status](https://img.shields.io/badge/status-development-orange.svg)]()

## 📖 Описание

**LUI** (Language for User Interface) — это декларативный язык программирования для создания пользовательских интерфейсов с автоматической генерацией кода на Tkinter. Проект представляет собой полноценный компилятор, который преобразует высокоуровневые описания интерфейса в исполняемый Python код.

## 🎯 Основные возможности

- **Декларативный синтаксис** — описание интерфейса в простом и понятном формате
- **Автоматическая генерация** — создание готового Tkinter кода без ручного программирования
- **Модульная архитектура** — разделение на лексический анализатор, синтаксический анализатор и генератор кода
- **Поддержка компонентов** — готовые UI компоненты (окна, кнопки, метки, фреймы и др.)
- **Гибкая компоновка** — различные способы размещения элементов интерфейса
- **Отладочный режим** — возможность просмотра промежуточных результатов компиляции

## 🏗️ Архитектура проекта

```
src/
├── app.py                          # Главное приложение
├── lui.py                          # Точка входа
├── components/                     # Базовые классы компонентов
│   ├── AbstractComponent.py       # Абстрактный базовый класс
│   ├── FormComponent.py           # Компоненты форм
│   ├── InputComponent.py          # Компоненты ввода
│   ├── LayoutComponent.py         # Компоненты компоновки
│   └── OutputComponent.py         # Компоненты вывода
└── translator/                     # Система трансляции
    ├── translator.py               # Главный класс транслятора
    ├── lui_definition.py          # Определения языка
    ├── preprocessor/               # Препроцессор
    ├── lexer/                      # Лексический анализатор
    ├── syntaxer/                   # Синтаксический анализатор
    ├── generator/                  # Генератор кода
    │   └── ComponentGenerator/     # Генераторы компонентов
    │       └── TkComponentGenerator.py
    └── postprocessor/              # Постпроцессор
```

## 🚀 Быстрый старт

### Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/your-username/lui.git
cd lui
```

2. Убедитесь, что у вас установлен Python 3.6+ и Tkinter

### Использование

#### Базовый пример

Создайте файл `hello.lui`:
```lui
Window {
    title: "Привет, мир!"
    width: 400
    height: 300

    Frame {
        width: 200
        height: 150
        background-color: "lightblue"

        Button {
            caption: "Нажми меня"
            position: CENTER
        }

        Label {
            caption: "Это метка"
            x: 50
            y: 50
        }
    }
}
```

#### Компиляция

```bash
python src/lui.py --file=hello.lui
```

#### Отладочный режим

```bash
python src/lui.py --file=hello.lui --debug
```

## 📚 Синтаксис языка

### Структура компонента

```lui
ComponentName {
    property1: value1
    property2: value2
    ...
    
    ChildComponent {
        child_property: child_value
    }
}
```

### Поддерживаемые компоненты

| Компонент | Описание | Свойства |
|-----------|----------|----------|
| `Window` | Главное окно приложения | `title`, `width`, `height` |
| `Frame` | Контейнер для других компонентов | `width`, `height`, `background-color` |
| `Button` | Кнопка | `caption` |
| `Label` | Текстовая метка | `caption`, `x`, `y` |
| `Grid` | Сеточная компоновка | `rows`, `cols` |
| `Line` | Поле ввода | - |
| `Text` | Многострочный текст | - |
| `List` | Список элементов | `data` |
| `Table` | Таблица | - |
| `Tree` | Древовидная структура | - |
| `Slider` | Ползунок | - |
| `Checkbox` | Флажок | - |
| `Radio` | Переключатель | - |
| `Combobox` | Выпадающий список | - |
| `Spinbox` | Поле с числовым значением | - |
| `Range` | Диапазон значений | - |

### Свойства позиционирования

- `position` - позиция элемента (LEFT, RIGHT, TOP, BOTTOM, CENTER)
- `x`, `y` - координаты элемента
- `padding-x`, `padding-y` - внутренние отступы
- `background-color` - цвет фона

## 🔧 Команды командной строки

```bash
python src/lui.py [опции]

Опции:
  --help        Показать справку
  --file=path   Путь к файлу .lui
  --debug       Включить отладочный режим
  --version     Показать версию
```

## 📁 Примеры

### Простое окно
```lui
Window {
    title: "Простое окно"
    width: 300
    height: 200
}
```

### Форма с элементами управления
```lui
Window {
    title: "Форма"
    width: 400
    height: 300

    Frame {
        width: 350
        height: 250

        Label {
            caption: "Имя:"
            x: 20
            y: 20
        }

        Line {
            x: 100
            y: 20
        }

        Button {
            caption: "Отправить"
            x: 150
            y: 100
        }
    }
}
```

## 🧪 Тестирование

Запуск тестов:
```bash
cd tests
python -m pytest test_lexer.py
python -m pytest test_syntaxer.py
```

## 🔍 Отладка

При включении отладочного режима (`--debug`) вы увидите:
- Токены, полученные лексическим анализатором
- Синтаксическое дерево
- Промежуточный код генератора

## 📖 Документация

Подробная документация доступна в папке `docs/`:
- `documentation.html` - основная документация
- `examples.html` - примеры использования
- `get_started.html` - руководство по началу работы

## 🤝 Вклад в проект

1. Форкните репозиторий
2. Создайте ветку для новой функции (`git checkout -b feature/amazing-feature`)
3. Зафиксируйте изменения (`git commit -m 'Add amazing feature'`)
4. Отправьте в ветку (`git push origin feature/amazing-feature`)
5. Откройте Pull Request

## 📝 Лицензия

Этот проект лицензирован под MIT License - см. файл [LICENSE](LICENSE) для деталей.

## 👥 Авторы

- Основная команда разработки LUI

## 📞 Поддержка

Если у вас есть вопросы или предложения:
- Создайте Issue в репозитории
- Обратитесь к документации в папке `docs/`

## 🔮 Планы развития

- [ ] Поддержка дополнительных UI библиотек (PyQt, Kivy)
- [ ] Визуальный редактор интерфейсов
- [ ] Расширенная система стилей
- [ ] Поддержка событий и обработчиков
- [ ] Интеграция с современными фреймворками

---

**LUI** - делаем создание интерфейсов простым и декларативным! 🚀
