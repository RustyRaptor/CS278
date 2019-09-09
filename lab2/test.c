#include <stdio.h>
// #include <stdchar.h>

/*
* Tell the compiler that we intend
* to use a function called show_message.
* It has no arguments and returns no value
* This is the "declaration".
*
*/

void show_message(void);
char not(char var);
char or(char l, char r);
char and(char l, char r);
char implies(char l, char r);
char prop1(char p, char q, char r);
char prop2(char p, char q, char r);
char prop3(char p, char q, char r);
char prop4(char p, char q, char r);
/*
* Another function, but this includes the body of
* the function. This is a "definition".
*/

int main(){
	not('F');
	or('F', 'T');
	and('T', 'T');
	implies('T', 'F');
	char truth[8][3+4];	
	// generate p
	for(int i = 0; i < 8; i++){
		if(i < 4){
		truth[i][0] = 'F';
		}else{
		truth[i][0] = 'T';
		}
	}
	for(int i = 0; i < 8; i++){
		printf(truth[i][0] ? "'T'\n" : "'F'\n");	

        }
	printf("new\n");
	char tick = 'F';
	for(int i = 0; i < 8; i++) {
		truth[i][1] = tick;
		if (i % 2 != 0&&i != 0){
			tick = not(tick);
		}

	}
	tick = 'F';
	for(int i = 0; i < 8; i++) {
		truth[i][2] = not(tick);

        }

	for(int i = 0; i < 8; i++){
                printf(truth[i][1] ? "'T'\n" : "'F'\n");

        }
	for(int i = 0; i < 8; i++){
		truth[i][3] = prop1(truth[i][0], truth[i][1], truth[i][2]);
		printf(prop1(truth[i][0], truth[i][1], truth[i][2]) ? "a'T'\n" : "a'F'\n");
	}
	for(int i = 0; i < 8; i++){
                truth[i][4] = prop2(truth[i][0], truth[i][1], truth[i][2]);
                printf(prop1(truth[i][0], truth[i][1], truth[i][2]) ? "a'T'\n" : "a'F'\n");
        }
	for(int i = 0; i < 8; i++){
                truth[i][5] = prop2(truth[i][0], truth[i][1], truth[i][2]);
                printf(prop1(truth[i][0], truth[i][1], truth[i][2]) ? "a'T'\n" : "a'F'\n");
        }
	for(int i = 0; i < 8; i++){
                truth[i][6] = prop3(truth[i][0], truth[i][1], truth[i][2]);
                printf(prop1(truth[i][0], truth[i][1], truth[i][2]) ? "a'T'\n" : "a'F'\n");
        }
	for(int i = 0; i < 8; i++){
                truth[i][7] = prop4(truth[i][0], truth[i][1], truth[i][2]);
                printf(prop1(truth[i][0], truth[i][1], truth[i][2]) ? "a'T'\n" : "a'F'\n");
        }




	for(int i = 0; i<8; i++){
		printf("\n");
     		for(int j = 0; j<(3+4); j++){
			 printf("%c\t", truth[i][j]);
		}
	}
     	return(0);
}

/*
* The body of the simple function.
* This is now a "definition".
*/

char not(char var){
	if(var == 'T'){
                return ('F');
        }else{
                return ('T');
        }
}
char or(char l, char r){
	if (l == 'T'|| r == 'T'){
                return ('T');
        }else{
                return ('F');
        }
}
char and(char l, char r){
	if (l == 'T' && r == 'T'){
                return ('T');
        }else{
                return ('F');
        }
}
char implies(char l, char r){
	if ((l == 'T' && r == 'T') || (l == 'F' && r == 'T')){
		return ('T');
	}else{
		return('F');
	}
}
char prop1(char p, char q, char r){
	return and(implies(not(p), q), implies(r, p));
}
char prop2(char p, char q, char r){
	return and(or(p, not(q)), or(r, not(implies(p,q))));
}
char prop3(char p, char q, char r) {
	return implies(implies(p,not(and(p, not(q)))), and(p, q));
}
char prop4(char p, char q, char r) {
	return and(and(p, implies(p,q)), not(q));
}
