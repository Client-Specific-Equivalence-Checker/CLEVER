int lib(int x) {
	return x % 5;
}

int client(int x){
	if (x < -100 || x > 100) {
		return x;
	}
	x = x*5*6;
	if (lib(x)==0){
		return 1;
	}else{
		return 0;
	}
}

int main() {
	int x = -10;
	return client(x);
}
