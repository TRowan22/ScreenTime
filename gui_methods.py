import datetime
import graphs

class GuiMethods:
    def __init__(self):
        self.curr_date = datetime.date.today()
        self.mode = "day"

    def change_label(self, given_mode):
        """
        Changes whether the label displays time by weeks or days
        :param given_mode: Week mode or Day mode
        """
        if given_mode == "day":
            self.curr_date = datetime.date.today()
        if given_mode == "week":
            self.curr_date += datetime.timedelta(days=-self.curr_date.weekday(), weeks=0)

    def change_by_one(self, forward):
        """
        Changes the day by either forward one or backwards one
        :param forward: whether we are moving forwards or backwards one
        """
        if self.mode == "day":
            self.curr_date += datetime.timedelta(days=(1 if forward else -1))
        if self.mode == "week":
            self.curr_date += datetime.timedelta(weeks=(1 if forward else -1))

    def check_mode(self, mode):
        """
        Updates the date label to reflect the current date
        :param mode: either day or week
        """
        if mode == "day":
            return self.curr_date.strftime("%A, %B %d, %Y")
        if mode == "week":
            return f'Week of Monday, {self.curr_date.strftime("%B %d, %Y")}'
