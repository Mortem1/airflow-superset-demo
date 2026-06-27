# ETL-пайплайн продаж с Airflow и дашбордом в Superset

## Описание
Проект демонстрирует полный цикл обработки данных: 
- Генерация тестовых данных о продажах.
- Обработка с помощью Python (Pandas).
- Агрегация и загрузка в PostgreSQL.
- Визуализация в Superset.

Всё работает в контейнерах Docker, запускается одной командой.

## Технологии
- Apache Airflow (оркестрация)
- PostgreSQL (хранилище)
- Apache Superset (визуализация)
- Python (Pandas, psycopg2)
- Docker Compose

## Как запустить проект (Windows)

1. Установите Docker Desktop
Скачайте и установите [Docker Desktop для Windows](https://www.docker.com/products/docker-desktop/).
Убедитесь, что в настройках Docker включена поддержка WSL2 (это делается автоматически при установке).
Запустите Docker Desktop и дождитесь, пока он полностью загрузится (иконка кита в трее станет стабильной).

2. Клонируйте репозиторий
Откройте командную строку (cmd) и выполните:
git clone https://github.com/Mortem1/airflow-superset-demo.git
cd airflow-superset-demo

3. Создайте файл .env с секретными ключами
В папке проекта есть файл-шаблон .env.example. Скопируйте его в .env:
copy .env.example .env
Откройте .env в Блокноте и заполните значения:

AIRFLOW_UID=50000 оставьте как есть.
FERNET_KEY= сгенерируйте ключ командой docker run --rm apache/airflow:2.10.0 python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
SUPERSET_SECRET_KEY= придумайте любую сложную строку, например my_very_strong_secret_key_2026.

4. Запустите все контейнеры
docker compose up -d

5. Проверьте, что всё поднялось
Откройте в браузере:

Airflow: http://localhost:8080
Логин: admin
Пароль: admin

Superset: http://localhost:8088
При первом входе создайте администратора (логин/пароль задайте сами).

6.Запустите DAG в Airflow
В интерфейсе Airflow найдите DAG sales_pipeline_organized
Включите его (переключатель On) и ажмите кнопку Trigger DAG
Дождитесь выполнения всех задач

7. Проверьте дашборд в Superset

После запуска контейнеров откройте http://localhost:8088.
Логин/пароль: admin / admin (если вы не меняли).
Дашборд уже будет импортирован автоматически.
Если данные ещё не отображаются, запустите DAG в Airflow (шаг 6), затем обновите дашборд.
