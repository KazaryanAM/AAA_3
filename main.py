class CountVectorizer:
    """Подается текст в виде списка из строк. Можно вывести количество вхождений слова в строку для всего текста """
    def __init__(self, text: list):
        self.corpus = text

    def get_dict(self):
        """Возвращает словарь, где все слова будут ключами, в значениями будут нули. """
        text1 = self.corpus
        text2 = ''
        for string in text1:
            text2 += f' {string}'
        text2 = text2.lower()
        return dict.fromkeys(tuple(text2.split()), 0)

    def fit_transform(self):
        """Для каждой строки из текста выводит количество вхождений слов в эту строку. """
        text = self.corpus
        result = []
        for string in text:
            d = self.get_dict()
            string = string.lower()
            for word in string.split():
                d[word] += 1
            result.append(d.values())
        return result

    def get_feature_names(self):
        """Выводит все различные слова из текста."""
        d = self.get_dict()
        return d.keys()


if __name__ == '__main__':
    corpus = ['Crock Pot Pasta Never boil pasta again', 'Pasta Pomodoro Fresh ingredients Parmesan to taste'
              ]
    vec = CountVectorizer(corpus)
    print(vec.get_feature_names())
    print(vec.fit_transform())
