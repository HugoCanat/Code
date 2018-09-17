#include <stdio.h>
#include <stdlib.h>

void poss(nbr, var);

int main()
{
	int nbrEn = 0;
    int var[100] = {0};
	int i = 0;
    
	printf("POSSIBILITY COUNTER\n\n");
	printf("Nombres d'entrees :");
	scanf("%d", &nbrEn);
    
    for(i = 1; i <= nbrEn; i++)
    {
        printf("valeur de l'entree numero %d \n", i);
        scanf("%d", &var[i]);
    }
    
    poss(nbrEn, var); 
}  

void poss(nbr, var)
{
    int resultat = 1;
    int a = 1;
    
    for(a = 1; a <= nbr; a++)
    {
        resultat = resultat * var[a];

    }
    printf("nombre de possibilite : %d", resultat);  
}
