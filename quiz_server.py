import socket
from threading import Thread
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = "127.0.0.1"
port = 8000
server.bind((ip_address, port))
server.listen()
client = []
nicknames = []

questions = [
    "What is the Italian word for PIE? \n a.Mozarella \n b.Pasty \n c.Patty \n d. Pizza",
    "Water boils at 212 units at which scale? \n a.Farenheit \n b.Celsius \n c.Rankine \n d.Kelvin",
    "Which sea creature has three hearts? \n a.Dolphin \n b.Octopus \n c.Walrus \n d.Seal",
    "Which is India's first super-computer? \n a.Param8000 \n b.Pratyush \n c.Siddhi \n d.AIRAWAT"
    "How many bones does a human adult have? \n a.206 \n b.208 \n c.201 \n d.196",
    "How many wonders are there in the world? \n a.7 \n b.8 \n c.10 \n d.4",
    "What element does not exist? \n a.Xf \n b.Re \n c.Si \n d.Pa",
    "How many states are there in India? \n a.24 \n b.29 \n c.30 \n d.31",
    "Who invented the telephone? \n a.A.G.Bell \n b.Nikolo Tesla \n c.Thomas Elva Edison \n d.G Marconi",
    "Who is Loki? \n a.God of Thunder \n. b. God of Dwarves \n c.God of Mischeif \n d.God of Gods",
    "Who was the first Indian female astronaut? \n.Sunita Williams \n b.Kalpana Chawla \n c.None of them \n d.Both of them",
    "Which is the smallest continent? \n a.Asia \n b.Antarctica \n c.Afica \n d.Australia",
    "The beaver is the national embelem of which country? \n a.Zimbabwe \n b.Iceland \n c.Argentina \n d.Canada",
    "How many players are on the field in baseball? \n a.6 \n b.7 \n c.9 \n d.8",
    "Hg in the periodic table stands for? \n a.Mercury \n b.Hulgerium \n c.Argenine \n d.Halfnium",
    "Who gifted the Statue of Liberty to USA? \n a.Brazil \n b.France \n c.Germany \n d. Russia",
    "Which planet is closest to the sun? \n a.Mercury \n b.Pluto \n c.Earth \n d.Venus"
]

answers = [
    'd', 'a', 'b', 'a', 'a', 'a', 'a', 'b', 'a', 'c', 'b', 'd', 'd', 'c', 'a', 'b', 'a'
]

def get_random_question_answer(connection):
    random_index = random.randint(0, len(questions)-1)
    random_question = questions[random_index]
    random_answer = answers[random_index]
    connection.send(random_question.encode("utf-8"))
    return random_index, random_question, random_answer


def remove_question(index):
    questions.pop(index)
    answers.pop(index)


def removenickname(nickname):
    if nickname in nicknames:
        nicknames.remove(nickname)

def removeconnection(client):
    if nickname in nicknames:
        nicknames.remove(nickname)

def clientThread(client,nickname):
    score = 0
    client.send("Welcome to this quiz game!".encode("utf-8"))
    client.send("Your will receive a question. The answer to that question should be on of a, b, c or d ".encode("utf-8"))
    client.send("Good Luck!\n\n".encode("utf-8"))
    index, questions, answers = get_random_question_answer(client)

    while True:
        try:
            message = client.recv(2048).decode("utf-8")
            if message:
                if message.lower() == answers:
                    score += 1
                    client.send(f"Bravo! Your score is {score}\n\n".encode("utf-8"))
                else:
                    client.send("Incorrect answer! Better luck next time\n\n".encode("utf-8"))
                remove_question(index)
                index, questions, answers = get_random_question_answer(socket)
            else:
                removeconnection(client)
                removenickname(nickname)
        except:
            continue

while True:
    connection, address = server.accept()
    connection.send("NICKNAME".encode("utf-8"))
    nickname = connection.recv(2048).decode("utf-8")
    client.append(connection)
    nicknames.append(nickname)
    message = "{} joined!".format(nickname)
    print(message)
    new_thread = Thread(target=clientThread, args= (connection,nickname))
    new_thread.start()