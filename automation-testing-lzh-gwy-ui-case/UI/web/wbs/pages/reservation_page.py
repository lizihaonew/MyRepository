from UI.base_page import BasePage
from ..elements.reservation_elements import ReservationQueryElementCollection, ReservationListElementCollection


class ReservationPage(BasePage):

    view_url = '/html/reservation.html'

    def __init__(self, browser):
        self.reservation_query = ReservationQueryElementCollection()
        self.reservation_list = ReservationListElementCollection()
        self.set_browser(browser)
        self.get_url()

    def search_reservation(self, status):
        self.reservation_query.reserve_status('text={0}'.format(status))
        with self.wait_for_page_load(self.reservation_list.reserve_status()[0]):
            self.reservation_query.query_button.click()
        reservation = self.reservation_list.reserve_status
        return [reservation.get_text(index) for index in range(0, len(reservation()))]
