from math import ceil


class Paginator:
    '''kwargs参数说明,order_field是按什么字段的顺序排序,reverse是否倒序'''
    def __init__(self, queryset, page, per_page, **kwargs):
        self.page = page
        self.perpage = per_page
        self.count = len(queryset)
        self.num_pages = ceil(self.count / self.perpage)
        self.queryset = self.change_queryset(queryset, page, per_page, **kwargs)
        self.page_range = [x for x in range(1, self.num_pages+1)]

    def change_queryset(self , queryset, page, per_page, **kwargs):
        if kwargs.get('order_field', ''):
            order_field = kwargs.get('order_field', '')
            queryset = self.change_order(queryset, order_field)
        if kwargs.get('reverse', ''):
            queryset = self.quertset_reverse(queryset)
        return self.queryset_split(queryset, page, per_page)

    def change_order(self, queryset, order_field):
        return queryset.order_by(order_field)

    def quertset_reverse(self, queryset):
        return queryset.reverse()

    def queryset_split(self, queryset, page, per_page):
        return queryset[(page - 1) * per_page:page * per_page]

