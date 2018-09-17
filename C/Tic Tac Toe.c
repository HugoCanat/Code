/* ==== tic tac toe ==== */

#include <string.h>
#include <stdlib.h>
#include <stdio.h>

#define N 3 //nombre de cases colonnes du tableau

int null(int tic[N][N])
{
    int i = 0, a;
    for(i = 0; i < N; i++)
    {
        for(a = 0; a < N; a++)
        {
            if(tic[i][a] == '-')
            {
                return 1;
            }
        }
    }
    return 0;
}

int win(int tic[N][N])
{
    int i = 1, Q = 'X';
    for(Q = 'X'; i != 3; Q = 'O')
    {
        /* -----------colonnes---------- */
        if(tic[0][0] == Q && tic[1][0] == Q && tic[2][0] == Q){return 0;}
        if(tic[0][1] == Q && tic[1][1] == Q && tic[2][1] == Q){return 0;}
        if(tic[0][2] == Q && tic[1][2] == Q && tic[2][2] == Q){return 0;}
        /* -----------lignes--------- */
        if(tic[0][0] == Q && tic[0][1] == Q && tic[0][2] == Q){return 0;}
        if(tic[1][0] == Q && tic[1][1] == Q && tic[1][2] == Q){return 0;}
        if(tic[2][0] == Q && tic[2][1] == Q && tic[2][2] == Q){return 0;}
        /*-----------diagonales----------*/
        if(tic[0][0] == Q && tic[1][1] == Q && tic[2][2] == Q){return 0;}
        if(tic[0][2] == Q && tic[1][1] == Q && tic[2][0] == Q){return 0;}

        i++;
    }
    return 1;
}

void intit_tic(int* tic[N][N])
{
    int i, y;
    for(i = 0; i != N; i++)
    {
        for(y=0; y!=N; y++)
        {
            tic[i][y] = '-';
        }
    }
}

void saisi(int* tic[N][N], int* joueur)
{
       int num = 0, a, b;

       printf("\njoueur %d:", *joueur+1);
       scanf("%d", &num);

       correspondance(&a, &b, num);


       if(a == 10 || tic[a][b] != '-')
       {
           printf("erreur case choisi incorrecte.\n");
       }
       else if(*joueur == 1) //si c'est au tour du joueur 2
       {
           tic[a][b] = 'O';
           *joueur -= 1;
       }
       else if(*joueur == 0)//si c'est au tour du joueur 1
       {
           tic[a][b] = 'X';
           *joueur += 1;
       }
}

int correspondance(int *a, int *b, int num)
{
    switch (num)
    {
    case 1:
        *a = 2;
        *b = 0;
        break;
    case 2:
        *a = 2;
        *b = 1;
        break;
    case 3:
        *a = 2;
        *b = 2;
        break;
    case 4:
        *a = 1;
        *b = 0;
        break;
    case 5:
        *a = 1;
        *b = 1;
        break;
    case 6:
        *a = 1;
        *b = 2;
        break;
    case 7:
        *a = 0;
        *b = 0;
        break;
    case 8:
        *a = 0;
        *b = 1;
        break;
    case 9:
        *a = 0;
        *b = 2;
        break;
    default:
        *a = 10;
        break;
    }
}

void affi(int tic[N][N])
{
    printf("    %c %c %c\n", tic[0][0], tic[0][1], tic[0][2]);
    printf("    %c %c %c\n", tic[1][0], tic[1][1], tic[1][2]);
    printf("    %c %c %c\n", tic[2][0], tic[2][1], tic[2][2]);
}

int main()
{
    int choix = 0;
    printf("Bonjour et bienvenue dans le Tic Tac Toe !\n");
    printf("\nVoulez-vous jouer contre l'ordinateur ? \n(1)Oui.\n(2)Non.");
    do
    {
        scanf("%d", &choix);
    }while(choix != 1 && choix != 2);
    if(choix == 1)
    {

    }


    int tic[N][N] = {{}};
    int joueur = 0;
    intit_tic(tic);
    affi(tic);
    do
    {
        saisi(tic, &joueur);
        affi(tic);
    }while(win(tic) && null(tic));

    if(joueur == 0 && null(tic) != 0){printf("joueur 1 gagner !\n");}
    if(joueur == 1 && null(tic) != 0){printf("joueur 2 gagner !\n");}
    if(null(tic) == 0){printf("Match null!\n");}

    int choix_fin = 0;
    printf("\nVoulez-vous recommencer ?(taper 1):");
    scanf("%d", &choix_fin);
    if(choix_fin == 1)
    {
        system("cls");
        main();
    }
    printf("Faites Ctrl+C pour quitter.");
    system("PAUSE");

    return 0;
}
