## Chatroom monitor based on sentiment analysis

### Overview
[![Alt text for your video](http://img.youtube.com/vi/XrVSxAahRg8/0.jpg)](https://www.youtube.com/watch?v=XrVSxAahRg8)
This frontend demo application is designed to provide real-time sentiment analysis feedback to users in a chatroom-like interface. 
It leverages the power of Socket.IO and Flask to establish a seamless communication channel between the frontend and backend.

### Key Features

* Real-time Sentiment Analysis
* Intuitive Interface
* Robust Backend Integration
* Efficient Communication

### How it Works

1. **User Input:** The user enters text into the chat input field.
2. **Frontend Processing:** The frontend sends the input text to the backend via a Socket.IO message.
3. **Backend Analysis:** The backend sentiment analysis module processes the text and determines the sentiment.
4. **Result Transmission:** The backend sends the sentiment analysis result back to the frontend via Socket.IO.
5. **Frontend Display:** The frontend displays the sentiment analysis result in the chat interface.

### Technical Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Flask, Socket.IO

### Getting Started
Install torch>2.0 with your CUDA version

Install the corresponding transformers

> We use torch==2.1.1 and transformers==4.36.2

```
cd chatroom_demo
pip install -r requirments.txt
```

Download the checkpoint from

https://drive.google.com/file/d/1f2PraeSnAcOMcknXZ92KpAzmgnvK80ff/view?usp=drive_link

and place it under current directory.

