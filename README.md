# friendly_terminal
We spend all day in the terminal, so why not have it say nice things to you to start your day off right?  Using friendly_terminal, you terminal will display a random motivational message from a selection you have created.

Set up takes ~10 minutes and you too can have friendly messages *every joyous day*.

## Installation
This program consists of three parts (two that you are likely to want to modify):
- A text file of affirmations that you will have selected.
- A Python file that will select a random affirmation from your text file.
- An added line in your .bash_profile that prints the selected affirmation when the terminal is opened.
Let's get started!

###Find or create your .bash_profile
To search for your .bash_profile using your terminal, type <code>find ~/ -type f -name ".bash_profile"</code>.  This will search your home directory (where your bash profile is likely stored) for a file called .bash_profile.  Using Mac's Spotlight will strip the "." before searching and this will make you sad.
If you do not have a .bash_profile, navigate to your home directory and (in your terminal) type <code><your editor of choice> .bash_profile</code> to create and open the file.

In your .bash_profile, add <code>python3 /Users/<username>/randline.py /Users/<username>/quotes_for_terminal.txt</code>

To create a new .bash_profile, 
(a) navigate to your user folder <code>cd /Users/<username>/</code>
(b) create file with <code>touch .bash_file</code>
(c) open file with your favorite editor and go to town!

<a href='http://www.recurse.com' title='Made with love at the Recurse Center'><img src='https://cloud.githubusercontent.com/assets/2883345/11325206/336ea5f4-9150-11e5-9e90-d86ad31993d8.png' height='20px'/></a>
