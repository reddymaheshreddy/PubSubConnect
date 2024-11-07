import tkinter as tk
import paho.mqtt.client as mqtt

# MQTT broker settings
BROKER = "test.mosquitto.org"  # Use a public broker

# Function to publish the tweet
def publish_tweet():
    username = username_entry.get()
    tweet_message = tweet_entry.get()
    hashtag = hashtag_entry.get()
    if username and tweet_message and hashtag:
        message = f"{username}: {tweet_message}"
        client.publish(hashtag, message)
        tweet_entry.delete(0, tk.END)  # Clear the tweet entry
        print(f"Tweet published: {message}")

# Set up MQTT client
client = mqtt.Client()
client.connect(BROKER)

# Create the GUI
root = tk.Tk()
root.title("Tweet Poster")

tk.Label(root, text="Username:").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Tweet Message:").pack()
tweet_entry = tk.Entry(root)
tweet_entry.pack()

tk.Label(root, text="Hashtag (Topic):").pack()
hashtag_entry = tk.Entry(root)
hashtag_entry.pack()

publish_button = tk.Button(root, text="Publish Tweet", command=publish_tweet)
publish_button.pack()

# Start the GUI event loop
root.mainloop()