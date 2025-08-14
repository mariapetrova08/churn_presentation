import streamlit as st

# 1. НАСТРОЙКА СТРАНИЦЫ И СТИЛЕЙ
# Используем широкий макет и добавляем иконку на вкладку браузера
st.set_page_config(
    page_title="Презентация по модели оттока", 
    layout="wide", 
    page_icon="🔮"
)

# Внедряем кастомные CSS-стили для более современного вида
# Это позволяет нам управлять шрифтами, цветами, отступами и тенями
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Создадим простой CSS для эксперимента. 
# Вы можете создать файл styles.css и вызвать local_css("styles.css")
# или просто вставить стили напрямую, как здесь.
st.markdown("""
<style>
    /* Импортируем современный шрифт из Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
    }

    /* Стили для основного контейнера-слайда */
    # .main-container {
    #     background-color: #f5f5f7;
    #     padding: 2rem;
    #     border-radius: 15px;
    #     border: 1px solid #e1e1e1;
    # }

    /* Стили для заголовков */
    h1 {
        color: #1d1d1f;
        font-weight: 700;
    }
    h2 {
        color: #333333;
        font-weight: 600;
    }

    /* Увеличиваем текст в сайдбаре для удобства */
    .st-emotion-cache-16txtl3 {
        font-size: 1.1rem;
    }
</style>
""", unsafe_allow_html=True)


# 2. ОБНОВЛЕННЫЕ ДАННЫЕ ДЛЯ СЛАЙДОВ
# Добавили иконки и изменили структуру некоторых слайдов для лучшей визуализации
slides_data = [
    {
        "nav_title": "1. Инструмент",
        "header": "Проактивное управление клиентским оттоком 🚀",
        "body": """
        ## Новый инструмент на основе искусственного интеллекта для сохранения ключевых клиентов
        
        """
    },
    {
        "nav_title": "2. Проблема",
        "header": "Каждый ушедший клиент — это упущенная выгода 💸",
        "body": """
        """,
        # Используем новый тип слайда "metrics" для акцентов
        "slide_type": "metrics",
        "metrics": [
            {"label": "Финансовые потери", "value": "Существенные", "delta": "Потеря дохода от РКО", "delta_color": "inverse"},
            {"label": "Управляемый инструмент", "value": "Отсутствует", "delta": "Нет возможности влияния", "delta_color": "inverse"},
            {"label": "Тестирование подходов", "value": "Без данных", "delta": "Решения на основе интуиции", "delta_color": "inverse"}
        ],
        "special": ("warning", "> **Ключевой вопрос:** Как нам узнать о намерении клиента уйти *до того*, как он примет окончательное решение?")
    },
    {
        "nav_title": "3. Решение",
        "header": "Наше решение — умная модель 📡",
        "body": """
        ### Теперь предсказываем отток клиентов

        Это сложный алгоритм, обученный на исторических данных о тысячах наших клиентов. Он анализирует десятки параметров:
        - Снижение оборотов по счету
        - Наличие ограничений по счету
        - Изменение частоты платежей
        - Использование (или неиспользование) продуктов банка
        - Частота обращений в поддержку
        - Закрытие неосновных счетов
        - Снижение активного использования онлайн-банка
        """
        ,
        "special": ("info", "✅ **Результат:** Каждый месяц модель формирует готовый список клиентов с высоким риском ухода.")
    },
    {
        "nav_title": "4. Как это работает",
        "header": "От интуиции к точным данным 🧠",
        "body": "Два подхода к работе с оттоком:",
        "columns": {
            "col1_title": "Старый подход (Реактивный) 👎",
            "col1_body": """
            - **Основа:** Отсутствие централизованного подхода на уровне КЦ.
            - **Момент:** Реакция на обращение клиента при закрытии счета.
            - **Итог:** Упускаем "тихих" клиентов, которые уходят молча.
            """,
            "col2_title": "Новый подход (Проактивный) 👍",
            "col2_body": """
            - **Основа:** Анализ данных и AI.
            - **Момент:** Выявление риска оттока на ранней стадии.
            - **Итог:** Фокусируем усилия на тех, кто действительно может уйти.
            """
        }
    },
    {
        "nav_title": "5. Бизнес-выгода",
        "header": "Что это дает именно вам? 🎯",
        "body": "",
        "special": ("success", """
        - **🎯 Польза** для управленческого состава для применения инструментов централизованно.
        - **📈 Фокус на клиентах в отток.** Управление на основе данных, а не интуиции. Чёткое выделение сегментов.
        - **🏆 Сохраняем клиента** — не теряем в потенциальном комиссионном доходе, который может принести клиент.
        - **💡 Удержание дешевле привлечения** (ограничения на привлечения клиентов).
        """)
    },
    {
        "nav_title": "6. План",
        "header": "Как мы начнем работать по-новому? 🗓️",
        "body": "### Наш план состоит из трех простых шагов:",
        "columns": {
            "col1_title": "1️⃣ Шаг 1. Работа модели",
            "col1_body": """
            Мы ежемесячно предоставляем список клиентов, подверженных к оттоку.
            """,
            "col2_title": "2️⃣ Шаг 2. Обработка",
            "col2_body": """
            Обработка клиентов, тестирование новых подходов.
            """,
            "col3_title": "3️⃣ Шаг 3. Масштабирование",
            "col3_body": """
            На основе анализа масштабируем критерии для модели.
            """
        }
    }
]


# 3. ЛОГИКА ОТОБРАЖЕНИЯ
# Боковая панель для навигации осталась прежней, но будет выглядеть лучше из-за CSS
st.sidebar.title("Навигация")
slide_titles = [slide["nav_title"] for slide in slides_data]
selected_slide_title = st.sidebar.radio("Выберите слайд:", slide_titles, label_visibility="collapsed")

# Находим данные для выбранного слайда
selected_slide = next(s for s in slides_data if s["nav_title"] == selected_slide_title)

# Отображаем контент в стилизованном контейнере
with st.container():
    # Оборачиваем все в div с нашим кастомным классом для стилизации
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    st.header(selected_slide["header"])
    st.markdown("---")
    st.markdown(selected_slide["body"], unsafe_allow_html=True)

    # Отображение специальных блоков
    if selected_slide.get("slide_type") == "metrics":
        cols = st.columns(len(selected_slide["metrics"]))
        for i, metric in enumerate(selected_slide["metrics"]):
            with cols[i]:
                st.metric(**metric)
    
    if "image" in selected_slide:
        # Создаем три колонки: две узкие по бокам и одну широкую в центре
        col1, col2, col3 = st.columns([1, 6, 1])
        with col2: # Используем только центральную колонку
            st.image(selected_slide["image"], use_container_width=True)

    if "columns" in selected_slide:
        cols_data = selected_slide["columns"]
        num_cols = len([key for key in cols_data if key.startswith('col') and key.endswith('title')])
        cols = st.columns(num_cols)
        for i in range(num_cols):
            with cols[i]:
                # Используем новый st.container(border=True) для создания красивых карточек
                with st.container(border=True):
                    st.subheader(cols_data[f"col{i+1}_title"])
                    st.markdown(cols_data[f"col{i+1}_body"])

    if "special" in selected_slide:
        block_type, content = selected_slide["special"]
        if block_type == "info":
            st.info(content)
        elif block_type == "warning":
            st.warning(content)
        elif block_type == "success":
            st.success(content)

    
            
    # Закрываем наш div
    st.markdown('</div>', unsafe_allow_html=True)
