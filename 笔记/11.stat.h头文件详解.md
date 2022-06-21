#include <sys/stat.h>

文件状态，

是unix/linux系统定义文件状态所在的伪标准头文件。

含有类型与函数：

             dev_t     st_dev     Device ID of device containing file.  
              ino_t     st_ino     File serial number.  
              mode_t    st_mode    Mode of file (see below).  
              nlink_t   st_nlink   Number of hard links to the file.  
              uid_t     st_uid     User ID of file.  
              gid_t     st_gid     Group ID of file.  
              dev_t     st_rdev    Device ID (if file is character or block special).  
              off_t     st_size    For regular files, the file size in bytes.  
                                   For symbolic links, the length in bytes of the  
                                   pathname contained in the symbolic link.  
  
                                   For a shared memory object, the length in bytes.  
  
                                   For a typed memory object, the length in bytes.  
  
                                   For other file types, the use of this field is  
                                   unspecified.  
              time_t    st_atime   Time of last access.  
              time_t    st_mtime   Time of last data modification.  
              time_t    st_ctime   Time of last status change.

              int    chmod(const char *, mode_t);

              int    fchmod(int, mode_t);  
              int    fstat(int, struct stat *);  
              int    lstat(const char *restrict, struct stat *restrict);  
              int    mkdir(const char *, mode_t);  
              int    mkfifo(const char *, mode_t);  
              int    mknod(const char *, mode_t, dev_t);  
              int    stat(const char *restrict, struct stat *restrict);  
              mode_t umask(mode_t);

使用stat函数最多的可能是ls-l命令，用其可以获得有关一个文件的所有信息。

一般头文件在/usr/include下面，这里是标准C程序头文件，如果你的头文件前加了 <sys/*>,那说明这是系统调用函数头文件，其在/usr/include/sys下面。

函数都是获取文件（普通文件，目录，管道，socket，字符，块（）的属性。函数原型#include <sys/stat.h>  
  
int stat(const char *restrict pathname, struct stat *restrict buf);提供文件名字，获取文件对应属性。  
int fstat(int filedes, struct stat *buf);通过文件描述符获取文件对应的属性。  
int lstat(const char *restrict pathname, struct stat *restrict buf);连接文件描述命，获取文件属性。  
文件对应的属性struct stat {  
        mode_t     st_mode;       //文件对应的模式，文件，目录等  
        ino_t      st_ino;       //inode节点号  
        dev_t      st_dev;        //设备号码  
        dev_t      st_rdev;       //特殊设备号码  
        nlink_t    st_nlink;      //文件的连接数  
        uid_t      st_uid;        //文件所有者  
        gid_t      st_gid;        //文件所有者对应的组  
        off_t      st_size;       //普通文件，对应的文件字节数  
        time_t     st_atime;      //文件最后被访问的时间  
        time_t     st_mtime;      //文件内容最后被修改的时间  
        time_t     st_ctime;      //文件状态改变时间  
        blksize_t st_blksize;    //文件内容对应的块大小  
        blkcnt_t   st_blocks;     //伟建内容对应的块数量  
      };

示例：

#include <sys/stat.h>  
#include <unistd.h>  
#include <stdio.h>  
  
int main() {  
    struct stat buf;  
    **stat("/etc/hosts", &buf)**;  
    printf("/etc/hosts file size = %d\n", **buf.st_size**);  
}