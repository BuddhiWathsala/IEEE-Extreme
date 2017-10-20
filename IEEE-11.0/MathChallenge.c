#include <stdio.h>
#include <math.h>

int main() {
    int a,b,c,t,i;
    int ncr;
    scanf("%d",&t);


    for(i=0;i<t;i++){
        scanf("%d %d %d",&a,&b,&c);

        if(a==0){
            printf("%d",0);
            continue;
        }else if(a == 1){
            printf("%d",1);
            continue;
        }
        else if((b != c) && ((b-c) < c)){
            ncr = NCR(b,(b-c));

        }else{
            ncr = NCR(b,c);

        }

        double num = pow(10,9) + 7;
        double n = (double)(pow(a,ncr));
        long answer = (long) (fmod(n,num));

        printf("%d %ld %ld\n",ncr,n,answer);

    }
    return 0;
}

int NCR(int n,int c){
    int i,r;
    int up=n,down=c;
    for(i=1;i<c;i++){
        down = down*(c-i);
        up=up*(n-i);

    }
    r = (int)(up/down);

    return r;
}

