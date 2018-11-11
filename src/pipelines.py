from src.sentiment_analyzer import SimpleSentimentAnalyzer
from src.tokenizers import SimpleSentenceTokenizer, SimpleTokenizer


class SimplePipeline(object):
    """
    Provides a means for linking NLP classes together that transform text data
    """

    def __init__(self, raw_text, features):
        """
        :param: input_text: string raw text document containing one or more sentences
        :param: features: list<string> features to run in pipeline

        """
        self.raw_text = raw_text
        self.features = features

        self.tokenized_sents = None
        self.tokenized_words = None
        self.sent_scores = None
        self.output = None

    # noinspection PyUnusedLocal
    def run(self):
        """
        Execute the transformation methods on attrs in the pipeline
        """
        res = self.raw_text
        for feature in self.features:
            try:
                print("applying: {}".format(feature))
                res = getattr(self, feature)(res)

            except AttributeError as e:
                print(e)
                print("SimplePipeline supports no feature named: {}"
                      .format(feature))

        self.output = res

    def sent_tokenize(self, input_text):
        """
        Invokes the tokenize method on SimpleSentenceTokenizer
        :param input_text: string text to tokenize
        """
        st = SimpleSentenceTokenizer()
        sents = st.tokenize(input_text)
        self.tokenized_sents = sents
        return sents

    def word_tokenize(self, input_texts):
        """
        Invokes the tokenize method on SimpleWordTokenizer
        :param input_text: string text to tokenize
        """
        st = SimpleTokenizer()
        all_words = [st.tokenize(text) for text in input_texts]
        self.tokenized_words = all_words

    def score_sentiment(self, input_texts):
        """
        Invokes the score method on the SimpleSentimentAnalyzer
        :param input_text: string text to sentiment score
        """
        sa = SimpleSentimentAnalyzer()
        sent_scores = [sa.score(text) for text in input_texts]
        self.sent_scores = sent_scores
        return sent_scores
