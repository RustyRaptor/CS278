#include <stdio.h>
#include <stdbool.h>

/*
* Tell the compiler that we intend
* to use a function called show_message.
* It has no arguments and returns no value
* This is the "declaration".
*
*/

void show_message(void);
bool not(bool var);
bool or(bool l, bool r);
bool and(bool l, bool r);
bool implies(bool l, bool r);
bool prop1(bool p, bool q, bool r);
bool prop2(bool p, bool q, bool r);
bool prop3(bool p, bool q, bool r);
bool prop4(bool p, bool q, bool r);
/*
* Another function, but this includes the body of
* the function. This is a "definition".
*/

int main(){
	not(false);
	or(false, true);
	and(true, true);
	implies(true, false);
	bool truth[8][3+4];	
	// generate p
	for(int i = 0; i < 8; i++){
		if(i < 4){
		truth[i][0] = false;
		}else{
		truth[i][0] = true;
		}
	}
	for(int i = 0; i < 8; i++){
		printf(truth[i][0] ? "true\n" : "false\n");	

        }
	printf("new\n");
	bool tick = false;
	for(int i = 0; i < 8; i++) {
		truth[i][1] = tick;
		if (i % 2 != 0&&i != 0){
			tick = !tick;
		}

	}
	tick = false;
	for(int i = 0; i < 8; i++) {
                truth[i][2] = tick;
                tick = !tick;

        }

	for(int i = 0; i < 8; i++){
                printf(truth[i][1] ? "true\n" : "false\n");

        }
	for(int i = 0; i < 8; i++){
		truth[i][3] = prop1(truth[i][0], truth[i][1], truth[i][2]);
		printf(prop1(truth[i][0], truth[i][1], truth[i][2]) ? "atrue\n" : "afalse\n");
	}
	for(int i = 0; i < 8; i++){
                truth[i][4] = prop2(truth[i][0], truth[i][1], truth[i][2]);
                printf(prop1(truth[i][0], truth[i][1], truth[i][2]) ? "atrue\n" : "afalse\n");
        }
	for(int i = 0; i < 8; i++){
                truth[i][5] = prop2(truth[i][0], truth[i][1], truth[i][2]);
                printf(prop1(truth[i][0], truth[i][1], truth[i][2]) ? "atrue\n" : "afalse\n");
        }
	for(int i = 0; i < 8; i++){
                truth[i][6] = prop3(truth[i][0], truth[i][1], truth[i][2]);
                printf(prop1(truth[i][0], truth[i][1], truth[i][2]) ? "atrue\n" : "afalse\n");
        }
	for(int i = 0; i < 8; i++){
                truth[i][7] = prop4(truth[i][0], truth[i][1], truth[i][2]);
                printf(prop1(truth[i][0], truth[i][1], truth[i][2]) ? "atrue\n" : "afalse\n");
        }




	for(int i = 0; i<8; i++){
		printf("\n");
     		for(int j = 0; j<(3+4); j++){
			 printf(truth[i][j] ? "T\t" : "F\t");
		}
	}
     	return(0);
}

/*
* The body of the simple function.
* This is now a "definition".
*/

bool not(bool var){
	if(var){
                return (false);
        }else{
                return (true);
        }
}
bool or(bool l, bool r){
	if(l||r){
                return (true);
        }else{
                return (false);
        }
}
bool and(bool l, bool r){
	if(l&&r){
                return (true);
        }else{
                return (false);
        }
}
bool implies(bool l, bool r){
	if( l<=r){
		return (true);
	}else{
		return(false);
	}
}
bool prop1(bool p, bool q, bool r){
	return and(implies(not(p), q), implies(r, p));
}
bool prop2(bool p, bool q, bool r){
	return and(or(p, not(q)), or(r, not(implies(p,q))));
}
bool prop3(bool p, bool q, bool r) {
	return implies(implies(p,not(and(p, not(q)))), and(p, q));
}
bool prop4(bool p, bool q, bool r) {
	return and(and(p, implies(p,q)), not(q));
}
