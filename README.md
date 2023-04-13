# spent_logger_bot
Telegram bot that allows to input family cash expenses, which are automatically logged into a GSheet and later pulled into a custom dashboard in Data Studio, providing insights on spending habits

![image](https://user-images.githubusercontent.com/104202715/231747295-52755ec2-ae17-4c51-933c-97e686d85869.png)
![image](https://user-images.githubusercontent.com/104202715/231747580-b45997dc-42a7-48e3-bdc5-27695444367d.png)


In order for the bot to input the spendings in your Google Sheet, you need to generate credentials that are used to obtain an access token from Google's authorization servers so your bot can call Google Workspace APIs. You can get those using this [guide](https://developers.google.com/workspace/guides/create-credentials?hl=en). 


In order to deploy with Docker, input your token and other envs into docker-compose.yaml:
```
docker build -t spent_logger_bot .

docker-compose up -d
```
