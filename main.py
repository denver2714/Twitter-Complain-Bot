from InternetSpeedTwitterBot import InternetSpeedTwitterBot
from dotenv import load_dotenv, dotenv_values


load_dotenv()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.complain_via_twitter()