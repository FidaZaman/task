#include<stdio.h>

int main(){
 printf("==================BMI Calculator==================\n");
 float w,ft,inch, BMI;
 printf("enter your weight : ");
 scanf("%f", &w);
 printf("enter your height in feet and inch ,\n");
 printf("feet : ");
 scanf("%f",&ft);
 printf("inch : ");
 scanf("%f",&inch);
 float height = (ft*12+inch)/39.37;
 BMI = w/(height*height);
 printf("Your BMI is %.2f", BMI);

  if(BMI<=0||BMI>100){
  printf("\n``you are an Alien``");
 }
  else if(BMI<18.5){
  printf("\n``Underweight``");
 }
 else if(BMI<24.9){
  printf("\n``Normal``");
 }
 else if(BMI<29.9){
  printf("\n``Overweight``");
 }
 else if(BMI<30){
  printf("\n``Obese``");
 }
printf("\n[Based on : World Health Organization. ©️2024.]");
 return 0;
}
