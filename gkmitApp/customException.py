class BalanceInsufficentError(Exception):
    def __init__(self,arg):
        self.msg = arg


class BalaceExceedError(Exception):
    def __init__(self,arg):
        self.msg = arg

