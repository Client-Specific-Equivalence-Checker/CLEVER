int foo(int a, int b) {
	int c=0;
	if (a<0) {
		for (int i=1;i<=a;++i)
			c += b;
	}
	return c;
	}

int main(int x, char*argv[]) {                
	if (x>=85 && x<115)                
		return foo(x,100);                
	return 0;
	}
