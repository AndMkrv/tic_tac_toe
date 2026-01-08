class FieldIndexError(IndexError):
    """
    Это класс для обработки исключений IndexError
    """

    def __str__(self):
        return 'Введено значение за границами игрового поля'
