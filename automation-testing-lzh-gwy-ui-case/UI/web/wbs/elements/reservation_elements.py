from UI.base_element import BaseElement, AsyncElement, ElementCollection
from UI.special_elements.select_element import SelectElement


class ReservationQueryElementCollection(ElementCollection):

    def __init__(self):
        self.reserve_status = SelectElement('#status')
        self.product_name = BaseElement('#productName')
        self.advisor_name = BaseElement('#advisorName')
        self.customer_name = BaseElement('#customerName')
        self.customer_mobile = BaseElement('#mobile')
        self.query_button = BaseElement('#_query')


class ReservationListElementCollection(ElementCollection):

    def __init__(self):
        self.product_name = AsyncElement('.gradeX td:nth-child(2)')
        self.reserve_money = AsyncElement('.gradeX td:nth-child(3)')
        self.reserve_status = AsyncElement('.gradeX td:nth-child(8)')
        self.action = AsyncElement('.gradeX td:last-child')
