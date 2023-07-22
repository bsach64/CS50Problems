#include "helpers.h"
#include <math.h>

void swap(RGBTRIPLE *a, RGBTRIPLE *b);

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Loops over all pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Calculates the average of the Red, Green and Blue value of each Pixel
            float grey = (image[i][j].rgbtBlue + image[i][j].rgbtRed + image[i][j].rgbtGreen) / 3.0;
            // Rounds the average to closest integer
            float gr = roundf(grey);
            int gi = gr;
            // limits avg to 255 & assigns red, green and blue the same value
            if (gi <= 255)
            {
                image[i][j].rgbtBlue = gi;
                image[i][j].rgbtRed = gi;
                image[i][j].rgbtGreen = gi;
            }
            else if (gi > 255)
            {
                gi = 255;
                image[i][j].rgbtBlue = gi;
                image[i][j].rgbtRed = gi;
                image[i][j].rgbtGreen = gi;
            }
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // Loops over all pixels
    for (int k = 0; k < height; k++)
    {
        for (int p = 0; p < width; p++)
        {
            // Applies the sepia formula
            float sepiaRed = 0.393 * image[k][p].rgbtRed + 0.769 * image[k][p].rgbtGreen + 0.189 * image[k][p].rgbtBlue;
            float sepiaGreen = 0.349 * image[k][p].rgbtRed + 0.686 * image[k][p].rgbtGreen + 0.168 * image[k][p].rgbtBlue;
            float sepiaBlue = 0.272 * image[k][p].rgbtRed + 0.534 * image[k][p].rgbtGreen + 0.131 * image[k][p].rgbtBlue;
            // rounds to integer and limits it to 255
            float srf = roundf(sepiaRed);
            int sri = srf;
            if (sri <= 255)
            {
                image[k][p].rgbtRed = sri;
            }
            else if (sri > 255)
            {
                sri = 255;
                image[k][p].rgbtRed = sri;
            }
            float sgf = roundf(sepiaGreen);
            int sgi = sgf;
            if (sgi <= 255)
            {
                image[k][p].rgbtGreen = sgi;
            }
            else if (sgi > 255)
            {
                sgi = 255;
                image[k][p].rgbtGreen = sgi;

            }
            float sbf = roundf(sepiaBlue);
            int sbi = sbf;
            if (sbi <= 255)
            {
                image[k][p].rgbtBlue = sbi;
            }
            else if (sbi > 255)
            {
                sbi = 255;
                image[k][p].rgbtBlue = sbi;
            }

        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int q = 0; q < height; q++)
    {
        // swaps pixels depending on parity of width
        if (width % 2 == 0)
        {
            for (int u = 0; u < width / 2; u++)
            {
                swap(&image[q][u], &image[q][width - u - 1]);
            }
        }
        else if (width % 2 != 0)
        {
            for (int w = 0; w < width - 2; w++)
            {
                swap(&image[q][w], &image[q][width - w - 1]);
            }
        }
    }
    return;
}

// Swap function used for reflect
void swap(RGBTRIPLE *a, RGBTRIPLE *b)
{
    RGBTRIPLE tmp = *a;
    *a = *b;
    *b = tmp;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // creates a copy of the image
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            RGBTRIPLE tmp = image[i][j];
            copy[i][j] = tmp;
        }
    }

    float Pixels = 0;
    int PixelRed = 0;
    int PixelGreen = 0;
    int PixelBlue = 0;
    // Loops over all pixels
    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < width; w++)
        {
            // loops for the pixel and all neighbouring pixels and adds their RGB values
            for (int hn = -1; hn < 2; hn++)
            {
                if (h + hn >= 0 && h + hn < height)
                {
                    for (int wn = -1; wn < 2; wn++)
                    {
                        if (w + wn >= 0 && w + wn < width)
                        {
                            PixelRed = PixelRed + copy[h + hn][w + wn].rgbtRed;
                            PixelGreen = PixelGreen + copy[h + hn][w + wn].rgbtGreen;
                            PixelBlue = PixelBlue + copy[h + hn][w + wn].rgbtBlue;
                            Pixels = Pixels + 1;
                        }
                    }
                }
            }
            // calculates the avg for RGB values
            int PRI = round(PixelRed / Pixels);
            int PGI = round(PixelGreen / Pixels);
            int PBI = round(PixelBlue / Pixels);
            // Assigns the avg value
            image[h][w].rgbtRed = PRI;
            image[h][w].rgbtGreen = PGI;
            image[h][w].rgbtBlue = PBI;
            Pixels = PixelRed = PixelGreen = PixelBlue = 0;
        }
    }
    return;
}
