#include <stdio.h>
#include <conio.h>
int fr[10], n, m;
int page[20];
int i, j, k, l, flag1 = 0, flag2 = 0, pf = 0;
int max, found = 0,index = 0;
int lg[10];

void display();
void read(); // Added read prototype for completeness

void main()
{
    read();

    // Initialization (missing in your pic, but necessary)
    for (i = 0; i < m; i++) {
        fr[i] = -1;
    }

    // This section is split between page 36 and 37
    for (j = 0; j < n; j++)
    {
        flag1 = 0;
        flag2 = 0;
        for (i = 0; i < m; i++)
        {
            if (fr[i] == page[j])
            {
                flag1 = 1;
                flag2 = 1;
                break;
            }
        }

        if (flag1 == 0)
        {
            for (i = 0; i < m; i++)
            {
                if (fr[i] == -1)
                {
                    fr[i] = page[j];
                    flag2 = 1;
                    pf++;
                    break;
                }
            }

            if (flag2 == 0)
            {
                for (i = 0; i < m; i++)
                {
                    lg[i] = 0;
                    for (k = j + 1; k < n; k++)
                    {
                        if (fr[i] == page[k])
                        {
                            lg[i] = k - j;
                            break;
                        }
                    }
                }
                
                // Found logic from page 37
                found = 0;
                for (i = 0; i < m; i++)
                {
                    if (lg[i] == 0)
                    {
                        index = i;
                        found = 1;
                        break; // break is in the pic
                    }
                }
                
                // break; is on page 37 after the loop, but it breaks the 'for (j=0...)' loop. 
                // It likely belonged after 'if (lg[i] == 0)' as shown above.
                // Assuming it's the correct break, we'll continue the logic:

                if (found == 0)
                {
                    max = lg[0];
                    index = 0;
                    for (i = 1; i < m; i++)
                    {
                        if (max < lg[i])
                        {
                            max = lg[i];
                            index = i;
                        }
                    }
                }

                if (index >= 0 && index < m) { // Safegaurd added
                    fr[index] = page[j];
                    pf++;
                }
            }
        }
        display();
    }

    float pr = (float)pf / n * 100;
    printf("\nNumber of page faults : %d\n", pf);
    printf("Page fault rate = %.2f\n", pr);
    getch(); // Non-standard function
}

// Read function (from page 36)
void read() {
    printf("Enter length of the reference string: ");
    scanf("%d", &n);
    
    printf("Enter the reference string: \n");
    for (i = 0; i < n; i++) {
        printf("Page %d: ", i + 1);
        scanf("%d", &page[i]);
    }
    
    printf("Enter number of frames: ");
    scanf("%d", &m);
}


// Display function (from page 38)
void display()
{
    printf("\n"); // Missing in pic, but for better output
    int i;
    for (i = 0; i < m; i++)
    {
        printf("%d\t", fr[i]);
    }
    printf("\n"); // Missing in pic, but for better output
}