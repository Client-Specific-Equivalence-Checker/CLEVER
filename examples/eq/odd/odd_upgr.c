int lib(int x) {
	return (x+1) % 2;
}

int client(int x){
	if (lib(x)==0){
	   	return 1;
	}else{
		return 0;
	}
}

int main() {
	int x;
	return client(x);
}
