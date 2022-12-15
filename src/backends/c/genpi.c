#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <stdio.h>

float generateπ_from_random(int n){
    srand((unsigned int)time(NULL));
    int ins = 0;
    int outs = 0;
    for(int i = 0; i < n; i++){
        // srand((unsigned) time(0));
        float max = 1.0;
        float x = ((float)rand()/(float)(RAND_MAX)) * max;
        float y = ((float)rand()/(float)(RAND_MAX)) * max;
        float distance = x*x + y*y;
        if (distance <= 1){
            ins += 1;
        } else {
            outs += 1;
        }
    }

    return ins;
}