from flask import Flask, render_template

from paho.mqtt import client as mqtt_client

app = Flask(__name__)
broker = 'broker.emqx.io'
port = 1883
topic = 'topicName/iot'

client_id = 'test'
username = 'emqx'
password = ''

def connect_mqtt():
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.connect(broker, port)
    return client

@app.route('/')
def index():
	return render_template('index.html')
@app.route('/main',methods=['POST'])
def test1():
	client = connect_mqtt()
	client.loop_start()
	send_1_data(client)
	return render_template('index.html')

def test2():
	client = connect_mqtt()
	client.loop_start()
	send_2_data(client)

def test3():
	client = connect_mqtt()
	client.loop_start()
	send_3_data(client)

def test4():
	client = connect_mqtt()
	client.loop_start()
	send_4_data(client)

def test5():
	client = connect_mqtt()
	client.loop_start()
	send_5_data(client)

def test6():
	client = connect_mqtt()
	client.loop_start()
	send_6_data(client)

def test7():
	client = connect_mqtt()
	client.loop_start()
	send_7_data(client)

def test8():
	client = connect_mqtt()
	client.loop_start()
	send_8_data(client)

def test9():
	client = connect_mqtt()
	client.loop_start()
	send_9_data(client)

def plus_test():
	client = connect_mqtt()
	client.loop_start()
	send_plus_data(client)

def minus_test():
	client = connect_mqtt()
	client.loop_start()
	send_minus_data(client)

def multiply_test():
	client = connect_mqtt()
	client.loop_start()
	send_multiply_data(client)

def division_test():
	client = connect_mqtt()
	client.loop_start()
	send_division_data(client)

def equal_test():
	client = connect_mqtt()
	client.loop_start()
	send_equal_data(client)

def C_test():
	client = connect_mqtt()
	client.loop_start()
	send_C_data(client)




def send_1_data(client):
	msg = "1"
	result = client.publish(topic, msg)
	status = result[0]
	if status == 0:
		print(f"Send {msg} to topic {topic}")

def send_2_data(client):
	msg = "2"
	result = client.publish(topic, msg)
	status = result[0]
	if status == 0:
		print(f"Send {msg} to topic {topic}")

def send_3_data(client):
	msg = "3"
	result = client.publish(topic, msg)
	status = result[0]
	if status == 0:
		print(f"Send {msg} to topic {topic}")

def send_4_data(client):
	msg = "4"
	result = client.publish(topic, msg)
	status = result[0]
	if status == 0:
		print(f"Send {msg} to topic {topic}")

def send_5_data(client):
	msg = "5"
	result = client.publish(topic, msg)
	status = result[0]
	if status == 0:
		print(f"Send {msg} to topic {topic}")

def send_6_data(client):
	msg = "6"
	result = client.publish(topic, msg)
	status = result[0]
	if status == 0:
		print(f"Send {msg} to topic {topic}")

def send_7_data(client):
	msg = "7"
	result = client.publish(topic, msg)
	status = result[0]
	if status == 0:
		print(f"Send {msg} to topic {topic}")

def send_8_data(client):
	msg = "8"
	result = client.publish(topic, msg)
	status = result[0]
	if status == 0:
		print(f"Send {msg} to topic {topic}")

def send_9_data(client):
	msg = "9"
	result = client.publish(topic, msg)
	status = result[0]
	if status == 0:
		print(f"Send {msg} to topic {topic}")

def send_plus_data(client):
	msg = "+"
	result = client.publish(topic, msg)
	status = result[0]
	if status == 0:
		print(f"Send {msg} to topic {topic}")

def send_minus_data(client):
	msg = "-"
	result = client.publish(topic, msg)
	status = result[0]
	if status == 0:
		print(f"Send {msg} to topic {topic}")

def send_division_data(client):
	msg = "/"
	result = client.publish(topic, msg)
	status = result[0]
	if status == 0:
		print(f"Send {msg} to topic {topic}")

def send_multiply_data(client):
	msg = "*"
	result = client.publish(topic, msg)
	status = result[0]
	if status == 0:
		print(f"Send {msg} to topic {topic}")

def send_equal_data(client):
	msg = "="
	result = client.publish(topic, msg)
	status = result[0]
	if status == 0:
		print(f"Send {msg} to topic {topic}")

def send_C_data(client):
	msg = "C"
	result = client.publish(topic, msg)
	status = result[0]
	if status == 0:
		print(f"Send {msg} to topic {topic}")

if __name__ == "__main__":
    app.run(port=5001)