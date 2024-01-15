## Chatroom monitor based on sentiment analysis

## Introduction
This is the frontend of our sentiment analysis, presenting users with suggestions through an interface resembling a chatroom. We utilize socket and Flask to connect the frontend and backend. By connecting to the analysis module, the frontend establishes real-time communication with the backend. The results of the sentiment analysis are then provided as feedback to the users.

## Enviroment set up

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

## Usage


1. run `python main.py`
2. Access the home page at http://127.0.0.1:5000.
3. Enter your name, room code (if joining a room), and choose to create or join a room.
4. Start chatting. And you can get some advices of your typing.
