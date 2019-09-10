#include <stdio.h>

// init functions
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
	char truth[8][8];
	char tick = 'F';	
	// generate all possible truth combinations
	for(int i = 0; i < 8; i++){
		truth[i][0] = tick;
		if((i+1) % 4 == 0 && i != 0){
			tick = not(tick);
		}
	}
	tick = 'F';
	for(int i = 0; i < 8; i++) {
		truth[i][1] = tick;
		if (i % 2 != 0&&i != 0){
			tick = not(tick);
		}

	}
	tick = 'F';
	for(int i = 0; i < 8; i++) {
		truth[i][2] = tick;
		tick = not(tick);

        }

	// apply all 4 propositions
	for(int i = 0; i < 8; i++){
		truth[i][3] = prop1(truth[i][0], truth[i][1], truth[i][2]);
	}
	for(int i = 0; i < 8; i++){
                truth[i][4] = prop2(truth[i][0], truth[i][1], truth[i][2]);
        }
	for(int i = 0; i < 8; i++){
                truth[i][5] = prop2(truth[i][0], truth[i][1], truth[i][2]);
        }
	for(int i = 0; i < 8; i++){
                truth[i][6] = prop3(truth[i][0], truth[i][1], truth[i][2]);
        }
	for(int i = 0; i < 8; i++){
                truth[i][7] = prop4(truth[i][0], truth[i][1], truth[i][2]);
        }



	// print out array
//	printf("%c\t");
	for(int i = 0; i<8; i++){
		printf("\n");
     		for(int j = 0; j<(7); j++){
			 printf("%c\t", truth[i][j]);
		}
	}
	printf("\n");
     	return(0);
}

// logic functions
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
	if ((l != 'T') || (l == 'T' && r == 'T')){
		return ('T');
	}else{
		return('F');
	}
}

// propositions 1 to 4
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
