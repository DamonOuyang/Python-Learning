#include <stdio.h>
#include <event2/event.h>

int main(void)
{
    struct event_base * base;
    struct event_base * base1;
    struct event_base * base2;
    enum event_method_feature f;
    base = event_base_new();
    base1 = event_base_new();
    base2 = event_base_new();
    if(!base)
    {
        puts("Couldn't get an event_base!");
    }
    else
    {
        puts(event_base_get_method(base));
        f = event_base_get_features(base);

        if((f & EV_FEATURE_ET))
            puts("EV_FEATURE_ET");
        if((f & EV_FEATURE_FDS))
            puts("EV_FEATURE_FDS");
        if((f & EV_FEATURE_O1))
            puts("EV_FEATURE_O1");

    }
    return 0;
}


#if 0
int main(void)
{
    struct event_config * cfg;
    struct event_base * base;

    cfg = event_config_new();

    event_config_avoid_method(cfg,"select");
    event_config_require_features(cfg,EV_FEATURE_ET);
    event_config_set_flag(cfg,EVENT_BASE_FLAG_EPOLL_USE_CHANGELIST);

    base = event_base_new_with_config(cfg);
    event_base_priority_init(base,5);

//    puts(event_base_get_method(base));
    puts(event_base_get_features(base));

    event_config_free(cfg);
    event_base_free(base);
}

int main(void)
{
    struct event_base * base = event_base_new();
    puts(event_get_version());

    const char **methods0 = event_get_supported_methods();

    puts(event_get_version());
    int i = 0;

    while(methods0[i] != NULL)
    {
        puts(methods0[i++]);
    }

    event_base_free(base);
    return 0;
}
#endif
