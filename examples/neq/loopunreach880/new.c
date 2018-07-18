int foo(int a, int b) {
	int c=0;
	if (a<0) {
		for (int i=1;i<=a;++i)
			c += b;
	}
	return c;
	}

int main(int x, char*argv[]) {                
	if (x>=833 && x<927)                
		return foo(x,880);                
	return 0;
}