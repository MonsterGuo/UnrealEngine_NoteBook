# 加密
```C++
/*
 *  Copyright 2014-2022 The GmSSL Project. All Rights Reserved.
 *
 *  Licensed under the Apache License, Version 2.0 (the License); you may
 *  not use this file except in compliance with the License.
 *
 *  http://www.apache.org/licenses/LICENSE-2.0
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <gmssl/sm2.h>
#include <gmssl/error.h>


int main(void)
{
	//SM2：密钥 
	SM2_KEY sm2_key;
	//SM2公钥
	SM2_KEY pub_key;
	//明文 最大长度是255
	unsigned char plaintext[SM2_MAX_PLAINTEXT_SIZE];
	//密文 最大长度是255
	unsigned char ciphertext[SM2_MAX_CIPHERTEXT_SIZE];
	size_t len;

	// SM2钥匙的生成
	sm2_key_generate(&sm2_key);
	// 拷贝1024位到公钥中
	memcpy(&pub_key, &sm2_key, sizeof(SM2_POINT));
	//SM2_加密(公钥,输入的明文，长度，密文，长度)
	uint8_t* Monster = "hello world";
	size_t length = strlen(Monster);
	sm2_encrypt(&pub_key, Monster, length, ciphertext, &len);
	//格式化位信息（函数指针，格式，编号，字符串描述，密文，长度）
	format_bytes(stdout, 0, 0, "ciphertext", ciphertext, len);
	
	// sm2解密（sm2密钥，密文，长度，明文，长度）
	if (sm2_decrypt(&sm2_key, ciphertext, len, plaintext, &len) != 1) {
		// 报错
		fprintf(stderr, "error\n");
		return 1;
	}
	// 将尾元素置：零
	plaintext[len] = 0;
	printf("plaintext: %s\n", plaintext);
	
	return 0;
}

```

# 钥匙的生成
```C++
/*
 *  Copyright 2014-2022 The GmSSL Project. All Rights Reserved.
 *
 *  Licensed under the Apache License, Version 2.0 (the License); you may
 *  not use this file except in compliance with the License.
 *
 *  http://www.apache.org/licenses/LICENSE-2.0
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <gmssl/sm2.h>

int main(void)
{
	SM2_KEY sm2_key;

	if (sm2_key_generate(&sm2_key) != 1) {
		fprintf(stderr, "error\n");
		return 1;
	}
	//sm2钥匙打印（文件，从哪个位置开始，到哪个位置，标签，SM2钥匙）
	sm2_key_print(stdout, 0, 0, "SM2PrivateKey", &sm2_key);
	sm2_public_key_print(stdout, 0, 0, "SM2PublicKey", &sm2_key);

	return 0;
}

```
# 将密钥保存到文件
```C++
/*
 *  Copyright 2014-2022 The GmSSL Project. All Rights Reserved.
 *
 *  Licensed under the Apache License, Version 2.0 (the License); you may
 *  not use this file except in compliance with the License.
 *
 *  http://www.apache.org/licenses/LICENSE-2.0
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <gmssl/sm2.h>

int main(void)
{
	SM2_KEY sm2_key;

	FILE* p = fopen("E:\\a.txt", "wb");
	if (sm2_key_generate(&sm2_key) != 1) {
		fprintf(stderr, "error\n");
		return 1;
	}
	//sm2钥匙打印（文件，从哪个位置开始，到哪个位置，标签，SM2钥匙）
	sm2_key_print(p, 0, 0, "SM2PrivateKey", &sm2_key);
	sm2_public_key_print(p, 0, 0, "SM2PublicKey", &sm2_key);
	fclose(p);
	return 0;
}

```
# 钥匙解析
```C++
/*
 *  Copyright 2014-2022 The GmSSL Project. All Rights Reserved.
 *
 *  Licensed under the Apache License, Version 2.0 (the License); you may
 *  not use this file except in compliance with the License.
 *
 *  http://www.apache.org/licenses/LICENSE-2.0
 */


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

	sm2_key_print(stdout, 0, 0, "SM2_KEY", &sm2_key);

	gmssl_secure_clear(&sm2_key, sizeof(sm2_key));
	fclose(keyfp);
	return 0;
}




```

# 单独的读取私钥

```C++
/*
 *  Copyright 2014-2022 The GmSSL Project. All Rights Reserved.
 *
 *  Licensed under the Apache License, Version 2.0 (the License); you may
 *  not use this file except in compliance with the License.
 *
 *  http://www.apache.org/licenses/LICENSE-2.0
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <gmssl/sm2.h>

int main(void)
{
	SM2_KEY sm2_key;
	char *password = "123456";
	// 密钥生成
	if (sm2_key_generate(&sm2_key) != 1) {
		fprintf(stderr, "error\n");
		return 1;
	}

	// 拿到私钥，并且打印。（打开私钥是需要密码的）
	if (sm2_private_key_info_encrypt_to_pem(&sm2_key, password, stdout) != 1) {
		fprintf(stderr, "error\n");
		return 1;
	}

	return 0;
}

```

