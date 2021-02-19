#!/home/hpoyatos/venv/bin/python3

import config

import requests 
import telebot
from telebot import types
import pymysql

conn = pymysql.connect(host=config.MYSQL_HOST, 
user=config.MYSQL_USER, 
passwd=config.MYSQL_PASSWD,
db=config.MYSQL_DATABASE) 

from datetime import datetime

bot = telebot.TeleBot(config.FIAPONBOT_API_TOKEN)

try:

    with conn.cursor() as cur:
        sql = "SELECT nome, telegram_username, genero FROM 1tdco2021.alunos WHERE MONTH(dt_nasc)={} AND DAY(dt_nasc) = {}".format(datetime.now().month, datetime.now().day)
        cur.execute(sql)
        rows = cur.fetchall()

        for row in rows:
            if row[1] != None:
                telegram_username = "("+row[1]+")"
            else:
                telegram_username = ""

            frase = "Bom dia, pessoal! Hoje é aniversário d{} {} {}! Meus parabéns, muitas felicidades, saúde e sucesso!".format(("o aluno" if row[2] == 1 else "a aluna"), row[0], telegram_username)
            print(f'{row[0]} {row[1]}')
            channel = bot.send_message(config.CHANNEL_1TDCO2021_ID, frase)

finally:
    conn.close()

