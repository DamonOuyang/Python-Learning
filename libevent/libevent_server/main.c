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
#define LISTEN_NUM 128
#define MAX_BYTES 1024

void read_cb(evutil_socket_t clientfd, short what, void * arg)
{

    (void)what;
    puts("read_cb");
    char buf[MAX_BYTES] = {0};

    struct event * ev = (struct event * )arg;

    int ret = read(clientfd,buf,sizeof(buf));
    if(ret < 0)
        perror("read");

    int i = 0 ;
    for(;i<ret; i++)
    {
        buf[i] = toupper(buf[i]);
    }

    ret = write(clientfd,buf,ret);
    if(ret < 0)
        perror("write");
}

void accept_cb(evutil_socket_t listenfd, short what, void * arg)
{
    struct sockaddr_in client_addr;
    bzero(&client_addr,sizeof(client_addr));
    socklen_t client_addr_len = sizeof(client_addr);

    int clientfd;
    clientfd = accept(listenfd,(struct sockaddr*)&client_addr,&client_addr_len);
    if(clientfd < 0)
        perror("accept");

    struct event_base * base = arg;
    struct event * ev;
    ev = event_new(base,clientfd,EV_READ | EV_PERSIST,NULL,NULL);
    event_assign(ev,base,clientfd,EV_READ | EV_PERSIST,read_cb,(void*)ev);

    event_add(ev,NULL);

}

void main_loop(evutil_socket_t fd)
{
    puts("main_loop");
    struct event_base* base = event_base_new();
    struct event * ev;
    ev = event_new(base,fd,EV_READ | EV_PERSIST,accept_cb,(void*)base);
    event_add(ev,NULL);

//    event_base_loop(base,NULL);
    event_base_dispatch(base);

    event_free(ev);
    event_base_free(base);
}
int main(void)
{
    int listenfd;
    listenfd = socket(AF_INET,SOCK_STREAM,0);
    if(listenfd < 0)
        perror("solistencket");

    struct sockaddr_in listen_addr;
    bzero(&listen_addr,sizeof(listen_addr));
    listen_addr.sin_family = AF_INET;
    listen_addr.sin_port = htons(PORT);
    listen_addr.sin_addr.s_addr = htonl(INADDR_ANY);

    int ret = bind(listenfd,(struct sockaddr*)&listen_addr,sizeof(listen_addr));
    if(ret < 0)
        perror("bind");

    ret = listen(listenfd,LISTEN_NUM);
    if(ret < 0)
        perror("listen");

//    struct sockaddr_in client_addr;
//    bzero(&client_addr,sizeof(client_addr));
//    socklen_t client_addr_len = sizeof(client_addr);

//    int clientfd;
//    clientfd = accept(listenfd,(struct sockaddr*)&client_addr,&client_addr_len);
//    if(clientfd < 0)
//        perror("accept");

    main_loop(listenfd); // accept
    close(listenfd);

    return 0;
}

