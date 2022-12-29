#include <graphics.h>
#include <iostream.h>
#include <math.h>
#include <dos.h>
#include <conio.h>

void main()
{
    float x, y, x1, y1, x2, y2, dx, dy, step;
    int i, gd = DETECT, gm;

    initgraph(&gd, &gm, "C://TURBOC3//BGI");

    cout << "Enter the value of x1 and y1 : ";
    cin >> x1 >> y1;
    cout << "Enter the value of x2 and y2: ";
    cin >> x2 >> y2;

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
        putpixel(x, y, 5);
        x = x + dx;
        y = y + dy;
        i = i + 1;
        delay(10);
    }
    getch();
    closegraph();
}
