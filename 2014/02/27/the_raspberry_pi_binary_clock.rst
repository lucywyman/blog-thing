The Raspberry Pi Binary Clock
=============================


Pre-Project Bonus

This Week I did a few bonus projects:

- The code for this website is now in a repository on `Github
  <https://github.com/about>`_. Click the link to check it out. I'll try to
  update the `repository <https://github.com/elijahcaine/blog.elijahcaine.me>`_
  weekly.
- I have also added a `RSS <https://en.wikipedia.org/wiki/Rss>`_ subscription
  feed to this project. You should subscribe by pressing the link above. If you
  don't currently use an RSS service, I suggest `Feedly <http://feedly.com/>`_.

So I've got this *thing*.

.. image:: http://i.imgur.com/b6wwU9Z.jpg
    :target: http://www.raspberrypi.org/
    :height: 300px
    :align: center

It's called a Raspberry Pi, and it's a credit-card sized mini computer designed
with hacking projects in mind. Some call it a RasPi.

.. image:: http://elinux.org/images/6/61/RPi_P1_header.png
    :target: http://elinux.org/RPi_Low-level_peripherals
    :height: 100px
    :align: center

The RasPi has these things called General Purpose Input/Output pins (GPIO)
which can be used for recording data and triggering electronics through the
RasPi. These are the major difference between a RasPi and a 'normal' computer.

A few weeks ago I acquired some LED's...

.. image:: http://upload.wikimedia.org/wikipedia/commons/f/f9/LED%2C_5mm%2C_green_%28en%29.svg
    :target: http://en.wikipedia.org/wiki/Light-emitting_diode
    :height: 300px
    :align: center

... Jumper Wires...

.. image:: http://upload.wikimedia.org/wikipedia/commons/5/5c/A_few_Jumper_Wires.jpg
    :target: http://en.wikipedia.org/wiki/Jump_wire
    :height: 300px
    :align: center

... and a Bread Board.

.. image:: http://upload.wikimedia.org/wikipedia/commons/7/73/400_points_breadboard.jpg
    :target: http://en.wikipedia.org/wiki/Breadboard
    :height: 300px
    :align: center

I combined these to make ~~Voltron~~ `a binary
clock <https://en.wikipedia.org/wiki/Binary_clock>`_.

.. image:: http://i.imgur.com/T7HBEH9.jpg
    :height: 300px
    :align: center

Here's a quick rundown of how I designed my Binary Clock:

The five lights on the left are for displaying the hour. In binary those lights
can represent 31 numbers, but I only needed 24.

Pretty cool right? Not yet! You haven't heard the best part.

The right most LED conveys the minute of the hour. The faster it blinks, the
later into the hour you are.

Initially I wasn't confident in how many LED's I would be able control for the
clock, so I had the bright idea to try and display the minute of the hour using
a single LED! To accomplish this I wrote an algorithm which caused the LED to
blink once per second at the top of the hour and blink so fast it was just on
at the end of the hour, naturally progressing over the course of 60 minutes.

*Eli. That sounds a bit sketchy. How would do you actually know the minute?
It's just a blinking light!*

I was worried too, so I showed my project to a friend, gave them a quick rundown
of how it worked, and asked them to make an educated guess as to what the time
was. To my pleasant surprise they guessed it correctly to an accuracy of five
minutes!

Now *that's* cool.

This project was the first time that I got really excited about information
theory and the idea of conveying complex information in as few 'bits' as
possible. The system described above is a trade-off between accuracy and using
as little 'space' as possible.

My initial goal, which I accomplished, was to represent accurate-enough time
using less than 9 LED lights. The system described above could work with only 6
bits, but I went with a 24 hour time base instead of 12.

After I had completed the clock and figured out how to control them with `Shell
Commands <https://en.wikipedia.org/wiki/Unix_shell>`_ over
`SSH <https://en.wikipedia.org/wiki/Secure_Shell>`_, allowing me to turn the
clock on and off from my laptop, I had a bunch of extra LEDs and nothing useful
to do with them. I strung them up behind my computer monitors, thus creating an
atmospheric back-light.

.. image:: http://i.imgur.com/gJfGgsu.jpg
    :align: center
    :height: 300px

*Thank you for reading,- Elijah*

.. image:: http://i.imgur.com/A1msThZ.jpg
    :align: center
    :height: 300px

.. image:: http://i.imgur.com/gdcp9YI.jpg
    :align: center
    :height: 300px

.. image:: http://i.imgur.com/FT6EflS.jpg
    :align: center
    :height: 300px

.. author:: default
.. categories:: p52
.. tags:: archive backlog project52
