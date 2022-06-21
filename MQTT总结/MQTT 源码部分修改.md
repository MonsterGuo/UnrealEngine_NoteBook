1.client.h文件的修改
![[Pasted image 20220608202358.png]]
2.ssl_options.h文件修改
问题未知：这个命名会导致出错，但是单纯在C++中是正常的应该是重名了
![[Pasted image 20220608202926.png]]
修正方式：
![[Pasted image 20220608203143.png]]
3.will_options.h文件修改
这里需要类型强转
![[Pasted image 20220608204819.png]]
