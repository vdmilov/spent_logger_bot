# spent_logger_bot
Telegram bot that allows to input family cash expenses, which are automatically logged into a GSheet and later pulled into a custom dashboard in Data Studio, providing insights on spending habits


In order to deploy with Docker, input your token and other envs into docker-compose.yaml:
```
docker build -t spent_logger_bot .

docker-compose up -d
```
