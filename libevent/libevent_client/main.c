#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <ctype.h>
#include <arpa/inet.h>
#include <signal.h>
#include <errno.h>
#include <sys/wait.h>
#include <event2/event.h>

#define PORT 8888
#define ADDR_IP "192.168.32.34"
#define MAX_BYTES 1024

void read_cb(evutil_socket_t ev_socket, short what, void *arg)
{
    puts("read clientfd");
    char buf[MAX_BYTES];
    int ret;
    ret = read(ev_socket,buf,sizeof(buf));
    if(ret <= 0)
    {
        close(ev_socket);
        event_base_loopexit((struct event_base*)arg,NULL);
    }
    write(STDERR_FILENO,buf,ret);
}

void write_cb(evutil_socket_t stdinfd, short what, void *arg)
{
    evutil_socket_t socketfd = arg;

    char buf[MAX_BYTES] = {0};
    int ret = read(STDIN_FILENO,buf,sizeof(buf));
    if(ret < 0)
        perror("read");

    ret = read(stdinfd,buf,sizeof(buf));
    if(ret < 0)
        perror("write");
    write(socketfd,buf,ret);

}

void main_loop(evutil_socket_t socketfd)
{
    puts("main_loop");
    struct event_base* base;
    base = event_base_new();

    struct event * ev_socket;
    ev_socket = event_new(base,socketfd,EV_WRITE | EV_PERSIST,read_cb,(void*)base);

    struct event * ev_stdin;
    ev_stdin = event_new(base,STDIN_FILENO,EV_WRITE | EV_PERSIST,write_cb,(void*)ev_socket);

    event_add(ev_socket,NULL);
    event_add(ev_stdin,NULL);
    event_base_dispatch(base);

    event_free(ev_socket);
    event_free(ev_stdin);
    event_base_free(base);
}

int main(void)
{
    int socketfd;
    socketfd = socket(AF_INET,SOCK_STREAM,0);

    struct sockaddr_in addr;
    bzero(&addr,sizeof(addr));
    addr.sin_port = htons(PORT);
    addr.sin_family = AF_INET;
    inet_pton(AF_INET,&addr.sin_addr.s_addr,ADDR_IP);

    int ret = connect(socketfd,(struct sockaddr*)&addr,sizeof(addr));
    if(ret < 0)
        perror("bind");

    main_loop(socketfd);

    return 0;
}

