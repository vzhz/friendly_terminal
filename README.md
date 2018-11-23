# Friendly Terminal
<a href='http://www.recurse.com' title='Made with love at the Recurse Center'><img src='https://cloud.githubusercontent.com/assets/2883345/11325206/336ea5f4-9150-11e5-9e90-d86ad31993d8.png' height='20px'/></a>

We spend all day in the terminal, so why not have it say nice things to you to start your day off right?  Using Friendly Terminal, you terminal will display a random motivational message from a selection you have created.

![Imagine this greeting you every morning. : )](https://github.com/vzhz/friendly_terminal/blob/master/friendly_terminal_preview.png)

Set up takes ~10 minutes and you too can have friendly messages *every joyous day*.

## Installation
This program consists of three parts (two that you are likely to want to modify):
- A text file of affirmations that you will have selected.
- A Python file that will select a random affirmation from your text file.
- An added line in your .bash_profile that prints the selected affirmation when the terminal is opened.
Let's get started!

You will:
- Clone this repo
- Try out the program (optional)
- Add program to your .bash_profile
- Add quotes & randline file to home directory
- Open a fresh terminal & smile!
- Customize your quotes (optional)

### Clone this repo
Navigate to your home directory <code>/Users/*username*/</code> and clone this repo. In the terminal, navigating to your home directory can be done with <code>cd ~/</code>.
```
cd ~
git clone https://github.com/vzhz/friendly_terminal.git
```
Anywhere you see <code>/Users/*username*/</code>, you can use a <code>~/</code> instead.

### Try it out
**(optional)**

If you haven't already used it for the first step, find your shell (e.g. you may be using [zshrc]() or bash) and add 
```
python3 /Users/username/friendly_terminal/randline.py /Users/username/friendly_terminal/quotes_for_terminal.txt [your name]</code>
```
Substitute the name you would like to be greeted by for <code>[your name]</code>!
Your terminal will return one greeting each time you run this command, so run it as many times as you like to preview your encouraging phrases.

### Add program to your .bash_profile
Navigate to your home directory and open your .bash_profile using your terminal:
```
cd ~
editor_name .bash_profile
```

If you need to search for your file you can do so with <code>find ~/ -type f -name ".bash_profile"</code>. This will search your home directory (where your bash profile is likely stored) for a file called .bash_profile.  Using Mac's Spotlight will strip the "." before searching and you won't find your file.
If you do not have a .bash_profile, navigate to your home directory and (in your terminal) type <code>*your editor of choice* .bash_profile</code> to create and open the file.

Once you open your .bash_profile, add 
```
<code>python3 /Users/<username>/randline.py /Users/<username>/quotes_for_terminal.txt</code> [your name]
```
the same way you did in your terminal earlier. If you haven't already, you're likely to be adding lots of customizations to your .bash_profile in the future, so it would be a good idea to add a comment explaining that this line runs the Friendly Terminal app!

### Add quotes & randline to home directory
Either drag-and-drop or use your terminal:
```
cd friend_terminal/
cp randline.py quotes_for_terminal.txt ~/
```

### Open a new terminal & smile!
It should say something nice to you!

### Add your favorite nice things to your text file
**(optional)**

Make your terminal say whatever will make you feel good. The text file starts with a few encouraging phrases. My favorite is "you look very nice tonight and you are very smart" but some people might be motivated by a nice "get to work, you fucker."  You do you. This is optional - there are lots of good phrases in there already!

Hurrah! Now you have a (even) friendly(er) terminal!  

## Contributing
We welcome your contributions in pretty much any form. 

**Have an idea for expanding Friendly Terminal?** Create [an issue](https://github.com/vzhz/friendly_terminal/issues) (or comment on an existing one)!

**Want to make your own modifications and share what you've done?** Fork & get started on a pull request. ([This repo](https://github.com/firstcontributions/first-contributions) has a step-by-step guide to for using Github as a first-time contributor). (Feel free to open [an issue](https://github.com/vzhz/friendly_terminal/issues) so we can start a conversation about your plans too!)

## License
Friendly Terminal is released under [the MIT license](https://github.com/vzhz/friendly_terminal/blob/master/LICENSE.txt).
