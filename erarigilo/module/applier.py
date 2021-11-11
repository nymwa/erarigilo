class TokenWiseApplier:

    def apply(self, sent, lottery):

        for index in range(len(sent)):
            if self.rule.cond(sent[index]) and lottery():
                sent[index] = self.rule(sent[index])

        return sent


class IndexWiseApplier:

    def apply(self, sent, lottery):

        for index in range(len(sent)):
            if self.rule.cond(sent, index) and lottery():
                sent = self.rule(sent, index)

        return sent


class SpanWiseApplier:

    def apply(self, sent, lottery):

        span_list = self.rule.extract_span(sent)
        for span in span_list:
            if lottery():
                sent = self.rule(sent, span)

        return sent

