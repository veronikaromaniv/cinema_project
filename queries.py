import django
import os

# Налаштування середовища Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinema.settings')
django.setup()

from movies.models import Genre, Director, Movie, Review
from django.db.models import Count, Avg, Min, Max, Q, F


# РОЗДІЛ 7. ORM-ЗАПИТИ

# Завдання 1 — Базова вибірка
# Отримуємо всі об'єкти фільмів та список лише їхніх назв
movies = Movie.objects.all()
titles = Movie.objects.values_list("title", flat=True)
print("Список назв фільмів:", list(titles))


# Завдання 2 — Фільтрація за рейтингом
# Фільтруємо фільми з рейтингом >= 8.5 та сортуємо від найвищого
top_movies = Movie.objects.filter(rating__gte=8.5).order_by("-rating")
print("\nТоп фільми (8.5+):")
for m in top_movies:
    print(f"{m.title}: {m.rating}")


# Завдання 3 — Пошук по тексту з Q-об'єктами
# Пошук фільмів, назва яких містить "Blade" АБО "Dark"
result_q = Movie.objects.filter(
    Q(title__icontains="Blade") | Q(title__icontains="Dark")
)
print("\nПошук 'Blade' або 'Dark':", [m.title for m in result_q])


# Завдання 4 — Фільтр через зв'язану таблицю
# Знаходимо всі фільми Крістофера Нолана через поле прізвища в моделі Director
nolan_films = Movie.objects.filter(director__last_name="Nolan")
print(f"\nКількість фільмів Нолана: {nolan_films.count()}")


# Завдання 5 — Комбінована фільтрація
# Sci-Fi фільми, що вийшли після 2015 року, відсортовані за роком
scifi_recent = Movie.objects.filter(
    genre__name="Sci-Fi",
    year__gt=2015
).order_by("year")


# Завдання 6 — exclude()
# Фільми, жанр яких НЕ Drama і НЕ Comedy
not_drama_comedy = Movie.objects.exclude(
    Q(genre__name="Drama") | Q(genre__name="Comedy")
)
print("\nФільми (не драма/комедія):")
for m in not_drama_comedy:
    print(f"{m.title} — {m.genre.name if m.genre else 'без жанру'}")


# Завдання 7 — Пагінація
# Розподіл фільмів на сторінки по 4 об'єкти за рейтингом
by_rating = Movie.objects.order_by("-rating")
page1 = by_rating[:4]  # Перші 4
page2 = by_rating[4:8] # Наступні 4


# Завдання 8 — Кількість фільмів у кожному жанрі
# Групування за жанром та підрахунок кількості фільмів
genres_stat = Genre.objects.annotate(
    movie_count=Count("movie")
).order_by("-movie_count")
print("\nСтатистика за жанрами:")
for g in genres_stat:
    print(f"{g.name}: {g.movie_count}")


# Завдання 9 — Середній рейтинг
# Загальний середній рейтинг та середній рейтинг по кожному режисеру
total_avg = Movie.objects.aggregate(avg=Avg("rating"))
print(f"\nЗагальний середній рейтинг: {total_avg['avg']}")

directors_avg = Director.objects.annotate(
    avg_rating=Avg("movie__rating")
).values("last_name", "avg_rating").order_by("-avg_rating")
print("Рейтинг режисерів:", list(directors_avg))

# Завдання 10 — Фільми без відгуків
# Пошук фільмів, де кількість пов'язаних відгуків дорівнює нулю
no_reviews = Movie.objects.annotate(
    review_count=Count("review")
).filter(review_count=0)
print("\nФільми без відгуків:", [m.title for m in no_reviews])


# Завдання 11 — Масовий UPDATE
# Встановлення is_public=False для фільмів з рейтингом нижче 7.8
updated_count = Movie.objects.filter(rating__lt=7.8).update(is_public=False)
print(f"\nОновлено публічність: {updated_count} фільмів")


# Завдання 12 — Оновлення через F()
# Масове підвищення рейтингу фільмів Тарантіно на 0.2 без завантаження в Python
Movie.objects.filter(
    director__last_name="Tarantino"
).update(rating=F("rating") + 0.2)


# Завдання 13 — Відгуки конкретного фільму
# Отримання всіх відгуків та середньої оцінки для "Inception"
inception = Movie.objects.get(title="Inception")
reviews = inception.review_set.all()
avg_score = inception.review_set.aggregate(avg=Avg("score"))
print(f"\nВідгуки на Inception (Середня: {avg_score['avg']}):")
for r in reviews:
    print(f"- {r.score}/10: {r.text}")


# Завдання 14 — Найкращий режисер за середнім рейтингом
# Знаходимо режисера з найвищим середнім показником рейтингу фільмів
top_director = Director.objects.annotate(
    avg=Avg("movie__rating")
).order_by("-avg").first()
if top_director:
    print(f"\nНайкращий режисер: {top_director.first_name} {top_director.last_name} ({top_director.avg})")


# Завдання 15 — Власний запит
# Знайти найстаріший та найновіший фільми в базі
movie_ages = Movie.objects.aggregate(
    oldest=Min("year"),
    newest=Max("year")
)
print(f"\nДіапазон років у базі: {movie_ages['oldest']} — {movie_ages['newest']}")