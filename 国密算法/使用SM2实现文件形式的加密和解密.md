## 加密并且导出文件
```C++
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <gmssl/sm2.h>

int main(void)
{
	SM2_KEY sm2_key;
	char *password = "12345678910";  //这里是加密的密码
	FILE* fp = fopen("D:\private_key2.pem", "wb");
	// 密钥生成
	if (sm2_key_generate(&sm2_key) != 1) {
		fprintf(stderr, "error\n");
		return 1;
	}

	// 拿到私钥，并且打印。（打开私钥是需要密码的）
	if (sm2_private_key_info_encrypt_to_pem(&sm2_key, password, fp) != 1) {
		fprintf(stderr, "error\n");
		return 1;
	}
	fclose(fp);
	return 0;
}
```
## 解密指定的文件
```C++
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <gmssl/mem.h>
#include <gmssl/sm2.h>

//钥匙解析

int main(int argc, char **argv)
{
	char *prog = argv[0];		//程序名（第一个参数就是程序名本身）
	char *keyfile;				//钥匙文件
	char *pass;					//密码
	FILE *keyfp = NULL;			//钥匙文件的指针
	SM2_KEY sm2_key;			//SM2密钥

	if (argc < 3) {
		fprintf(stderr, "usage: %s <key.pem> <pass>\n", prog);
		return -1;
	}
	keyfile = argv[1];			//钥匙文件
	pass = argv[2];				//密码
	// 钥匙文件的指针不为空
	if (!(keyfp = fopen(keyfile, "rb"))) {
		fprintf(stderr, "%s: open file '%s' failure\n", prog, keyfile);
		return -1;
	}
	// 如果打开的是通过密钥，那么可能是失败的。
	if (sm2_private_key_info_decrypt_from_pem(&sm2_key, pass, keyfp) != 1) {
		fprintf(stderr, "%s: load key failure\n", prog);
		fclose(keyfp);
		return -1;
	}

	// 输出sm2的键值
	sm2_key_print(stdout, 0, 0, "SM2_KEY", &sm2_key);

	gmssl_secure_clear(&sm2_key, sizeof(sm2_key));
	fclose(keyfp);
	return 0;
}

```