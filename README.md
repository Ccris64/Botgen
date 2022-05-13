# Botgen - A bot generator, made in Python.
Hey! This is my first project made in Python and my first program uploaded to Github.

### How it works
Botgen generates a bot with a random name stored on a list and uses a dict stored on a file called dictionary.bot to read input and reply.
When I say that it's highly customizable, I mean that its easy to someone edit the dictionary.bot and customize the bot.

As I said, dictionary.bot is a python **dict** and its readed by the **json module**.
You can add as much commands as you want. Each command is separated by a comma and needs the input and output. It should look like this: {"command":"reply"}.

A ***very important*** note: Write the commands in that file in lowercase, or else you will not be able to run.

## Bot in action:

![image](https://user-images.githubusercontent.com/93295652/168388534-04aaac5d-efd5-4076-a6a0-8ce14883b6e8.png)
