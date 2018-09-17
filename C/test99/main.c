#include <stdlib.h>
#include <stdio.h>
#include <math.h>
void affich(int phase, int nombre, int pourcent)
{
  system("cls");
     if(phase == 1) //fonction choix_1
    {
        printf("Calcul des %d premiers nombres premiers.\n", nombre);
    }
    else if(phase == 2)//fonciton choix_2
    {
        printf("Calcul des nombres premiers jusqu'a %d.\n", nombre);
    }
    printf("Calcul..%d%%", pourcent);
}


int cent(int nombre_b, int nb)
{
    int calc = 0;
    calc = (100*nb)/nombre_b;
    if(calc > 100)
    {
        calc = 100;
    }
    return calc;
}

void choix_1(void)
{
    int pourcent_a = 0, pourcent_b = 0;
    int a = 0;
    int nombre = 1, i;
    FILE* NombresPremiers = NULL;
    NombresPremiers = fopen("NombresPremiers.txt", "w");
    if(NombresPremiers == NULL)
    {
        printf("Imposible d'ouvrir le fichier.\n");
    }
    else
    {
        printf("Entrez le nombre de nombres premiers que vous voulez calculer:");
        scanf("%d", &nombre);

        fprintf(NombresPremiers, "Voici les %d premiers nombres premiers\n", nombre);

        printf("Calcul..\n");
        system("cls");
        pourcent_a = cent(nombre, a);
        printf("%d %%", pourcent_a);

        for(i = 1; a < nombre; i++)
        {
            if(premier(i))
            {
                fprintf(NombresPremiers, "%d\n", i);
                a++;
            }
            pourcent_b = cent(nombre, a);
            if(pourcent_b > pourcent_a)
            {
                affich(1, nombre, pourcent_b);
                pourcent_a = pourcent_b;
            }
        }
    }
    fclose(NombresPremiers);
}

void choix_2(void)
{
    int pourcent_a = 0, pourcent_b = 0;
    int nombre = 1, i;
    FILE* NombresPremiers = NULL;
    NombresPremiers = fopen("NombresPremiers.txt", "w");
    if(NombresPremiers == NULL)
    {
        printf("Imposible d'ouvrir le fichier.\n");
    }
    else
    {
        printf("Entrez le nombre jusqu'auquel vous voulez calculer les nombres premiers:");
        scanf("%d", &nombre);

        fprintf(NombresPremiers, "Voici les nombres premiers jusqu'a %d\n", nombre);

        printf("Calcul..");

        for(i = 1; i <= nombre; i++)
        {
            if(premier(i))
            {
                fprintf(NombresPremiers, "%d\n", i);
            }
            pourcent_b = cent(nombre, i);
            if(pourcent_b > pourcent_a)
            {
                system("cls");
                affich(2, nombre, pourcent_b);
                pourcent_a = pourcent_b;
            }
        }
        fclose(NombresPremiers);
    }
}

int premier(int nb)
{
    int y = 1;
    int i = 0, b = sqrt(nb) + 1; //+1 au cas le resultat est decimal
    if(nb % 2)
    {
        y=2;
    }
    for(i = 1; i < b; i+=y)
    {
        if(!(nb % i) && i != 1)
        {
            return 0;
        }
    }
    return 1;
}

int main(void)
{
    int nombre = 1, i, choix = 0;
    printf("--TEST DE PRIMILITE--\n");

    printf("Bonjour, voulez-vous calculer un certain nombre de nombres premiers?(1)\n");
    printf("Ou voulez-vous calculer les nombres premiers jusqu'a un certain nombre?(2)\n");
    printf("\nEntrez votre choix: ");
    do
    {
        scanf("%d", &choix);
        if(choix != 1 && choix != 2)
        {
            printf("choix incorrect(1 ou 2).");
        }
    }while (choix != 1 && choix != 2);
    if(choix == 1) {choix_1();}
    else {choix_2();}

    printf("\a");
    system("NombresPremiers.txt");

}
