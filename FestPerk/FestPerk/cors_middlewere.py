


class DisableCorsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        print(response)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = "DELETE, GET, OPTIONS, PATCH, POST, PUT, HEAD"
        response['Access-Control-Allow-Headers'] = "accept, accept-encoding, authorization, content-type, dnt, origin, user-agent, x-csrftoken, x-requested-with"
        return response