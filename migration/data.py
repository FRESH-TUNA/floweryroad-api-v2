import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), 'connection.env')
load_dotenv(dotenv_path)

new_db_data = {
    "db_name": os.getenv('NEW_DB_NAME'),
    "db_user": os.getenv('NEW_DB_USER'),
    "db_password": os.getenv('NEW_DB_PASSWORD'),
    "db_host": os.getenv('NEW_DB_HOST'),
    "db_port": os.getenv('NEW_DB_PORT')
}

db_data = {
    "db_name": os.getenv('DB_NAME'),
    "db_user": os.getenv('DB_USER'),
    "db_password": os.getenv('DB_PASSWORD'),
    "db_host": os.getenv('DB_HOST'),
    "db_port": os.getenv('DB_PORT')
}

old_data_tables = [
    "public.core_flower",
    "public.core_comment",
    "public.core_image",
    "public.core_language",
    "public.core_purpose",
    "public.core_view",
    "public.core_color",
    "public.core_commentlike",
    "public.core_flower_colors",
    "public.core_flower_languages",
    "public.core_flower_purposes",
]

new_data_tables = [
    "public.app_flower",
    "public.app_comment",
    "public.app_image",
    "public.app_language",
    "public.app_purpose",
    "public.app_view",
    "public.app_color",
    "public.app_commentlike",
    "public.app_flower_colors",
    "public.app_flower_languages",
    "public.app_flower_purposes",
]
