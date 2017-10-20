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

void run_base_with_ticks(struct event_base * base )
{
    struct timeval ten_sec;
    ten_sec.tv_sec = 10;
    ten_sec.tv_usec = 0;

    while(1)
    {
        event_base_loopexit(base,&ten_sec);
        event_base_dispatch(base);
        puts("Tick");
    }
}

void cb_func(evutil_socket_t fd, short what, void * arg)
{
    (void)what;
    (void)fd;
    struct event_base * base = arg;
    run_base_with_ticks(base);

    //    struct timeval tv = {5,0};
    //    event_base_loopbreak(base);
    //    event_base_loopexit(base,&tv);
}


void main_loop(evutil_socket_t fd)
{
    struct event_base * base;
    struct event * ev;
    //    struct timeval tv = {5,0};
    ev = event_new(base,fd,EV_TIMEOUT|EV_PERSIST,cb_func,base);
    //    event_add(ev,&tv);
    event_add(ev,NULL);

    event_base_dispatch(base);//
}
int main(void)
{
    evutil_socket_t fd;
    main_loop(fd);
    return 0;
}

#if 0

void cb_func(evutil_socket_t fd, short what, void *arg)
{
    const char * data = arg;
    printf("Got an event on socket %d:%s%s [%s]\n",
           (int)fd,
           (what & EV_TIMEOUT)?"EV_TIMEOUT":" not EV_TIMEOUT",
           (what & EV_READ)?"EV_READ":" not EV_READ",
           data);

}

void main_loop(evutil_socket_t fd)
{
    struct event *ev;
    struct timeval five_sce = {5,0};
    struct event_base* base = event_base_new();

    ev = event_new(base,fd,EV_TIMEOUT
                   |EV_PERSIST,cb_func,(char*)"Reading event");

    event_add(ev,&five_sce);
    //    event_base_loop(base,EVLOOP_ONCE|EVLOOP_NONBLOCK);
    event_base_dispatch(base);


}
int main(void)
{
    evutil_socket_t fd;
    main_loop(fd);
    return 0;
}



void read_cb(evutil_socket_t fd , short flag, void * arg)
{
    (void)fd;
    (void)flag;
    (void)arg;

}

void write_cb(evutil_socket_t fd , short flag, void * arg)
{
    (void)fd;
    (void)flag;
    (void)arg;

}

void main_loop(evutil_socket_t fd)
{
    struct event_base * base = event_base_new();
    event_base_priority_init(base,2);

    struct event * read_ev = event_new(base,fd
                                       ,EV_READ | EV_PERSIST,read_cb,NULL);

    struct event * write_ev = event_new(base,fd
                                        ,EV_WRITE | EV_PERSIST,write_cb,NULL);

    event_priority_set(read_ev,0);
    event_priority_set(write_ev,1);
}

int main(void)
{
    evutil_socket_t fd;
    main_loop(fd);
    return 0;
}

#endif

