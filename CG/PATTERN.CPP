#include <iostream.h>
#include <graphics.h>
#include <conio.h>
#include <dos.h>
#include <math.h>

void drawline(int x1, int y1, int x2, int y2)
{
    float x, y, dx, dy, step;
    int i;

    dx = (x2 - x1);
    dy = (y2 - y1);

    if (abs(dx) >= abs(dy))
        step = dx;
    else
        step = dy;

    dx = dx / step;
    dy = dy / step;

    x = x1;
    y = y1;

    i = 1;
    while (i <= step)
    {
        putpixel(x, y, YELLOW);
        x = x + dx;
        y = y + dy;
        i = i + 1;
        delay(4);
    }
}

void drawcircle(float x0, float y0, float radius)
{
    float x = radius;
    float y = 0;
    float err = 0;

    while (x >= y)
    {
        putpixel(x0 + x, y0 + y, YELLOW);
        putpixel(x0 + y, y0 + x, YELLOW);
        putpixel(x0 - y, y0 + x, YELLOW);
        putpixel(x0 - x, y0 + y, YELLOW);
        putpixel(x0 - x, y0 - y, YELLOW);
        putpixel(x0 - y, y0 - x, YELLOW);
        putpixel(x0 + y, y0 - x, YELLOW);
        putpixel(x0 + x, y0 - y, YELLOW);
        delay(10);

        if (err <= 0)
        {
            y += 1;
            err += 2 * y + 1;
        }

        if (err > 0)
        {
            x -= 1;
            err -= 2 * x + 1;
        }
    }
}

int main()
{
    int gd = DETECT, gm;
    float r;
    initgraph(&gd, &gm, "C://TURBOC3//BGI");

    // Rectangle
    drawline(200, 200, 600, 200);
    drawline(600, 200, 600, 350);
    drawline(200, 350, 600, 350);
    drawline(200, 200, 200, 350);

    // Rhombus
    drawline(400, 200, 600, 275);
    drawline(400, 350, 600, 275);
    drawline(200, 275, 400, 350);
    drawline(200, 275, 400, 200);

    // Circle
    r = (float)400 * 150 / (2 * sqrt((pow(400, 2) + pow(150, 2))));
    drawcircle(400, 275, r);
    getch();

    return 0;
}