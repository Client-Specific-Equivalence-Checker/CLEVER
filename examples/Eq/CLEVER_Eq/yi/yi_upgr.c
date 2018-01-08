/*
 * Yi's example in klee
 */

int lib(int x){
	if (x > 10)
		return 12;
	else
		return x+1;
}

int client(int x){
	if (x > lib(x))
		return x;
	else
		return lib(x);
}

int main() {
    int x;//=2659237091;
    return client(x);
}
