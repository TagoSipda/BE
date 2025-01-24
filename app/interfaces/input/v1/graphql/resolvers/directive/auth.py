def auth_resolver(func):
    def wrapper(*args, **kwargs):
        # 인증 로직을 추가 (예: AccessToken 확인)
        # raise Exception("Not authenticated") 를 통해 인증 실패 처리
        return func(*args, **kwargs)

    return wrapper
