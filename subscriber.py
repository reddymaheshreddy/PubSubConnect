import tkinter as tk
import paho.mqtt.client as mqtt

# MQTT broker settings
BROKER = "test.mosquitto.org"  # Use a public broker

# Function to handle incoming messages
def on_message(client, userdata, message):
    tweet = message.payload.decode()
    tweet_list.insert(tk.END, tweet)  # Insert tweet into the list box

# Function to subscribe to a hashtag
def subscribe():
    hashtag = hashtag_entry.get()
    if hashtag:
        client.subscribe(hashtag)
        print(f"Subscribed to: {hashtag}")

# Function to unsubscribe from a hashtag
def unsubscribe():
    hashtag = hashtag_entry.get()
    if hashtag:
        client.unsubscribe(hashtag)
        print(f"Unsubscribed from: {hashtag}")

# Set up MQTT client
client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER)
client.loop_start()  # Start the MQTT loop

# Create the GUI
root = tk.Tk()
root.title("Hashtag Follower")

tk.Label(root, text="Hashtag (Topic):").pack()
hashtag_entry = tk.Entry(root)
hashtag_entry.pack()

subscribe_button = tk.Button(root, text="Subscribe", command=subscribe)
subscribe_button.pack()

unsubscribe_button = tk.Button(root, text="Unsubscribe", command=unsubscribe)
unsubscribe_button.pack()

# List box to display tweets
tweet_list = tk.Listbox(root, width=50, height=10)
tweet_list.pack()

# Start the GUI event loop
root.mainloop()

# Stop the MQTT loop on closing the window
client.loop_stop()
client.disconnect()