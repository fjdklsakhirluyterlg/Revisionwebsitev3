#include <math.h>
#include <stdlib.h>
#include <time.h>
float generateπ_from_random(int n){
    int ins = 0;
    int outs = 0;
    for(int i = 0; i < n; i++){
        // srand((unsigned) time(0));
        int x = rand() % 10;
        int y = rand() % 10;
        float distance = pow(x, 2) + pow(y, 2);
        if (distance <= 1){
            ins += 1;
        } else {
            outs += 1;
        }
    }

    return 4*(ins/outs);
}