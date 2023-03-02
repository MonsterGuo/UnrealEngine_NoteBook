```C++
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <gmssl/mem.h>
#include <gmssl/sm2.h>


int main(void)
{
	SM2_KEY sm2_key;
	char *password = "123456";
	unsigned char buf[512];  //密钥的缓冲区
	unsigned char *p;
	size_t len;

	printf("Read SM2 private key file (PEM) from stdin ...\n");
	if (sm2_private_key_info_decrypt_from_pem(&sm2_key, password, stdin) != 1) {
		fprintf(stderr, "error\n");
		return 1;
	}

	p = buf;
	len = 0;
	//sm2_private_key_to_der函数，它用于将SM2私钥转换为DER编码。
	//此函数需要提供原始的私钥缓冲区，该缓冲区的大小必须在32到114字节之间，然后将返回DER编码的私钥。
	if (sm2_private_key_to_der(&sm2_key, &p, &len) != 1) {
		fprintf(stderr, "error\n");
		return 1;
	}
	fwrite(buf, 1, len, stdout);

	gmssl_secure_clear(&sm2_key, sizeof(sm2_key));
	return 0;
}
```

>sm2_private_key_to_der函数，它用于将SM2私钥转换为DER编码。此函数需要提供原始的私钥缓冲区，该缓冲区的大小必须在32到114字节之间，然后将返回DER编码的私钥。
