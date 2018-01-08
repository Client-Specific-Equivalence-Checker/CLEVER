/*
 * Yi's example in klee
 */
 
int lib(int x){
	if (x > 11)
		return 11;
	else
		return x-1;
}

int client(int x){
	if (x > lib(x))
		return x;
	else
		return lib(x);
}

int main() {
    int x;//=2147483648;
    return client(x);
}
