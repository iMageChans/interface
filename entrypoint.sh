#!/bin/sh

# 等待数据库服务启动
while ! nc -z db 5432; do
  echo "Waiting for PostgreSQL..."
  sleep 1
done

while ! nc -z redis 6379; do
  echo "Waiting for Redis..."
  sleep 2
done

# 运行数据库迁移
python manage.py migrate

# 启动 Django 应用
exec "$@"
