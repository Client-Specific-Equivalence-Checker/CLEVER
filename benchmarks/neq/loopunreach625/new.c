int foo(int a, int b) {
	int c=0;
	if (a<0) {
		for (int i=1;i<=a;++i)
			c += b;
	}
	return c;

int main(int x, char*argv[]) {                
	if (x>=585 && x<665)                
		return foo(x,625);                
	return 0;
