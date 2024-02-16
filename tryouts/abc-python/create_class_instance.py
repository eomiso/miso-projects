class Factory:
    def __new__(cls, factory_calss=None, **kwargs):
        if factory_calss is None:
            return super().__new__(cls)
        else:
            instance = factory_calss.__new__(factory_calss, **kwargs)
            instance.__init__(**kwargs)
            return instance
