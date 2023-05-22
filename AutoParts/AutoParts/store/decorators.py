from django.http import HttpResponse


def allowed_users(groups=[]):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            if not request.user.is_authenticated:
                return HttpResponse('You need to login to access these instruments!')
            groups_names = [x.name for x in request.user.groups.all()]
            result = set(groups_names).intersection(groups)
            if not result:
                return HttpResponse(
                    f'You need to be member in at least one of the following groups: {", ".join(groups)}')
            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator
