// Код для новостей
// получаем элементы header-content
const header_content = document.querySelector('.header-content');
// Получаем левую кнопку
const prevButton = document.querySelector('.left-arrow');
// Получаем правую кнопку
const nextButton = document.querySelector('.right-arrow');
// Получаем все новости
const news = Array.from(header_content.querySelectorAll('.news'));
// Получаем количество новостей
const newsCount = news.length;
// Начинаем показывать с первой (актуальной) новости
let newsIndex = 0;

// Устанавливаем обработчики событий для кнопок
prevButton.addEventListener('click', showPreviousNews);
nextButton.addEventListener('click', showNextNews);

// Функция для показа предыдущей новости
function showPreviousNews() {
    newsIndex = (newsIndex - 1 + newsCount) % newsCount;
    updateNews();
}

// Функция для показа следующей новости
function showNextNews() {
    newsIndex = (newsIndex + 1) % newsCount;
    updateNews();
}

// Функция для обновления отображения новостей
function updateNews() {
    news.forEach((slide, index) => {
        if (index === newsIndex) {
            slide.style.display = 'block';
        } else {
            slide.style.display = 'none';
        }
    });
}

// Инициализация слайдера
updateNews();