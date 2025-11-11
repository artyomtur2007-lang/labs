# сгенерирровать какую то структуру,в которой для каждого пользователя будет храниться его номер карты и его айд,с клавиа
# туры ввод айди и номера карты если есть айд то добавь номер карты если нету айд добавь в структуру клиента
import random
def generator_num():
    return ''.join(str(random.randint(0,9))for _ in range(16))
def generator_id(a):
    return random.randint(1000,9999)
client={}
for _ in range(1,5):
    client_id=generator_id(_)
    num_card=generator_num()
    client[client_id]=num_card

for client_id,card in client.items():
    print(f"{client_id}:{card}")
user_id=input('Введите четырехзначный id: ').strip()
user_num=input('Введите 16значный номер карты: ').strip()

if user_id in client:
    if  client[user_id]==user_num:
        print("Такой клиент и номер уже существует")
    else:
        print("id существует,но карта другая")
        print("Обновляем")
        client[user_id]=user_num
else:
    client[user_id]=user_num
print("обновленное")
for client_id,card in client.items():
    print(f"{client_id}:{card}")