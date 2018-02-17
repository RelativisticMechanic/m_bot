# m_bot
Tiny Mandelbrot Renderer.<br>

A mandelbrot usually refers to a set of complex numbers defined by the sequence Z(n+1) = Z(n) + c * c which do not diverge (starting from zero) to no further than 2 even when iterated through a large number of times. <br>

Plotting these on the Argand plane gives... rather interesting results:
![Rendering the Mandelbrot!](https://i.imgur.com/7nXDnL1.png) <br>

This is the result obtained by rendering from Re: -2 to 1, Im: i to -i, with 1000 iterations per number on a 800 by 600 screen. Better results can be obtained if you start rendering specific areas of the mandelbrot. This ran rather slow on a i5 - 8250U, I guess I'll port it to cython for native execution so as to make it significantly faster.

- S, Gautam.
