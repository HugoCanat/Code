#include <stdio.h>
#include <stdlib.h>
#include <SDL/SDL.h>

int virg(double Nb, int i);
int premi(double a);

int main(void)
{
    int time_1 = 0, time_2 = 0;
    int Nb_stbl = 0;
    int Nb_int = 0;
    int Nb_Nb = 0;
    double Nb_doub = 0;
    FILE* fichier = NULL;

    printf("TEST DE PRIMILITE\n");
    printf("\nentrez un nombre :");
    scanf("%d", &Nb_int);

    fichier = fopen("premi.txt","w");
    if(fichier == NULL)
    {
        printf("\nimpossible d'ouvrir le fichier premi.txt");
    }
    else if(fichier != NULL)
    {
        time_1 = SDL_GetTicks();
        for(Nb_doub = 1; Nb_doub < Nb_int; Nb_doub++)
        {
            if(premi(Nb_doub) == 1)  //nombre premier
            {
                Nb_Nb++;
                Nb_stbl = Nb_doub;
                printf("%d\n", Nb_stbl);
                fprintf(fichier, "%d\n", Nb_stbl);
            }
        }
    }
    fclose(fichier);
    time_2 = SDL_GetTicks() - time_1;
    printf("\n%d nombres trouves en %d ms", Nb_Nb, time_2);

    return 0;
}

int virg(double Nb, int i)
{
    int stble = 0;
    double stbl = 0;

    stble = Nb / i;
    stbl = Nb / i;
    if(stbl == stble) //pas de virgule
    {
        return 0;
    }
    else              //virugle
    {
        return 1;
    }

}

int premi(double a)
{
    int i = 1;
    int y = 1;

    if(virg(a, 2) == 1)
    {
        y = 2;
    }

    for(i = 1;i < a ; i += y)
    {
        if(virg(a, i) == 0 && i != 1)
        {
            return 0;
        }
    }
    return 1;
}

