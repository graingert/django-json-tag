def dumps(*args, **kwargs):
    """
    Wrapper for json.dumps that uses the JSONArgonautsEncoder.
    """
    import json

    from django.conf import settings
    from .serializers import JSONArgonautsEncoder

    kwargs.setdefault('cls', JSONArgonautsEncoder)
    # pretty print in DEBUG mode.
    if settings.DEBUG:
        kwargs.setdefault('indent', 4)
        kwargs.setdefault('separators', (',', ': '))
    else:
        kwargs.setdefault('separators', (',', ':'))

    return json.dumps(*args, **kwargs)
