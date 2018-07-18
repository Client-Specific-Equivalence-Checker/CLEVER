int foo(int a, int b) {
	int c = 0;
	for (int i=0; i<a; ++i)
		c += b;
	return c;}

int main(int x, char*argv[]) {
	if (x>=23 && x<27)
		return foo(x,25);
	return 0;
}