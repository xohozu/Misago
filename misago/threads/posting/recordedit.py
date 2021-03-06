from django.db.models import F

from misago.threads.posting import PostingMiddleware, EDIT


class RecordEditMiddleware(PostingMiddleware):
    def __init__(self, **kwargs):
        super(RecordEditMiddleware, self).__init__(**kwargs)

        if self.mode == EDIT:
            self.original_title = self.thread.title
            self.original_post = self.post.raw

    def save(self, form):
        if self.mode == EDIT:
            # record edit
            pass
