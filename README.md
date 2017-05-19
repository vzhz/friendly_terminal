# Friendly Terminal
<a href='http://www.recurse.com' title='Made with love at the Recurse Center'><img src='https://cloud.githubusercontent.com/assets/2883345/11325206/336ea5f4-9150-11e5-9e90-d86ad31993d8.png' height='20px'/></a>

We spend all day in the terminal, so why not have it say nice things to you to start your day off right?  Using friendly_terminal, you terminal will display a random motivational message from a selection you have created.

![Imagine this greeting you every morning. : )](https://github.com/vzhz/friendly_terminal/blob/master/friendly_terminal_preview.png)

Set up takes ~10 minutes and you too can have friendly messages *every joyous day*.

## Installation
This program consists of three parts (two that you are likely to want to modify):
- A text file of affirmations that you will have selected.
- A Python file that will select a random affirmation from your text file.
- An added line in your .bash_profile that prints the selected affirmation when the terminal is opened.
Let's get started!

### Clone this repo
Navigate to your home directory <code>/Users/*username*/</code> and clone this repo.

### Find your shell
Find your shell (e.g. you may be using [zshrc]() or bash) and add <code>python3 /Users/*username*/friendly_terminal/randline.py /Users/*username*/friendly_terminal/quotes_for_terminal.txt [your name]</code>, of course substituting the name you would like to be greeted by for <code>[your name]</code>.

#### Troubleshooting
To search for your .bash_profile using your terminal, type <code>find ~/ -type f -name ".bash_profile"</code>.  This will search your home directory (where your bash profile is likely stored) for a file called .bash_profile.  Using Mac's Spotlight will strip the "." before searching and this will make you sad.
If you do not have a .bash_profile, navigate to your home directory (<code>/Users/*username*/</code>) and (in your terminal) type <code>*your editor of choice* .bash_profile</code> to create and open the file.

### Add your favorite nice things to your text file
Make your terminal say whatever will make you feel good. The text file starts with a few encouraging phrases. My favorite is "you look very nice tonight and you are very smart" but some people might be motivated by a nice "get to work, you fucker."  You do you.

Now you are ready to open yourself a fresh terminal and smile.  

## Contributing
We welcome your contrubutions in pretty much any form.  Create an issue or clone and go to town on a pull request.

## License
friendly_terminal is released under [the MIT license](https://github.com/vzhz/friendly_terminal/blob/master/LICENSE.txt).
