# fast_api_docker

# миграции:
для создания новой миграции:

```
yoyo new migrations
```

для запуска миграций:

```
yoyo apply --database postgresql://postgres:postgres@0.0.0.0:5432/postgres ./migrations -b
```
