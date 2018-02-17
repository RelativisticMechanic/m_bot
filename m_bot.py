import pygame
import math
import random
import colorsys

display_output = 0
framespersecond = 60
w = 800;
h = 600;
max_iterations = 1000;
real_start = -2;
real_end = 1;
im_start = -1;
im_end = 1;

def draw_pixel(x, y, r, g, b):
        global display_output
        display_output.set_at((x,y), (r,g,b));

def mandelbrot(c):
    z = 0;
    n = 0;
    while abs(z) <= 2 and n < max_iterations:
        z = z*z + c
        n = n + 1
    return n;

def main():
    global display_output, w, h, framespersecond
    r_freq = 0.52;
    g_freq = 0.6;
    b_freq = 0.5;
    phase_r = 0;
    phase_b = 0;
    phase_g = 0;
    # Initialise pygame
    pygame.init();

    display_output = pygame.display.set_mode((w, h))
    pygame.display.set_caption("Rendering the Mandelbrot");

    clock = pygame.time.Clock();

    quit = False;

    # Draw the mandelbrot
    for x in range(0, 800):
        for y in range(0, 600):
            c = complex(real_start + (x/w) * (real_end - real_start), im_start + (y/h)*(im_end - im_start))
            m = mandelbrot(c);
            r = int((math.sin(r_freq*m + phase_r)+1)*255.0/2);
            g = int((math.sin(g_freq*m + phase_g)+1)*255.0/2);
            b = int((math.sin(b_freq*m + phase_b)+1)*255.0/2);
            draw_pixel(x, y, r, g, b);

    while not quit:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        quit = True
        
        pygame.display.flip();
        clock.tick(framespersecond);

    exit(0);
    
main();