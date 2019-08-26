#include <stdio.h>
// #include <stdbool.h>
int main() {
	char str1 = *"F";
	char str2 = *"F";
	char str3 = *"F";
	char str4 = *"F";
	char str5 = *"F";
	char str6 = *"F";
	char str7 = *"F";
	char str8 = *"F";
	int counter = 1;

	for (int a = 0; a < 2; a++){
		if (a == 0){
			str1 = *"F";
		}else if (a == 1){
			str1 = *"T";
		}
		{
			
		}
		for (int b = 0; b < 2; b++){
			if (b == 0){
				str2 = *"F";
			}else if (b == 1){
				str2 = *"T";
			}
			for (int c = 0; c < 2; c++){
				if (c == 0){
					str3 = *"F";
				}else if (c == 1){
					str3 = *"T";
				}
				for (int d = 0; d < 2; d++){
					if (d == 0){
						str4 = *"F";
					}else if (d == 1){
						str4 = *"T";
					}
					for (int e = 0; e < 2; e++){
						if (e == 0){
							str5 = *"F";
						}else if (e == 1){
							str5 = *"T";
						}
						for (int f = 0; f < 2; f++){
							if (f == 0){
								str6 = *"F";
							}else if (f == 1){
								str6 = *"T";
							}
							for (int g = 0; g < 2; g++){
								if (g == 0){
									str7 = *"F";
								}else if (g == 1){
									str7 = *"T";
								}
								for (int h = 0; h < 2; h++){
									if (h == 0){
										str8 = *"F";
									}else if (h == 1){
										str8 = *"T";
									}
									printf("%d\n", counter);
									counter++;
									printf("\
										F, F, F, %c,\n\
										F, F, T, %c,\n\
										F, T, F, %c,\n\
										F, T, T, %c,\n\
										T, F, F, %c,\n\
										T, F, T, %c,\n\
										T, T, F, %c,\n\
										T, T, T, %c\n", str1,str2,str3,str4,str5,str6,str7,str8);
									
									

		
	}
	}
	}
	}
	}
	}
	}
	}
	return 0;
}