int foo(int a, int b);

int main(int x, char*argv[]) {
	return foo(2,2);
}

int foo(int a, int b) {
	int c=1;
	if (a<0) {
		for (int i=1;i<=b;++i)
			c+=a;
	}
	
	return c;
}
