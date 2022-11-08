#include <stdio.h> 
int reverse(int A){
    int B ; int C = 0 ;
    while (A != 0){
        B = A % 10 ;
        C  = C * 10 + B ;
        A = A / 10 ;}
    return C ;}
int main() { 
int A, B;
scanf("%d %d",&A,&B); 
A=reverse(A); 
B=reverse(B);
int C = A+B; 
printf("%d",reverse(C));
}